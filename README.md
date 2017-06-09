# 关于女性文胸尺码的深入探讨  

> 关爱女性健康，从我做起！  

## 概况  

心血来潮，想爬取天猫内衣的购买信息记录，来对中国广大女性的胸围情况来次认真地探讨。爬取内容为评论里的信息，包括尺码，颜色以及评价。习惯性打开开发者工具，果不其然，评论信息是动态生成的。所以就要到 network 去抓包，数据是 json 格式的。搞到评论的具体网址后分析下各参数，用 list 迭代岂不美滋滋？第一次迭代爬取 10w 条评论后用 set 去重后只剩下 1000 多条？？？ 经分析，它每隔几页评论就会弹出一个反爬虫连接验证登录，而且靠后一点，如 100 页后的数据显示的总是重复，经优化后一个商品差不多能爬到 4000 条不重复的评论。也可能是我技术还不到家吧，能力不够，努力来凑。我就爬取了不同的约 50 件商品的记录，得到了 20w 条评论信息（样本容量还是有点小，不过取样的范围广一点）。 

## 前言  

首先，得对内衣的尺码有所了解，为此我专门查了一下，在这里给对这个还不熟悉的男同胞们科普一下。  

**胸围分为上胸围和下胸围**  

如何测量下胸围尺码？  
水平围绕胸部乳房底部一周的长度，即为胸部下围尺寸，单位：CM  

如何测量上胸围方法？  
水平围绕胸部最高点（乳头）一周的长度，即为胸上围尺寸，如测量尺寸时遇到小数，测量时建议采用进一法，例如 72.1 公分，计算为 73 公分。  

还不知道怎么测量，看图 
 
![cup_ins_1](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_ins_1.png)  

如何计算罩杯的大小？  
罩杯的大小就是上胸围减去下胸围的差。根据步骤一测量的结果，用胸围尺寸 - 下胸围尺寸的差，即确定罩杯号型。对应罩杯参考。  

![cup_ins_2](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_ins_2.png)  

本来以为 A 已经够优秀了，没想到还有 AA 的，比优秀还优秀。加油，摸摸大！
接下来就是确定具体尺码了，尺码有两种，英式尺码和国际尺码。  

![cup_ins_3](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_ins_3.png)  

有了这些基本概念后，我们再来看看这具体的 20w 条数据  

## 颜色  

对颜色进行分词统计词频，清理数据后共有 136 个，对 top20 生成条形图  

![cup_color_bar](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_color_bar.png)  

**肤色 黑色 粉色** 在第一梯队，遥遥领先  
**灰色 白色 卡其色 紫色 蓝色 浅紫色 红色 贵族黑 浅蓝** 处于第二梯队，贵族黑和黑色有什么差别？黑得若隐若现？  
**薄杯，薄款，厚款，超薄** 按厚度来，厚款 > 薄款 > 薄杯 > 超薄 ？广大女性对薄款还是更多钟爱的，是因为现在夏天薄的比较凉爽吗？还是薄的性感一点？ 

具体 top60 
```
肤色, 67861
黑色, 48686
粉色, 15788
钢圈, 14846
薄款, 11928
薄杯, 9874
单件, 7109
灰色, 6486
白色, 6345
套装, 6228
卡其色, 5745
紫色, 5540
蓝色, 5333
厚款, 5126
浅紫色, 4336
红色, 4322
贵族黑, 4285
拉丝, 3793
浅蓝, 3667
超薄, 3627
下厚, 3459
上薄, 3459
绑带, 3236
酒红, 3215
肤嫩色, 2804
三排, 2543
亮面, 2403
纯色, 2205
轻肤, 2189
蕾丝, 2102
银灰色, 1979
藕荷色, 1802
玫红, 1781
宝蓝色, 1681
纯洁, 1659
全光肤, 1642
银灰, 1636
咖啡色, 1587
光面, 1548
段染, 1547
虾粉, 1546
水晶, 1371
亚光版, 1262
藏青, 1211
轻粉, 1185
绿色, 1113
浅绿色, 1074
粉红色, 1056
全光, 1053
金肤色, 1006
豆沙, 870
典雅, 788
果绿, 722
冰沙粉, 699
紫颜色, 678
经典, 649
蓝边, 643
奶白色, 621
浅粉, 563
薄荷绿, 556
```  
才知道原来颜色可以有这么多种...  
**土豪金 静谧蓝 个性黑** 挺别致的，**蕾丝** 好像也深受喜爱  

最后来个词云  

![cup_wordcloud](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_wordcloud.jpg)  

## 尺码  

这 20w 条数据中，下胸围范围为 [ 70cm - 90cm ]，罩杯范围为 [ A - E ]  

先来看看总体的胸围情况  

![cup_down_all_line](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_down_all_line.png)  

总体上呈现先升后降的趋势，以 75cm 为分界点开始下滑，总体范围还是在 70cm - 85cm， 95cm 的基本上已经很少了，一是可能爬取的内衣商品里面有的没卖 95cm 的，二是这胸围的本来就少...   

下胸围对应的总体比例  

![cup_down_all_pie](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_down_all_pie.png)  

再来看看总体的罩杯情况  

![cup_size_all_line](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_size_all_line.png)  

也是先升后降的趋势，这个是以 B 罩杯为分界点开始下滑，但是这个滑得明显比较陡峭一点，E 罩杯 只有可怜的 155。哎！现实太骨感了，还是理想丰满一点。  

