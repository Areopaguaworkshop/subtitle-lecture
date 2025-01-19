import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import os
    import re
    import dspy
    return dspy, mo, os, re


@app.cell
def _():
    def _(dspy, os):
        os.environ['GEMINI_API_KEY'] = "GEMINI_API_KEY"
        lm = dspy.LM('gemini/gemini-1.5-flash')
        dspy.configure(lm=lm)

        # Define the signature for the module
        signature = 'text: str -> segmented_text: str'

        # Create the Predict module with the specified signature
        segmenter = dspy.Predict(signature)

        # Define the prompt template for paragraph segmentation
        def segment_text(text):
            prompt = (
                # "Segment the following text into coherent paragraphs. Ensure that each paragraph focuses on a specific topic or idea. Rewrite each paragraph with the same language, with a formal, written style, ensuring the same meaning is preserved:\n\n"
                # "Segment the following text into coherent paragraphs. Ensure that each paragraph focuses on a specific topic or idea:\n\n"
                # "按写作规范重写每个段落，确保保留相同的意思。按文意分段，确保每段有明确主体:\n\n"
                # "按文意分段，确保每段有明确主体:\n\n"
                # "删除其中的语气词，比如好，好的等，删除其中重复出现的字词:\n\n"
                "请插入中文标点:\n\n"
                f"{text}\n\n"
                "Segmented Text:"
            )
            return segmenter(text=prompt).segmented_text

        input_text = """"
           
            
            是另外一个就是系统就是那个CalvinCalvin教就是特别在瑞士还有在就是荷兰北部瑞士西部好像是教尔文嘛John Clavin对吧对呀对Calvin对他是他原来是啊啊啊啊啊啊他原来是法国人可以说是法国人因为那时候啊那个瑞士还是不算是存在的但是啊那个瑞士的那个存在的就是基本原则是为了保护就属于那个罗马帝国还有那个法国的就是宗教改革的因为就是理论上他们都是非法的就是所以他们就是开始造成一个新的那个国家就是那个瑞士荷兰北部也是完全一样因为他们那时候也算是西班牙的一个殖民地就是他们属于西班牙是完全百分之百是天主教的一个国家所以他们开始把就是他们自己的宗教改革者就是他们开始就是压迫他们英国一样就是在英国有就是你们都知道那个英格兰的就是那个宗教改革的故事苏格兰有他自己的故事就是他们很苏格兰的那个新教和荷兰瑞士的还有法国的那个宗教改革是有同样的原则但是我们现在看的是那个村子的地区因为他们就是除了这一部分以外他们都是北欧的他们都是就是德国中部还有那个北欧的地区这个地区一直到现在都是鲁德宗的就是他们他没有改变然后有好多战争就是十六世纪的战争十五世纪的那个战争已经是存在的但是十六世纪的十七世纪的那个战争是宗教类的一种那个战争但是不一定是宗教类的战争但是不一定是宗教类的一种那个战争但是不一定是宗教类的战争但是不一定是宗教类的战争那些原因完全是宗教的非常重要的一部分就是农民的就是经济情况因为他们越来越多就是在就是经过那个宗教改革因为他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革他们越来越多就是在就是经过那个宗教改革因为基本上是梵天驻以在欧洲的最后一段然后就是开始的时候我们的那个马丁·路德他就是指示农民他说他们当然有那个就是那个旗的权利但是他们这个旗就是慢的就是发展成一种用英文说是clas warfare就是他们就是普通的那个社会阶级就是互相消灭就是由于不同阶级的人相互消灭OK对你有问题吗没有我就补充一下对那你就是因为这一方面就是19世纪的时候有一个有两个人一个是马克思另外一个是那个弗里希·安根斯他们都跟马丁·路德的那个看法就是他们完全同意开始的那个看法因为他们说那就是那个农民战争基本上是就是新时代的一个标志但是我自己当然就是有也觉得他们有的时候是比较过分的就是同意的因为马丁·路德的看法基本上是神学家的一个看法他说他就他最有名的一个最有名的一个文章就是他自己写成的一种辩论这个辩论以后就是变成为95条论感然后他就是把他自己的想法就是把首先在自己的那个屌汤门口以外就是给大家看但是以后他也就是在很多就是跟他同意的出版社就是他们开始就是用各种就是各地语言比如说德国语言比如说德国语言比如说德国语言比如说德国的那个地方语言或者河南或者北欧就印书就是小的报纸类的文章然后他们就开始跟布马尼的农民影响到他们自己的那个社会关于社会改革的看法所以宗教改革和社会改革从头开始是两种就是同类的盘旺所以宗教改革和社会改革从头开始是两种就是同类的盘旺我们现在就是慢就是在中国因为经过马克思恩格斯我们一定会到中国明清代的那个最厄烈的那个就是情况的厄烈的那个就是情况的就是也有同样的那个农民气宜但是中国的那个农民气宜他们一般都有佛教的印象所以他们虽然这是一个非常大的从神学方面来说非常大的一个区别但是到我们现在这个世上但是到我们现在这个世上就是19世纪到了中国的鲁德宗传教士他们会看到同类的情况比如说你看这里的那个农民战争和中国的那个对不起啊中国乡下的情况都差不多所以他们很会理解农民就是想改良他们自己的那个生活情况好那这里这个是上面就是用繁体字写的但是我也给你们看一个简体字就是这个对你们来说就是大概就是简单一些但是我给你们看就是三个人物一个是就是那个他就可以说是中国第一个鲁德宗的传教士他当然是比较那个他的宣道方法是比较就是比较独特的就是有的时候也说他是上英国人的那个鸦片船就是进入中国然后他就是用就是卖给鸦片的方式就是卖给就是西方的一种一个宗教对可以这样认为但是当然不是对的因为那时候就是有啊就是西方和中国之间的那个交流是非常就是少的所以他用的船当然是英国人的船还有就是之前他用了荷兰人的船因为他开始的时候也在荷兰非常有就是他就开始学习鲁德宗的就是基本原则后来这是最早的一些就是那个鲁德宗的就是组织他们就是学宣道会他们有他们都大部分是德国人开的包括现在瑞士的那个巴斯会基本上是德国人开的一个就是当时的住在就是瑞士就是新教的一块的一个就是一个教会这个教会就是他们也是慢的用英国人的船就是进入中国最有名的一个人就是那个汉伯就是在这边他是帖多尔汉伯他是汉山明还有一个德国人他叫利勒吉就是下面的他们两个人他们都是他们跟国师拉同样的一个方法就是进入中国就是他们坐船然后他们就这是鸦片战争以后他们也可以就是用那个就是不平等跳跃五个港口他们在那边就是可以准备他们自己的那个China mision就是那个中国的那个传教事业他们的这个传教事业他们的这个传教事业他们的这个传教事业他们的这个传教事业他们的这个传教事业他们的这个传教事业他们的这个阶级他们的这个内塔他们的这个制度他们的这个境界他们的这些不同的而且他们的资源他们的观点就是越来越多远Gro uncertainty就是这个那个战国时代的那个亲国他们就慢把所有的德国就是将德国的地区除了奥地利之外他们都把它就是变成他们自己的那个国家的一部分那个Prusia就最明显的一个方面也是他们从头开始都是新教的所以他们也欢迎从整个欧洲特别从法国和比利时就是跑到新教的地区就是来坚持他们自己的国家因为开始的时候是非常穷的一个国家那时候最在北欧最有权力的一个大帝国就是瑞典和芬兰一起这是一个国家还有那个这一块就是埃塞尼亚他们拉特维亚就是这一块他们都属于那个瑞典大帝国他们也是从头开始算是新教的那个鲁德尊在那里是一个很重要的所以罕白他是瑞典人勒斯勒他是德国人格斯拉夫他也是德国人但是他跟荷兰人也有交流下面的就是那个巴斯汇的就是在瑞士的一个中心就是最大的一个建筑这个就是那个瑞典大帝国的一个建筑这个是就是那个瑞典大帝国的一个建筑这个是就是那个瑞典大帝国的一个建筑这个是就是那个瑞典大帝国的一个建筑就是那个瑞典大帝国的一个建筑这个是那个瑞典大帝国的一个建筑这个是那个瑞典大帝国的一个建筑这个创造是德国西部一块德国西部一般是天诸教的但是稍微往北就是我们进入那个新教的地区所以从那时候一来我们就很新的一个情况就是很新的一个情况这些就是开始的时候极少人他们在港口就是那个比如说上海或者福州或者厦门遇到的就是已经成为基督教或者天主教的信徒他们一般以前也是信徒这都是耶稣会或者天主教所有的教会的工作然后他们就是把他们就是再次皈依就是归心后他们成为就是那个卢德众的人对这里我们有就是比较早的一个教会就是无常日言行道会那个他们就是在就是那个行道会你看这里这个字原来的名字是瑞典的传教会的那个地区就是整个中国但是我们很快会理解天津教育以后就是先方八年以后我们也会再来讲一下这个天津教育的传教会这个天津教育的传教会就是在西部和南部的港口里面的传教士他们突然会就是他们允许去中国内地他们跟别的国家的新教和天主教的那个传教士也有交流最重要的一个就是英国英格兰的那个内地会英格兰的内地会1951年的后期joke他们大会中国内地会bilder对于传教园我们就有他们的那个档案所以对于那个中国内地会 ecosystem的话那你们可以就是来伦敦大学那个亚非学院可以研究这些文献啊从那时候以来欧洲所有的卢德宗他们跟英格兰的中国内地会有密切的关系因为他们的组织是最发达的他们在中国任何的一个地方都有mision base他们自己的那个传教中心非常重要的一个地方就是现在的那个武汉口 汉阳和武昌人员一直到现在就是能看到陆德宗的传教中心最明显的是在这个地区就是瑞典的但是还有诺威马上就是给你们讲诺威的就是更多这里我就是给你们写下这是比较完整的一个就是一个每一个陆德宗每一个就是新一会的名称他就是每一个新一会的名称他就是每一个新一会的名称他们都是国外的你们看在这里基本上有三种一个是就是德国的包括瑞士的那个巴斯是那个巴斯会这个是巴林是柏林就是柏林的就是后来德国的那个首都还有北欧的北欧国家包括丹麦就是是很有趣的一个例子我以后给你们讲为什么是这样另一个是挪威还有瑞典就是那时候整个晚清时代就是从1817年以来就是是甲青时代就是一直到1905年他们两个国家是他们有一个他们是联合起来的他们是一个国家有两个首都的一个国家就是跟苏格拉和英格兰就是的情况完全一样所以基本上挪威和瑞兰的传教士他们都是一个国家就是派到中国的腾兰那时候就是属于俄罗斯就是1817年以后就是也是这就是有个战争就是俄罗斯和瑞典之间的一个战争所以他们突然就是属于俄国但是芬兰的传教士他们都是信那个卢德总所以他们经常就是用瑞典的那个传就是去中国第三个方面这是很有趣这是美国这是北美那时候并不是就是讲英文的美国人他们都讲北欧的语言为什么是这样?因为那时候有很多人就是他们离开北欧因为北欧的国家那时候还是比较穷都是农就是农村多的地方所以有的时候就是冬天就是非常冷的时候有好多人他们就是他们饿死他们真的饿死了所以给你一个例子就是1900年就是瑞典不知道也是挪威的但是我估计在挪威的情况也是同类的挪威和瑞典的人口三分之一都移民美国他们都去那个密西根就是那个密西根就是那个密西根那个大户地区然后在那些地区突然有卢德宗多的就是教会这些教会他们也派人就是往中国所以就是德国北部完全的洋他们也是就是排经过美国经过就是北美往中国的那个传教士这是历史上非常有趣的这个例子所以这里就是挪威和瑞典的国际您看就是跟英国的那个国际就都差不多就是因为是联合起来的一个国家还有丹麦还有本来是属于那时候属于俄国这个德国171年以前就是不是存在的这个最大的一个一块地区都是那个帕萨他们都是那个帕萨的基本上是卢德宗的一个地区然后德国南部有天主教的然后在北部多大部分是卢德宗的包括就是那个瑞士的北部和西部他们多大部分也是卢德宗的不是卢德宗是那个卡尔滨是新教的对好所以他们我们最我们经常会见到的文献是用德文献的就是在后面就是有柏林1901年就是出版的一个就是一个传教期刊在左边的是那个马丁路德用的一个教义就是用中文大概是那个教义文的所以这是非常对本地的信徒是义务的就是他们必须把这个教义就是背下来的然后有神父就是一个牧师他有的时候会给他们敲门然后就是他们必须知道那个教义文的里面的就是最重要的部分这是基本上是就是大清国的那个形式这是就是民国时期的一个地图这个你们看就是卢德宗在什么地方会有就是基本上在这一地区就是在不行就是我们在湖北湖南还有一块就是一小块在河南有还有稍微就是往西就是在重庆西但是很重要也有在内蒙古就是不同的地方还有甘肃宁夏就是这些地方但是当然那时候就是信徒很少传教士也是比较少的所以对于当代的传教士来说经常有一个好处因为他们没有那个金帐就是没有别的传教士干涉他们自己的工作特别是瑞典的传教士他们就是经常在就是内蒙古还有在就是新疆就是开始就是部队我在这里就是给你们写下他们的地区你看就是那个祥传就是你们看你们跟中国的那个地图比较熟悉的人你们跟中国的那个地图比较熟悉的人你们会知道就是在地图上的地区大概在什么地方就是有一个河北当然是靠蒙古的那个方向新疆就是新疆的意思对还有一小部分在就是在云南但是大部分就是在中部和北部好那我快讲完就是我给你们讲就是后来在中国发展还有那个新疆特别是那个鲁德中在世界上各个地方的影响但是特别在北欧所以看那个清朝最后的二十年左右过去选通的那个年代你们会看最重要的传教士传教会他们仍然是德国北部和就是北欧还有一些就是美国就是去中国的但是他们也是慢就变成本地化的一种教会在很多地方就是中国的那个本地人的地位就是原来的来那时候我们可以说就是新疆就是那个鲁德中在中国的本地化在下面就是当然是德国人在青岛就是盖的一个教堂就是我看是整个中国就是最大的一个教堂所以他们从外面那时候他们当然是在中国的一个教堂就是他们的影像就是不少您看在这里就是这个是有25个不同的那个鲁中教会他们都是西方人派的就是没有一个就是中国本地的1907年就是他们从那时候开始就是把中国的就是分开不同的那个教区这些教区就是对于以后的那个发展特别是那个三次时代以来就是非常重要因为他们从那时候我们会知道就是悉尼教的那个角度在他们都在什么地方有一个问题就是传教士的不同民族背景所以他的意思是他们经常就是不能就是听不懂互相的语言所以如果他们是丹麦人他们当然就是会学会那个日语和德语但是他们经常就是也不带他们也不算是语言学家所以他们学习的语言越来越多是中文所以他们那个本土化也就是影响到他们自己的那个认同对总是采用那个新译为了主张就是来寻找的那个结合对所以他们从那时候就是那个伦敦诵就是不是平常就是用的一种词在中文就是那个新译就是开始更多就是用对然后就是这个他们就是那个鲁德宗就是那个新译众他们设立一个就是中心那个中心是美国人芬兰人和挪威人就是开的1900年有个非常就是重要的一个大使就是那个义和团就是对新译教最大的影响是他们基本上叫他们不允许就是依靠国外的就是武士因为在全国就是中国只有一个国家会就是派人就是派兵队保护他们的传教士就是德国就是他们然后就是在中国任何的一个地方就是他们有非常重要的一个地位但是一直到第一次世界大战争因为以后德国的那个就是殖民地就是突然没有了我们快到了那个最后一些图片就是你看在这边就是有一个就是个学校这是20年基本上是就是民国时期洗礼教会跟就是所有的国外的那个教会一样他们有一个新的方向这个方向是不太照就是新的那个新图但是一定要主张就是那个医疗你看在右边就是有武汉的一个非常重要的一个医院在韩国就是的就是三个原来就是三个地方都是传教士不一定是那个路德宗的但是瑞典和德国人的那个悉尼教会他们也参加那个就是那个医疗方法就是医疗传教方法左边是就是教会就是教育的一个例子就是一个耳子就是蒙学就是基督教的那个小学可以说是个小学但是他们在中学大学他们也参加这个教育就是事业对你们可以看在这里就是一直到现在就是这个医院就是还是存在的但是原来的医院当然就是现在是一种一个博物馆后来就是在这一方面是比较有趣的就是基本上就是中华人民共和国之前以挪威的就是在中华最后的一个传教中心就是在长沙就是长沙地区就是这里也有一个医院还有一个高中所以就是还有一个师范学院所以你看就是新一传教士他们的传教方法跟别的传教士传教会一样改变就是从就是神学从宗教就是主张宗教的到主张教育和医疗然后我给你一些例子这是下一段就是基本上是从1949年以来这些在中国内就是中国大陆之内当然有一个三次政策以后就是从那时候以来那个新一教就是属于那个基督教的那个组织但是在台湾在香港在就是在马来西亚就是在就是有基督教的就是华人的地区他们还是存在的所以这些名字都是例子就是你可以看就是原来在中国大陆也有当时比如说德国的那个但是他们现在就是如果是讲外语的话是英语就是他们原来的那个关系就是现在就是不存在的但是都大部分都是本体化的都是中国人的好那我现在就是给你一个这是也是一个在这里也是一个简体字的版本你们先看就是右边就是那个普世教就是这是一个在新教建筑教的1960年代以来的一个趋势这是他们的就是表征上就是一个船就是船上有一个十字想出来的地方很主要因为也是那个AugsburgAugsburg以前听说这是就是Martin Luther就是被开除的一个地方就是所以他们就是从就是60年代以来他们建筑教和新教他们开始慢就是把就是分开的方言就是都放就是放在他们认为是自由的不是最重要的方面他们都是属于那个基督教就是世界上的那个基督教英文名字是那个Ocumenism就是Ocumen希腊词是非常重要的一个概念基本上是就是自由和平就是公义的基础上就是他们想就是改成一个新的一种一个大社会那个大社会当然也是一个大教会两个例子在这里就是第一个是那个圣餐就是我以后就是给你就是建筑教的那个意见他们认为也有一点那个异端就是那个就是邪教的方面因为他对就是种族的那个建筑教来说建筑那个新义来说他们教义来说他们都是他们都是基督耶稣基督的那个肉和血他们不能就是看是就是神外的一回事但是新教他们新教徒他们一般就是认为是就是标志上就是那个symbolic的一个意思这个那个圣礼就是那个sacrament就是完全一样就是他们但是建筑教他们一直到现在就是还是那个就是那个呃那种普世教的去向好快完了就是给你们讲就是那个路德宗就是到在北欧的你看就是在这里是那个贫农就是非常穷的农民在Martin Luther生活的时候的一个图画就是路德教就是路德宗他就是帮助把非常穷的和就是基本上就是封建主义的一种那个社会变成一个福利国家的那个概念福利国家就是在选个北欧是非常普遍的国家选的一个概念然后社会稳定就是那个稳定的那个社会也是非常重要的因为像就是那个法国革命之前在北欧有一个就是路德宗的一种那个革命他们虽然一直到现在都有国王和就是国朝就是但是他们是归族但是他们的地位就是民族化的新一教他也就是从头开始主张那个免费大众教育所以他们以后在中国就是建设的中学和大学那个十分大学他们都是用同样的规则就建设起来就是免费或者非常便宜的给大家就是老百姓就是那个教育的意思教育的机会这是非常重要的包括就是能就是读书就是因为会读书的人他们也会读那个《圣经》这是马丁·路德所以基本上的一个这个他原理的但是我开始的时候也跟你们说马丁·路德他也给每一个国王一个权力那个权力是把是为就是为人民的那个我说的是那个道德健康是比较复杂的一个概念但是基本上就是他给国王就是开出邪教的那个权力还有一直到每个人的那个身体健康所以他在19世纪最重要的一个后果是每一个北欧国家他显示就是一般的人就是能喝的酒所以那个酒在北欧当然是非常那个恶德克还有就是非常强的那个包括毒品都是那个国家就是控制着就是比欧洲所有的地方就是控制的厉害这也是那个路德宗的一个后果教育就是体制就是我看北欧的那个政治制度和路德宗的教会之内的政治制度那个教会体制是同类的那两个是主张那个平等政治平等所以两个可以说那个路德宗他认为就是一个民主新的那个政治制度是最好的当然路德生活的时候就是没有现代化的那个民主制度所以他不会知道这个概念但是他也认为每一个就是身负和每一个信徒他基本上是平等的他是他没有虽然有国王制度但是他们都应该是他们应该有同样的就是政治权力主张的也是自由他有一个用德文写的小的那个书叫Wonderfreiheit in its case dimension就是信徒的自由是什么基本上他可以就是每天都决定他自己的生活应该是好的应该是坏的应该是他随着谁这当然农民记忆的时候也是比较有政治性的一种方面因为他们会决定他们也可以就是反对他们的国王但是这个自由是神学的一种自由所以后北欧国家他们都有那个同一世界的那个概念也主张那个和平我看了那个康游卫写的大同书以后我会我很有他学会了马丁路德的那个基本原则的印象因为康游卫的那个思维和马丁路德的思维有的时候是非常同类的最后还有就是文化上的印象比如说巴赫那个约翰斯巴斯天巴他是一个非常就是有信仰的一个就是信徒路德宗的信徒我们现在就是在特别在北欧但是在整个就是基督教还有天主教的那个教堂里面我们都听他的音乐还有别的就是德国的北欧的音乐家他们也是信徒但是特别是那个巴赫听到他的那个音乐以后你会知道就是他一定想就是给大家讲比较神学很深的一些方面非常感谢大家好的谢老曼教授的讲课讲得特别好完全是耳目一新的感觉我们已经开始有问题了我们先看一下这个问题吧路德宗作为一个具有路德神学标志的宗派的传教伙伴在晚清明初你认为对普通中国基督徒在思想上文化上最重要的影响是什么他留给今天中国教会的思想遗产拥有哪些好我没有听到就是最后一句说他留给今天中国教会的思想遗产有哪些好我在中国还有在就是香港是那个巴赫会的这个地区我讨论了这个问题他们都认为他们有那个心理教就是有积极的一种那个影响当然是就是建国那个概念跟就是那个路德宗的就是国民的那个责任的概念也是同类的所以他们两个是积极的就是他们对国家是积极的一种就是一个一种方面当然心理教他也主张就是个人的那个责任但是也是个人的自由所以他有的时候有一个矛盾这个矛盾在什么地方就是比如说中央政府或者各种各样的一种那个政府他们就是愿意就是每一个国民就是应该就是在一起就是进行一个政治上的那个方向如果一个就是个人的那个信徒就是觉得就是跟他自己的那个道德感就是不可能就是不是完全就是在一起的一回事他怎么办就是最可怜的就是例子都是50年就是在苏联就是发生的事情因为他们那时候就是决定就是苏联的政府就是他们决定就是压迫每一个宗教的方向所以那时候就是有很大的矛盾但是一般的情况下就是个就是心理的那个信徒他应该就是对国家的态度是比较积极的好的谢老教授我们看还有一些问题陆德中在大陆的现在的发展状况如何对如果是包括香港的话那当然有一个直接的一个就是发展这个发展就是我看是那个上次教会那个信教组织之内的一种发展我认识的就是地理教徒他们一般是就是中年级的上次一部分也是年轻的为什么他们还是算是就是跟就是新教就是跟那个基督教就是普通的就是那个教会有区别呢一般是因为他们在国外就是他们在德国或者在北欧生活过然后他们参加他们的然后他们参加他们的然后他们参加他们的就是本地的教会的就是那个活动所以他们会自己认为他们属于就是那个信义的一个教会要不然的话很多人他们就是所以那个经理会那个BaptistBaptist他们当然就是也有跟那个卢德众就是同样的方面但是在选个基督教现象之内那个卢德众是比较保守的一种就是一个教会一个教义因为那个教义一般是从改革天主教的那个原则就是而来的比如说那个梅兰西顿我开始的时候给你们看到他属于天主教改革的一种就是教内就是天主教内改革的一个就是一个学派卢德他差不多就是跟他们同意但是他就最不同的一方面就是那个钱就是他认为就是教会他就是他不允许就是让他的自己的那个教徒就是给比较就是很有钱的一个教皇就是更多钱所以从那个就是社会经济方面以来就是有一个比较就是神的就是普通的方面这个普通的方面就是在可以说是教会上政治性的方面不是神学上的方面那么中国的那个基督教也属于比较就是离天主教很远的就是组织可以说从60年代1960年代以来就是特别是北欧的就是还有德国北部的卢德教他们卢德宗他们开始慢就是跟所有的那个新教的教派就是开始就是联合起来美国仍然一直到现在就是没有那个趋势好的特别感谢我老汪教授我看到这里就想起我做的这个研究吗因为是研究警教的嘛你看我不知道就是说有没有可能有一种就是现代的这种宣教运动的发展可以给我的就是我警教的研究做一个参考您看我看到这个现在很多的宣教的中心都到了香港马来西亚台湾这地区因为我研究的是吐鲁番嘛所以会想到同样非常类似的情况对啊对他们从长安就推到了吐鲁番就是这样子就是可能找一个政治更加相对宽容的环境但我觉得您这个讲座一个最给我的一个非常大的一个启发是原来卢德宗跟北欧的这一群这个卢德宗的信徒有那么深远的联系然后北欧的这个像马丁路德的一些神学思想不只是神学思想包括一些他的社会啊神学啊政治上的借鉴对中国的近代社会都产生了深远的影响其实如果是从一个类比的角度来看的话就是完全是如果是看到唐代的警教的话有没有可能出现类似的情况但是我们现在唯一的一个大的缺乏是说对于唐代警教我们的资料实在是太少了我觉得卢德宗是有很多啊我们可以说是这样论断的如果对如果就是唐朝的传教士他们不是苏德人的话或者就是亚洲西部的人的话他们很可能是就是北欧的人因为北欧人的那个人格是比较怎么说呢就是他们不管生活就是生活情况舒不舒服他们很想他们一般就是很想就是把他们自己的那个工作就是或思想就是放在就是社会上就是格过的社会里面所以前也有就是北欧人就是去就是亚洲但是只是就是基督教之前所以因为基督教在天主教在北欧是比较是就是那个以前就是1000年以前的一回事所以对欧洲所有的地区来说是比较往期的一回事你看就是中国的那个天主教那个基督教到了就是几百年就是比北欧来说就是到了几百年以前所以他们还是很发达还有别的问题吗还有一个问题那个说路德宗的神学思想在今天中国教会神学思想中还有哪些表现好还是比较复杂的一个问题就是我看就是我最后就是给你们就是提到的就是有两种就是比较有矛盾的想法一个是就是那个当然是福利国家那个社会稳定的那个稳定的方面当然也是国家制度的一个问题所以他如果在那个三次就是基督教制度之内每一个教派比如说那个悉尼教像就是支持就是治理中国的国家的话那当然是个好事但是如果他们认为就是下一半就是那个自由方面如果他们那个国家就是影响到就是那个教派的自由的话那有的时候对就是个人那个信徒的个人信徒就是会有问题的所以我说是比较复杂的一个问题就是得看就是具体的情况就是每一个地方就是每一个教会具体的情况以后才能说就是怎么能解决的我们可以就是您可以就是寄给我一个电邮然后那个email然后我可以就是继续再就是给你我的看法好的还有一个问题问得比较专业后面有两本杂志ArgeminiMision这是德语吧我不太会读了你看这个呢是这个吗Argemini Misions at ShiftYeah还有New InternetMision at Shift这个是阿尼干的吗那个宣教还是什么这是德国柏林就是的一个宣教杂志对是传教杂志但是Mision at Shift就是传教学是那时候从那时候以来就是跟历史学和神学就是不太一样的一种那个学派在英国也会有但是德国就是影响到了就是因为那时候有一个多大部分是就是历史学就是理论学但是他不是学他不是写是神学就是theology如果是这样的话那以前也有学派但是这个这样的那个学派一直到1950 60年代会有然后就是他变成了那个历史类的一种那个学派因为什么因为现在就是没有就是一个非常强的那个传教那个传教现象现在就是布隆斯坦是那个卢德宗最重要的一方面他们还是在他们支持国外的就是教会特别是北欧的教会每个大城市之内就是基本上会有传教是还是有还是存在的但是他们经常就是在非洲也不一定是就是很就是也不一定是就是最近会有的就是也是比较古老的就是传教中心好还有最后一个问题他说现在三自两会在推动这个路德宗神学吗就是这个三自教会在推动路德宗神学吗我看还是存在特别在不知道就是香港的那个制度跟中国大陆的制度不一样我就是最近跟一个比较年轻的一个就是属于那个路德宗的就是学者就是讲话他说很可能就是再过50年以后就是大概没有那个区别了因为很多人就是他们在中国大陆他们还记得就是他们的祖先是被就是路德宗的传教士就是归心然后他们就自己认为是那个信律会但是很多人他们就是年轻人他们经常就是没有那个就是族派感觉他们自己认为是就是新教人或者那个基督教图不一定是那个路德宗的但是他们全部都可以学习那个路德就是马丁路德的那个神学文章因为他们并不是很复杂所以他们而且他对基督教的那个发展就是影响到了不少是的是这样的对好的我看是没有问题了感谢老曼教授的讲座如果大家以后有问题欢迎在我们的群里面聊天如果要问老曼教授呢我有机会可以跟老曼教授见面可以再亲自问一下然后把他的答案汇总过来然后我们这个讲座会在油管提供这个视频然后有时候也会提供这个最后整理出这个中文讲稿的内容如果大家有兴趣欢迎关注再次感谢大家来了解我们这个关于路德宗在中国的影响我相信这是一个非常好的讲座从历史学的角度呢希望这个讲座的内容能够一直传下去不要像警教一样大家以后警教对中国有多少影响我忘了忘得一干二净这个历史是很容易遗忘的这个因为我跟老师也是学历史方面的所以希望这个对大家有帮助对了解中国的历史有帮助好我们今天就讲到这里谢老曼教授谢大家非常感谢大家好的拜老曼教授拜拜再见拜再见"""
        segmented_output = segment_text(input_text)

        print("重写文字:\n", segmented_output)
        return (
            input_text,
            lm,
            segment_text,
            segmented_output,
            segmenter,
            signature,
        )
    return


if __name__ == "__main__":
    app.run()
