import os
import whisper
import re
import pandas as pd
from moviepy.video.io.VideoFileClip import VideoFileClip  # Changed import

# Use AudioFileClip for audio conversion
from moviepy.audio.io.AudioFileClip import AudioFileClip
from spacy.lang.zh import Chinese  # Add this import
from spacy.lang.en import English  # Add this import
import spacy  # Add this import
from langdetect import detect, detect_langs, LangDetectException  # Add this import

# the following functions are used in the main.py file,
# most of them are convertors, from ulr, video and audio and subtitle
# to vtts text files.


def parse_subtitle(file_path, vtt_file=None):
    """
    Parses various subtitle formats (.ass, .sub, .srt, .txt, .vtt) into a DataFrame.
    If vtt_file is provided, it will be used directly as the content.
    """
    if vtt_file is None:
        try:
            with open(file_path, "r", encoding="utf-8-sig", errors="replace") as file:
                lines = file.readlines()
        except FileNotFoundError:
            return pd.DataFrame(columns=["Timestamps", "Content"])
        except ImportError:
            print("pysrt library not found. Falling back to less robust parsing.")
    else:
        lines = vtt_file.splitlines()

    timestamps = []
    contents = []
    current_content = []
    if file_path.lower().endswith(".txt") or (
        vtt_file is not None and file_path.lower().endswith(".txt")
    ):
        contents = lines
        timestamps = [""] * len(contents)
    else:
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            # Added pattern to support timestamps like "00:00:51.160 --> 00:01:00.700"
            if "-->" in line or re.match(
                r"\d{2}:\d{2}:\d{2}[,\.]\d{3} --> \d{2}:\d{2}:\d{2}[,\.]\d{3}", line
            ):
                timestamps.append(line)
                i += 1
                current_content = []
                while (
                    i < len(lines)
                    and lines[i].strip()
                    and not re.match(
                        r"\d{2}:\d{2}:\d{2}[,\.]\d{3} --> \d{2}:\d{2}:\d{2}[,\.]\d{3}",
                        lines[i].strip(),
                    )
                ):
                    current_content.append(lines[i].strip())
                    i += 1
                contents.append(" ".join(current_content))
            elif "Dialogue:" in line or re.match(r"{\d+}{\d+}.*", line):
                timestamps.append(line)
                i += 1
                current_content = []
                while (
                    i < len(lines)
                    and lines[i].strip()
                    and not lines[i].strip().isdigit()
                ):
                    current_content.append(lines[i].strip())
                    i += 1
                contents.append(" ".join(current_content))
            else:
                i += 1

    return pd.DataFrame({"Timestamps": timestamps, "Content": contents})


def rm_rep(file_path):
    """Removes repeated words/phrases from a file."""
    try:
        vtt_df = parse_subtitle(file_path)
        all_content = " ".join(vtt_df["Content"])
        pattern = r"(([\u4e00-\u9fa5A-Za-z，。！？；：“”（）【】《》、]{1,5}))(\s?\1)+"
        return re.sub(pattern, r"\1", all_content)
    except Exception as e:
        return f"An error occurred: {e}"