罩杯对应的总体比例  

![cup_size_all_pie](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_size_all_pie.png)  

看完总体看具体  

以罩杯为横坐标，绘制出各胸围对应的罩杯情况  

![cup_size_line](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_size_line.png)  

基本上都是先升后降，75cm 80cm 85cm 的是以 B 罩杯为分界点变换趋势，只有 70cm 的是一路向下滑。90cm 和 95cm 由于量不足，在这个图里基本上已经贴着 X 轴了，把这两个单独拉出来看看  

![cup_90_95](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_90_95.png)  

这下就明显很多了，这两个是以 C 罩杯为分界点变换趋势的，因为毕竟胸围大，罩杯大的几率会大一点。值得注意的是，95cm 是没有 A 罩杯和 E 罩杯的。95cm 的胸围 A 的罩杯，这太可怜了吧..., 95cm 的胸围 E 的罩杯，那也是强得不敢想象。  

以胸围为横坐标，绘制出各罩杯对应的胸围情况  

![size_cup_line](https://github.com/chenjiandongx/cup-size/blob/master/images/size_cup_line.png)  

这个的趋势就比较有趣了，A 罩杯和 B 罩杯以 75cm 为分界点，开始下降，A 罩杯降得比 B 罩杯稍微平缓一点，C 罩杯的波动就平缓很多，可能也是总体的量偏少，加上图表比例的关系。至于 D 罩杯和 E 罩杯，还是贴地了，我也把它俩单独拉出来。  

![cup_DE](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_DE.png)

可以看到 D 罩杯是呈现梯状的，E 罩杯由于量实在少，基本上毫无波动。  

### 再详细看看数据集中的范围吧  

胸围范围为 [ 70cm - 85cm ]，罩杯范围为 [ A - C ]  
其对应的比例分别为 

70cm 的情况，**A > B > C**  

![cup_70](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_70.png)  

75cm 的情况，**B > A > C**  

![cup_75](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_75.png)   

80cm 的情况，**B > A > C**  

![cup_80](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_80.png)  

85cm 的情况，**B > C > A**   

![cup_85](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_85.png)   

70cm 的小胸围罩杯比例 A > B > C，小胸围的本身应该就是偏瘦，瘦的话罩杯也是偏小。 75cm 和 80cm 的 B 罩杯的比例都要稍大于 A 罩杯的。85cm 的 C 罩杯已经反超于 A 罩杯了，毕竟胸围大，罩杯也不会小到哪里去  

## 评价  

一样的套路，分词然后统计词频，进行数据的清理。其中有 42321 条评论用户是没有填写评论的，这个不进行处理。  
由于评价没有统一规范，这个统计出来的词就多了去了。由 top20 生成条形图  

![cup_comment_bar](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_comment_bar.png)  

**舒服 不错 喜欢 满意 可以 好评 合适** 这些都是不错的评价，**聚拢** ？显得大一点吗？  

展示一下 top60 
```
 舒服, 39425
 不错, 38335
 质量, 27383
 喜欢, 21841
 穿着, 19816
 内衣, 18281
 宝贝, 17377
 非常, 16812
 聚拢, 14919
 收到, 14881
 满意, 14558
 效果, 12684
 可以, 11989
 好评, 11520
 合适, 10705
 购买, 10254
 没有, 9114
 就是, 8807
 有点, 8658
 特别, 8455
 真的, 8105
 感觉, 7927
 小, 7347
 颜色, 6945
 下次, 6876
 这个, 6557
 物流, 6517
 起来, 6279
 好看, 6250
 还会, 5864
 夏天, 5585
 以后, 5472
 值得, 5457
 尺码, 5453
 第二次, 5415
 价格, 5378
 舒适, 5369
 不会, 5169
 还是, 5080
 而且, 5052
 适合, 5041
 卖家, 4964
 一样, 4834
 钢圈, 4756
 东西, 4711
 客服, 4696
 一下, 4638
 大小, 4591
 面料, 4531
 试穿, 4476
 挺舒服, 4468
 推荐, 4383
 很快, 4037
 便宜, 3996
 一次, 3843
 但是, 3717
 已经, 3714
 超级, 3692
 衣服, 3621
 一个, 3476
```
第二次都出现了 5415 次，看来是回头客了。来看一下没有排上 top60 的其他词，来个有趣一点的。
```
哈哈, 989
哈哈哈, 554
哈, 318
哈哈哈哈, 170
```  
所以，哈多少个是看心情决定的吗？  
```
便宜, 3996
实惠, 3216
方便, 1708
性价比, 1662
```
货比三家，上网买东西图的就是一个方便和便宜。  
其他的就不再详细分析了，还是老规矩，上个评价的词云。  

![comment_woldcloud](https://github.com/chenjiandongx/cup-size/blob/master/images/comment_woldcloud.jpg)  

## 最后

看我用散点图画出一个内衣  

![cup_red](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_red.png)  

什么？不喜欢这火辣的红色，那来个性感的黑色。  

![cup_black](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_black.png)  

用散点图表白也不是说不行，诺！  

![cup_love](https://github.com/chenjiandongx/cup-size/blob/master/images/cup_love.png)  

最后一张图引用我心目中永远的大神 Linus 的一句话  

![talk_is_cheap](https://github.com/chenjiandongx/cup-size/blob/master/images/talk_is_cheap.png)