def transcribe(file_path, language=None, output_dir=None):
    """
    Transcribes an audio file to a WebVTT file with proper timestamps.
    Now accepts an optional output_dir where the VTT file will be saved.

    Args:
        file_path (str): Path to the audio file
        language (str, optional): Language code for transcription.
        output_dir (str, optional): Directory to save the VTT file. Defaults to current directory.

    Returns:
        tuple: (Path to the generated VTT file, auto-detected language)
    """
    base, ext = os.path.splitext(file_path)
    ext = ext.lower()

    model = whisper.load_model("large-v3-turbo", device="cpu")
    result = model.transcribe(
        file_path, fp16=False, verbose=True, language=language if language else None
    )
    detected_language = result.get("language", language if language else "unknown")

    # Create VTT content with proper timestamps
    vtt_content = ["WEBVTT\n"]
    for segment in result["segments"]:
        # ...existing timestamp formatting...
        hours = int(segment["start"] // 3600)
        minutes = int((segment["start"] % 3600) // 60)
        start_seconds = segment["start"] % 60
        end_hours = int(segment["end"] // 3600)
        end_minutes = int((segment["end"] % 3600) // 60)
        end_seconds = segment["end"] % 60

        start_time = f"{hours:02d}:{minutes:02d}:{start_seconds:06.3f}"
        end_time = f"{end_hours:02d}:{end_minutes:02d}:{end_seconds:06.3f}"
        text = segment["text"].strip()
        vtt_content.append(f"\n{start_time} --> {end_time}\n{text}")

    # Use provided output_dir or default to the base file's directory
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(file_path))
    else:
        os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    out_file = os.path.join(output_dir, base_name + ".vtt")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("".join(vtt_content))

    return out_file, detected_language


def segment(file_path, sentence_count=8):
    """
    Segments a text file into paragraphs by grouping every N sentences.

    Args:
        file_path (str): Path to the text file
        sentence_count (int): Number of sentences per paragraph (default: 8)

    Returns:
        str: Paragraphs joined with double newlines
    """
    text = rm_rep(file_path)  # Integrate rm_rep here

    # Directly use basic language classes
    if any(char in text for char in "，。？！"):
        nlp = Chinese()  # Use basic Chinese
    else:
        nlp = English()  # Use basic English

    # Add the sentencizer component to the pipeline
    if "sentencizer" not in nlp.pipe_names:
        nlp.add_pipe("sentencizer")

    doc = nlp(text)

    paragraphs = []
    current_paragraph = []
    current_count = 0
    for sent in doc.sents:
        current_paragraph.append(sent.text)
        current_count += 1
        if current_count >= sentence_count:
            paragraphs.append(" ".join(current_paragraph))
            current_paragraph = []
            current_count = 0

    if current_paragraph:
        paragraphs.append(" ".join(current_paragraph))

    segmented_text = "\n\n".join(paragraphs)
    return segmented_text


def download_audio(url, output_dir=None):
    """
    Download audio from a URL and convert it to WAV format.

    Args:
        url (str): URL of the video/audio to download
        output_dir (str, optional): Directory to save the downloaded file

    Returns:
        str: Path to the downloaded WAV file
    """
    import yt_dlp

    if output_dir is None:
        output_dir = os.getcwd()

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
            }
        ],
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "quiet": False,
        "no_warnings": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            output_file = ydl.prepare_filename(info).rsplit(".", 1)[0] + ".wav"
            return output_file
    except Exception as e:
        raise Exception(f"Error downloading audio: {str(e)}")


def video_to_audio(video_path, output_dir=None):
    """
    Extracts audio from a video file and converts it to WAV format.

    Args:
        video_path (str): Path to the video file.
        output_dir (str, optional): Directory to save the audio file. Defaults to the current working directory.

    Returns:
        str: Path to the extracted WAV audio file.
    """
    if output_dir is None:
        output_dir = os.getcwd()

    base_name = os.path.splitext(os.path.basename(video_path))[0]
    audio_path = os.path.join(output_dir, f"{base_name}.wav")

    try:
        video_clip = VideoFileClip(video_path)
        video_clip.audio.write_audiofile(
            audio_path, codec="pcm_s16le"
        )  # Ensure WAV format
        video_clip.close()
        return audio_path
    except Exception as e:
        raise Exception(f"Error extracting audio from video: {e}")


def language_detect(file_path, detected_lang=None):
    """
    Detects the language of a text file using langdetect.
    Returns language code (e.g., 'zh', 'en', 'ja', etc.).
    """
    try:
        df = parse_subtitle(file_path)
        sample_content = " ".join(df["Content"].head(20))
        
        # Try to detect language with confidence scores
        languages = detect_langs(sample_content)
        if languages:
            # Get the most probable language
            detected = languages[0].lang
            # Normalize Chinese variants
            return 'zh' if detected.startswith('zh') else detected
            
    except LangDetectException as e:
        print(f"Language detection error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error in language detection: {str(e)}")
    
    # Fallback to basic character detection
    if any(ord(c) > 0x4E00 and ord(c) < 0x9FFF for c in sample_content):
        return "zh"
    return "en"


def audio_wav(audio_path, output_dir=None):
    """
    Convert any audio file to WAV format using MoviePy.

    Args:
        audio_path (str): Path to the input audio file
        output_dir (str, optional): Directory to save the WAV file. Defaults to same directory as input.

    Returns:
        str: Path to the converted WAV file
    """
    if output_dir is None:
        output_dir = os.path.dirname(audio_path)

    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    wav_path = os.path.join(output_dir, f"{base_name}.wav")

    # Skip conversion if file is already WAV
    if audio_path.lower().endswith(".wav"):
        return audio_path

    try:
        audio_clip = AudioFileClip(audio_path)
        audio_clip.write_audiofile(wav_path, codec="pcm_s16le")  # PCM format for WAV
        audio_clip.close()
        return wav_path
    except Exception as e:
        raise Exception(f"Error converting audio to WAV: {e}")
