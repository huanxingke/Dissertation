## 污染物落地浓度计算

### 1.影响污染物在大气中扩散的因素

#### 1.1气象的动力因子

##### 1.1.1风

###### 1.1.1.1风向

- 在气象上，把空气的铅直运动称为升降气流，空气的水平运动称为风。风具有方向（指风的来向）和大小。
- 风向表示：
- - 方位表示法：一般把圆周均分为16个方位，两相邻风向方位夹角为22.5°。
  - 角度表示法：以正北为0°，将圆周分为360°，角度顺时针增加，东为90°，南为180°，西为270°，以此作为确定风向的标准。

###### 1.1.1.2风速

- 地表附近的气流运动受下垫面（地表面的树林、田野、建筑物等）摩擦力的阻滞，使气流在垂直方向上产生了风速梯度。表示风速随高度变化的曲线称为“风速廓线”。随着地面粗糙度增加，风速梯度减少。目前常用的两种风速廓线模式是：

**（1）对数率**：
$$
\overline{u}=\frac{u^{•}}{k}ln{\frac{z}{z_{0}}}\tag{1-1}
$$

- $\overline{u}$：高度为$z$处风速，m/s。
- $u^{•}$：摩擦速度，m/s。
- $k$：卡门常数，一般取：$k=0.4$。
- $z$：高度，m。
- $z_{0}$：地面粗糙度，m，有代表性的地面粗糙度：
- 
<table>
	<tr>
		<th colspan=3 style="text-align:center">表1-1 有代表性的地面粗糙度</th>
	</tr>
	<tr>
		<th style="text-align:center">地面类型</th>
		<th style="text-align:center">z<sub>0</sub>/cm</th>
		<th style="text-align:center">有代表性的z<sub>0</sub>/cm</th>
	</tr>
	<tr>
		<td style="text-align:center">草原</td>
		<td style="text-align:center">1~10</td>
		<td style="text-align:center">3</td>
	</tr>
	<tr>
		<td style="text-align:center">农作物地区</td>
		<td style="text-align:center">10~30</td>
		<td style="text-align:center">10</td>
	</tr>
	<tr>
		<td style="text-align:center">村落、分散的树林</td>
		<td style="text-align:center">20~100</td>
		<td style="text-align:center">30</td>
	</tr>
	<tr>
		<td style="text-align:center">分散的大楼（城市）</td>
		<td style="text-align:center">100~400</td>
		<td style="text-align:center">100</td>
	</tr>
	<tr>
		<td style="text-align:center">密集的大楼（大城市）</td>
		<td style="text-align:center">&gt;400</td>
		<td style="text-align:center">&gt;300</td>
	</tr>   
</table>


**（2）指数率**：
$$
\overline{u}=u_{10}\bigg(\frac{z}{10}\bigg)^m\tag{1-2}
$$

- $\overline{u}$：高度为$z$处风速，m/s。
- $u_{10}$：高度10m处的平均风速，m/s。
- $m$：常数，与大气稳定度、地形有关，一般实验确定，无实测值时，在150m高度以下按下表选取，在150m高度以上取150m处的风速。

<table>
	<tr>
		<th colspan=6 style="text-align:center">表1-2 指数m的值</th>
	</tr>
	<tr>
		<th style="text-align:center">稳定级别</th>
		<th style="text-align:center">A</th>
		<th style="text-align:center">B</th>
		<th style="text-align:center">C</th>
		<th style="text-align:center">D</th>
		<th style="text-align:center">E,F</th>
	</tr>
	<tr>
		<td style="text-align:center">m</td>
		<td style="text-align:center">0.10</td>
		<td style="text-align:center">0.15</td>
		<td style="text-align:center">0.20</td>
		<td style="text-align:center">0.25</td>
		<td style="text-align:center">0.30</td>        
	</tr> 
</table>

###### 1.1.1.3风对污染物浓度分布的影响

- 整体输送，因而污染区总是在污染源的下风向。
- 冲淡稀释，因此污染物浓度总是与风速大小成反比。

##### 1.1.2湍流

- **定义**：在摩擦层中，风速时快时慢，风向也忽上忽下、忽左忽右不断变化，风的这种阵性和摆动称为大气的湍流。
- **近地层大气湍流形式**：
- - 由机械力产生的机械湍流，如空气与地面相对运动引起的地面风的切变、空气流经障碍物（山丘、树木、建筑物）而引起风向和风速的突然改变等，这些都会引起机械湍流。
  - 由热力产生的热力湍流，主要是由于大气层结不稳定而导致空气垂直运动。
  - 一般情况下，大气湍流的强弱既取决于机械因素，又取决于热力因素，是两者综合作用的结果。

- **大气污染物的扩散，主要靠大气湍流的作用**：
- - 可以想像，如果大气只是"层流”流动，而没有湍流运动，从烟囱排出的废气向下风向漂移时，就应像一条“烟管”那样保持着相同的粗细。
  - 然而实际并非如此，因为烟云向下风漂移时，除其本身的分子扩散外，还受大气湍流作用，从而使得烟团周界逐渐扩张。
- **空气污染的稀释是大气湍流和分子扩散的直接结果**。湍流扩散的速率要比分子扩散的速率快10°~10°倍，以至分子扩散效应在大气扩散问题中可忽略不计。

##### 1.1.3局地风

###### 1.1.3.1海陆风

- 当海风吹到陆上时，造成冷的海洋空气在下，暖的陆地空气在上，形成逆温，使沿海排放污染物向下游冲去而造成短时间的污染。
- 海陆风对大气污染的另一作用是循环污染，特别是海风和陆风转变时，原来被陆风带去的污染物会被海风带回原地形成重复污染。

###### 1.1.3.2山谷风

- 根据地形条件及时间，山谷风的污染可出现以下几种情况：①山风和谷风转换期的污染；②山谷中热力环流引起的漫烟；③侧向封闭山谷引起的高浓度污染；④下坡风气层中的污染。
- 另外，山区迎风面和背风面所受的污染也不相同。污染源在山前上风侧时，对迎风坡会造成高浓度的污染。在山后则会出现以下几种情况：①污染源在山的上风侧，并有一段距离，则烟流可能随风越过山头，被下沉气流带到地面，从而造成严重污染；②污染源在山后，正好处在过山气流的下沉气流中，烟流抬升不高，很快落到地面而造成污染；③污染源在山后的回流区，烟流不能扩散出去而导致污染。
- 四周高、中间低的地区，如果周围没有明显的出口，则在静风而有逆温时，很容易造成高浓度的污染。

###### 1.1.3.3城市热岛效应

- 工业的发展，人口的集中，使城市热源和地面覆盖与郊区形成显著的差异，从而导致城市比周围地区热的现象，称为城市热岛效应。由于城市温度经常比农村高（特别是夜间），气压较低，在晴朗平衡的天气下可以形成一种从周围农村吹向城市的特殊局地风，称为城市风。
- 这种风在市区内辐合产生上升气流，周围地区的风则向城市中心汇合，使城市工业区的污染物在夜晚向城中心输送，特别当上空有逆温层阻挡时，污染更为严重。

#### 1.2气象的热力因子

##### 1.2.1大气温度层结

- 如前所述，污染物在大气中的扩散主要受湍流的影响，而大气湍流在很大程度上取决于近地层的垂直温度分布。由于测量大气湍流比测量相应的垂直温度分布要困难得多，所以常常用后者作为评价大气湍流的指标。这种气温随高度的分布通常称为大气层结。

###### 1.2.1.1干绝热递减率

- 空气团在大气中的升降过程可以看作绝热过程，因为它与周围的热量交换很小，可以忽略。当一个干空气团在大气中绝热上升时，因周围气压降低而膨胀，部分内能用于反抗外界压力而做膨胀功，温度下降；反之，气团绝热下降时，温度将升高。

- 干空气团或未饱和的湿空气团绝热上升或下降单位高度（通常取100m）时温度降低或升高的数值称为干绝热递减率，以$\gamma_{d}$表示，定义为：

$$
\gamma_{d}=-\bigg(\frac{dT_{i}}{dz}\bigg)_{d}\tag{1-4}
$$

- 下标$i$和$d$分别代表气团和干空气或未饱和湿空气，理论上：

$$
\gamma_{d}\approx\frac{g}{C_{p}}
$$

- $C_{p}$：干空气的比定压热容，$C_{p}=1.004J/(kg{\cdot}K)$。
- $g$：重力加速度，$g=9.81m/s^2$。
- 则：$\gamma_{d}=0.98K/(100m)$。

###### 1.2.1.2气温递减率

- 大气环境中，气温随高度的变化称为气温递减率，以$\gamma$表示：

$$
\gamma=-\bigg(\frac{dT}{dz}\bigg)_{环境}\tag{1-5}
$$



- 可见$\gamma_d$和$\gamma$是两个不同的概念：$\gamma_d$是对气块而言，$\gamma$则是对周围空气而言；$\gamma_d=0.98K/(100m)$，是一个常数，而$\gamma$可正可负，可大可小，不是常数。

###### 1.2.1.3气温的垂直分布

- 污染物的迁移、扩散和转化主要发生在离地10km以内的对流层。在对流层中，气温一般随高度的增加而降低，整个对流层的气温垂直递减率平均为$0.65℃/(100m)$。实际上，各高度的气温垂直递减率是因时、因地而不同的。气温的垂直分布也可用坐标曲线来表示，称为温度层结曲线，简称温度层结。
- 大气中的温度层结有四种类型：
- - $\gamma>\gamma_d$，称为递减或超绝热。
  - $\gamma=\gamma_d$，称为中性。
  - $\gamma=0$，称为等温。
  - $\gamma<0$，称为气温逆转，简称逆温。

##### 1.2.2逆温

- 如上所述，$\gamma<0$的大气层结称为逆温。由于逆温层内气温随高度的增加而增加，它将阻碍气团的上升运动，所以逆温层又称阻挡层。污染的空气不能穿过逆温层，而只能在它的下面扩散，因此可能造成高浓度的污染。大多数空气污染事件就发生在有逆温及静风的条件下，故对逆温层必须高度重视。
- 逆温层可分为接地逆温层和上部逆温层。逆温层的下限称为逆温高度，上、下限的高度差称为逆温层厚度，上、下限的温度差称为逆温强度。

![逆温层的类型](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\逆温层的类型.png)

- 形成逆温层的原因：

###### 1.2.2.1辐射逆温

- 辐射逆温是由于地面辐射冷却而形成的，大陆常年可见，以冬季最强。晴朗或少云、风不大的夜间，地面强烈的辐射损失使地表很快冷却，近地层大气随之自下而上变冷，下面降温多，上面降温少，因而形成自地面开始的接地逆温层。
- - 辐射逆温一般从日落前开始形成。
  - 到黎明时逆温层最厚，强度最大。
  - 日出后，地面开始增热，近地层大气自下而上被加热，逆温自下而上逐渐消失。
  - 上午9：00—10：00逆温层全部消失。

![辐射逆温](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\辐射逆温.png)

###### 1.2.2.2下沉逆温

- 当高空高压区内某一气层发生下沉运动时，因气压逐渐增大以及气层向水平方向辐散，其厚度减小（h'<h）。这样气层顶部比底部下沉的距离要大（H>H'），因而顶部绝热增温比底部多而形成逆温。
- 下沉逆温的形成与昼夜没有关系，持续时间长，范围宽，逆温层厚度也较大，离地面数百米的高空都可能出现。特别是冬季，下沉逆温与辐射逆温结合在一起，形成很厚的逆温层，对高架污染源排放影响很大。

![下沉逆温](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\下沉逆温.png)

###### 1.2.2.3湍流逆温

- 湍流逆温是低层空气湍流混合形成的逆温。
- 图中AB为原来的气温分布，气温递减率$\gamma>\gamma_d$。
- 低层空气经过湍流混合后，气层的温度分布逐渐接近于$\gamma_d$。这是因为湍流运动中，上升空气的温度是按干绝热递减变化的，空气上升到混合层上部时，它的温度比周围空气温度低，混合的结果，使上层空气降温；空气下沉时，情况相反，会使下层空气增温。所以经过充分地湍流混合以后，气层的温度递减率逐渐趋于$\gamma_d$，如图中 CD所示。
- 这样在湍流混合层与未发生湍流的上层空气之间的过渡层就出现了逆温层DE。这种逆温层厚度不大，约几十米。

![湍流逆温](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\湍流逆温.png)

###### 1.2.2.4锋面逆温

- 对流层中的冷、暖空气相遇时，暖空气密度小，就会爬到冷空气的上面，形成一个倾斜的过渡区，即锋面。如果锋面处冷、暖空气温度差很大，即可在冷空气一边形成逆温，如图8-16（a）所示。
- 如在白天，大范围的盛行风和海风方向相反，低温的海风在下，陆风暖气流在上，前沿形成锋面，出现一层锋面逆温，如图8-16（b）所示。沿岸低矮的烟流随下层海风吹向内陆，它的上部受逆温顶盖的限制，可形成较高的地面浓度。



![锋面逆温](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\锋面逆温.png)

##### 1.2.3大气稳定度

- 如果一团空气受到对流冲击力的作用，产生了向上或向下的运动，这以后就可能出现三种情况：
- - 当外力撤销后，该气团逐渐减速，并且有返回原来高度的趋势，则说明大气是稳定的。
  - 当外力撤销后，该气团仍加速升降，则说明此时大气是不稳定的。
  - 当外力去除后，气团既不加速，也不减速，则此时大气处于中性平衡状态。

- 大气稳定度是大气对污染源排人其中的污染物扩散能力的一种量度。大气愈不稳定，污染物在大气中的扩散速率就愈快。

###### 1.2.3.1 大气稳定度的判别

- 大气稳定度是取决于气温垂直递减率（$\gamma$）与干绝热递率（$\gamma_d$）的对比。根据气团在大气中的受力分析和气体状态方程，可以导出单位体积的气团产生的加速度（$a$）为：

$$
a=g\bigg(\frac{\gamma-\gamma_d}{T}\bigg)\Delta{z}\tag{1-6}
$$

- $\Delta{z}$：气团在垂直方向上的位移，m。
- 由上式可以看出，（$\gamma=\gamma_d$）的符号决定了气团加速度（$a$）与其位移（$\Delta{z}$）的方向是否一致，也就决定了大气是否稳定：

- - $\gamma<\gamma_d$，若$\Delta{z}>0$，则$a<0$，开始的运动将受到抑制，层结是稳定的。
  - 当$\gamma>\gamma_d$时，若$\Delta{z}>0$，则$a>0$，开始的运动将加速进行，层结是不稳定的。
  - 当$\gamma=\gamma_d$时，$a=0$，层结是中性的。

###### 1.2.3.2大气稳定度与烟流扩散的关系

- 波浪型：$\gamma>0$，$\gamma>\gamma_d$，大气处于很不稳定的状况。此时对流强烈，排入大气的烟云上下左右波动翻腾，沿主导风向流动扩散很快，形成波浪型。污染物着地很少，只有不够高的烟囱才有一定污染物可能在离烟囱不远处与地面接触。这种烟型多发生在夏季或其他季节的晴天中午或午后。

- 锥型：$\gamma>0$，$\gamma\approx\gamma_d$，大气处于中性或稳定状态。烟气沿主导风向扩散、兼有上下左右扩散。扩散速度比波浪型慢，烟形沿风向愈扩愈大，形成锥型。这种烟型多发生在阴天中午或冬季夜间。

- 扇型：$\gamma<0$，$\gamma<\gamma_d$，温度逆增，大气处于稳定状态。烟气几乎无上下流动，而沿两侧扩散，从高处下望，烟气呈扇形散开。这种烟气可传送到很远的地方，若遇到山地、丘陵或高层建筑物，则可发生下沉作用，在该地造成严重污染，此现象多发生在晴天的夜间或早晨。

- 屋脊型：大气向逆温过渡，在排出口上方，$\gamma>0$，$\gamma>\gamma_d$，大气处于不稳定状态；在排出口下方，$\gamma<0$，$\gamma<\gamma_d$，大气处于稳定状态。因此，烟气不向下扩散，只向上扩散，呈屋脊型。尾气流的下部浓度大，如不与建筑物或丘陵相遇，不会造成对地面的严重污染。

- 熏烟型：大气逆温向不稳定过渡时，排出口上方，$\gamma<0$，$\gamma<\gamma_d$，大气处于稳定状态；排出口下方，大气处于不稳定状态。清晨太阳出来后，逆温开始消散，当不稳定大气发展到烟流的下缘，而上部大气仍然处于稳定状态时，就发生重烟状态。这时，好像在烟流上面有一个“锅盖”，阻止烟气向上扩散，烟气大量下沉，在下风地面上造成比其他烟型严重得多的污染，许多烟雾事件都是在此条件下形成的。熏烟型烟雾多发生在冬季日出前后。

![大气稳定度和烟型](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\大气稳定度和烟型.png)

##### 1.2.4大气稳定度的分类

- 大气稳定度的分类方法很多，这里仅介绍国标GB3840—83推荐的**修订帕斯奎尔法**。它是将距地面10m高处的风速和辐射状况（云量、云状和日照）作为划分大气稳定度等级的指标，把大气稳定度分为六级，即A（极不稳定）、B（不稳定）、C（弱不稳定）、D（中性）、E（稳定）、F（极稳定），详见表1-3。表1-3中的太阳辐射等级可由表1-4查得。

<table>
	<tr>
		<th colspan=7 style="text-align:center">表1-3 大气稳定度等级</th>
	</tr>
	<tr>
		<th rowspan=2 style="text-align:center">地面风速/(m/s)</th>
		<th colspan=6 style="text-align:center">太阳辐射等级</th>
	</tr>
	<tr>
		<th style="text-align:center">+3</th>
		<th style="text-align:center">+2</th>
		<th style="text-align:center">+1</th>
		<th style="text-align:center">0</th>
		<th style="text-align:center">-1</th>
		<th style="text-align:center">-2</th>
	</tr>
	<tr>
		<td style="text-align:center">≤1.9</td>
		<td style="text-align:center">A~B</td>
		<td style="text-align:center">A~B</td>
		<td style="text-align:center">B</td>
		<td style="text-align:center">D</td>
		<td style="text-align:center">E</td>
		<td style="text-align:center">F</td>        
	</tr>
	<tr>
		<td style="text-align:center">2~2.9</td>
		<td style="text-align:center">B</td>
		<td style="text-align:center">B</td>
		<td style="text-align:center">C</td>
		<td style="text-align:center">D</td>
		<td style="text-align:center">E</td>
		<td style="text-align:center">F</td>        
	</tr>
	<tr>
		<td style="text-align:center">3~4.9</td>
		<td style="text-align:center">C</td>
		<td style="text-align:center">B~C</td>
		<td style="text-align:center">C</td>
		<td style="text-align:center">D</td>
		<td style="text-align:center">D</td>
		<td style="text-align:center">E</td>        
	</tr>
	<tr>
		<td style="text-align:center">5~5.9</td>
		<td style="text-align:center">C</td>
		<td style="text-align:center">D</td>
		<td style="text-align:center">D</td>
		<td style="text-align:center">D</td>
		<td style="text-align:center">D</td>
		<td style="text-align:center">D</td>        
	</tr>
	<tr>
		<td style="text-align:center">≥6</td>
		<td style="text-align:center">C</td>
		<td style="text-align:center">D</td>
		<td style="text-align:center">D</td>
		<td style="text-align:center">D</td>
		<td style="text-align:center">D</td>
		<td style="text-align:center">D</td>        
	</tr>    
</table>

<table>
	<tr>
		<th colspan=7 style="text-align:center">表1-4 太阳辐射等级</th>
	</tr>
	<tr>
		<th colspan=2 style="text-align:center">云量</th>
		<th colspan=5 style="text-align:center">太阳高度角</th>
	</tr>
	<tr>
		<th style="text-align:center">总云量</th>
		<th style="text-align:center">低云量</th>
		<th style="text-align:center">夜间</th>
		<th style="text-align:center">h<sub>0</sub>≤15<sup>o</sup></th>
		<th style="text-align:center">15<sup>o</sup>&lt;h<sub>0</sub>≤35<sup>o</sup></th>
		<th style="text-align:center">35<sup>o</sup>&lt;h<sub>0</sub>≤65<sup>o</sup></th>
		<th style="text-align:center">h<sub>0</sub>>65<sup>o</sup></th>
	</tr>
	<tr>
		<td style="text-align:center">≤4</td>
		<td style="text-align:center">≤4</td>
		<td style="text-align:center">-2</td>
		<td style="text-align:center">-1</td>
		<td style="text-align:center">+1</td>
		<td style="text-align:center">+2</td>
		<td style="text-align:center">+3</td>        
	</tr>
	<tr>
		<td style="text-align:center">5~7</td>
		<td style="text-align:center">≤4</td>
		<td style="text-align:center">-1</td>
		<td style="text-align:center">0</td>
		<td style="text-align:center">+1</td>
		<td style="text-align:center">+2</td>
		<td style="text-align:center">+3</td>        
	</tr>
	<tr>
		<td style="text-align:center">≥8</td>
		<td style="text-align:center">≤4</td>
		<td style="text-align:center">-1</td>
		<td style="text-align:center">0</td>
		<td style="text-align:center">0</td>
		<td style="text-align:center">+1</td>
		<td style="text-align:center">+1</td>        
	</tr>
	<tr>
		<td style="text-align:center">≥5</td>
		<td style="text-align:center">5~7</td>
		<td style="text-align:center">0</td>
		<td style="text-align:center">0</td>
		<td style="text-align:center">0</td>
		<td style="text-align:center">0</td>
		<td style="text-align:center">+1</td>        
	</tr>
	<tr>
		<td style="text-align:center">≥8</td>
		<td style="text-align:center">≥8</td>
		<td style="text-align:center">0</td>
		<td style="text-align:center">0</td>
		<td style="text-align:center">0</td>
		<td style="text-align:center">0</td>
		<td style="text-align:center">0</td>        
	</tr>
</table>

- 表1-4中的太阳高度角（$h_{0}$）由下式求得：

$$
h_{0}=arcsin[{sin\varphi}{sin\theta}+{cos\varphi}{cos\theta}{cos(15t+\lambda-300)}]\tag{1-7}
$$

- $\varphi$：当地地理纬度，$^o$。
- $\lambda$：当地地理经度，$^o$。
- $\theta$：太阳倾角，$^o$：
- - 可按当时月份与日期由表1-5查取。
  - 也可按下式计算：

$$
\theta=[0.006918-0.399912cos\delta_0+0.070257sin\delta_0-\\0.006758cos2\delta_0+0.0009079sin2\delta_0-\\0.002697cos3\delta_0+0.001480sin3\delta_0]{\times}180/\pi\tag{1-8}
$$

- - $\theta$：太阳倾角，$^o$。
  - $\delta_0=360d_n/365$，$^o$。
  - $d_n$：一年中的日期序数，$1,2,...,365$。

- $t$：观测进行时的北京时间，$h$。


<table>
	<tr>
		<th colspan=9 style="text-align:center">表1-5 太阳倾角θ概略值</th>
	</tr>
	<tr>
		<th style="text-align:center">月</th>
		<th style="text-align:center">旬</th>
		<th style="text-align:center">倾角/<sup>o</sup></th>
		<th style="text-align:center">月</th>
		<th style="text-align:center">旬</th>
		<th style="text-align:center">倾角/<sup>o</sup></th>
		<th style="text-align:center">月</th>
		<th style="text-align:center">旬</th>
		<th style="text-align:center">倾角/<sup>o</sup></th>
	</tr>
	<tr>
		<td rowspan=3 style="text-align:center">1</td>
		<td style="text-align:center">上</td>
		<td style="text-align:center">-22</td>
		<td rowspan=3 style="text-align:center">5</td>
		<td style="text-align:center">上</td>
		<td style="text-align:center">+17</td>
		<td rowspan=3 style="text-align:center">9</td>
		<td style="text-align:center">上</td>
		<td style="text-align:center">+7</td>	
	</tr>
	<tr>
		<td style="text-align:center">中</td>
		<td style="text-align:center">-21</td>
		<td style="text-align:center">中</td>
		<td style="text-align:center">+19</td>
		<td style="text-align:center">中</td>
		<td style="text-align:center">+3</td>	
	</tr>
	<tr>
		<td style="text-align:center">下</td>
		<td style="text-align:center">-19</td>
		<td style="text-align:center">下</td>
		<td style="text-align:center">+21</td>
		<td style="text-align:center">下</td>
		<td style="text-align:center">-1</td>	
	</tr>
	<tr>
		<td rowspan=3 style="text-align:center">2</td>
		<td style="text-align:center">上</td>
		<td style="text-align:center">-15</td>
		<td rowspan=3 style="text-align:center">6</td>
		<td style="text-align:center">上</td>
		<td style="text-align:center">+22</td>
		<td rowspan=3 style="text-align:center">10</td>
		<td style="text-align:center">上</td>
		<td style="text-align:center">-5</td>	
	</tr>
	<tr>
		<td style="text-align:center">中</td>
		<td style="text-align:center">-12</td>
		<td style="text-align:center">中</td>
		<td style="text-align:center">+23</td>
		<td style="text-align:center">中</td>
		<td style="text-align:center">-8</td>	
	</tr>
	<tr>
		<td style="text-align:center">下</td>
		<td style="text-align:center">-9</td>
		<td style="text-align:center">下</td>
		<td style="text-align:center">+23</td>
		<td style="text-align:center">下</td>
		<td style="text-align:center">-12</td>	
	</tr>
	<tr>
		<td rowspan=3 style="text-align:center">3</td>
		<td style="text-align:center">上</td>
		<td style="text-align:center">-5</td>
		<td rowspan=3 style="text-align:center">7</td>
		<td style="text-align:center">上</td>
		<td style="text-align:center">+22</td>
		<td rowspan=3 style="text-align:center">11</td>
		<td style="text-align:center">上</td>
		<td style="text-align:center">-15</td>	
	</tr>
	<tr>
		<td style="text-align:center">中</td>
		<td style="text-align:center">-2</td>
		<td style="text-align:center">中</td>
		<td style="text-align:center">+21</td>
		<td style="text-align:center">中</td>
		<td style="text-align:center">-18</td>	
	</tr>
	<tr>
		<td style="text-align:center">下</td>
		<td style="text-align:center">+2</td>
		<td style="text-align:center">下</td>
		<td style="text-align:center">+19</td>
		<td style="text-align:center">下</td>
		<td style="text-align:center">-21</td>	
	</tr>
	<tr>
		<td rowspan=3 style="text-align:center">4</td>
		<td style="text-align:center">上</td>
		<td style="text-align:center">+6</td>
		<td rowspan=3 style="text-align:center">8</td>
		<td style="text-align:center">上</td>
		<td style="text-align:center">+17</td>
		<td rowspan=3 style="text-align:center">12</td>
		<td style="text-align:center">上</td>
		<td style="text-align:center">-22</td>	
	</tr>
	<tr>
		<td style="text-align:center">中</td>
		<td style="text-align:center">+10</td>
		<td style="text-align:center">中</td>
		<td style="text-align:center">+14</td>
		<td style="text-align:center">中</td>
		<td style="text-align:center">-23</td>	
	</tr>
	<tr>
		<td style="text-align:center">下</td>
		<td style="text-align:center">+13</td>
		<td style="text-align:center">下</td>
		<td style="text-align:center">+11</td>
		<td style="text-align:center">下</td>
		<td style="text-align:center">-23</td>	
	</tr>	
</table>	
- 确定大气稳定度等级的步骤：
- - 先根据日期由表1-5中查取太阳倾角$\theta$，计算太阳高度角（$h_o$）。
  - 由太阳高度角$h_o$及云量按表1-4查出辐射等级。
  - 再由辐射等级与地面风速按表1-3查出稳定度等级。

- 云：
- - 云分为高云（5000 m 以上）、中云（2500~5000m）和低云（2500m以下）三类。
  - 云量是指云遮蔽天空的成数。我国将可见天空分为10等份，云遮盖了几分，云量就是几。如碧空无云，云量为零；阴天云量为10。
  - 总云量是指所有云遮蔽天空的成数，不考虑云的层次和高度。
  - 低云量是指低云遮蔽天空的成数。
  - 我国对云量的记录采取分数的形式，以总云量为分子，低云量为分母，如10/7，5/2等，任何时候低云量不得大于总云量。
  - 云量可从气象台、气象站取得，也可以自行观测。

### 2.烟气抬升高度

#### 2.1烟气抬升高度及其影响因素

- 通过烟囱排出的烟气通常都具有一定的速度和温度。在动力及浮力作用下，烟气在离开烟囱口以后，仍然要向上冲出一定的高度，然后再沿风的方向扩散。
- 烟气在水平方向的扩散称为烟羽。烟羽轴线与烟囱口间的距离称为烟羽抬升高度$\Delta{H}$。烟气所达到的高度称为有效源高，因此，有效源高度$H$（m）等于烟囱实体高度$H_{s}$（m）与烟气抬升高度$\Delta{H}$（m）之和，即：

$$
H=H_s+\Delta{H}\tag{2-1}
$$

- 对于一般的烟囱，$H_{s}$为一定值。因此，只要计算出$\Delta{H}$，有效源高就可随之而定。

- 影响烟气抬升和扩散的因素主要是排放因素、气象因素及下垫面状况：
- - 排放因素：烟流喷速和烟气温度。
  - 气象因素：平均风速（$\overline{u}$）、湍流强度、环境空气温度、大气稳定度以及逆温层等。
  - 下垫面状况：主要是指地形及建筑物构型。

- 图8-19（a）：烟流喷出速度愈快或烟气温度与周围空气温度之差越大，在中低风速下，烟气抬升高度越大。
- 图8-19（b）：平均风速越大，湍流越强，空气与烟气的混合就越快，此时温度和动量就迅速减小，抬升就小。
- 图8-19 （c）和（d）：逆温层及逆温层消散前后的不利气象因素阻止烟流的抬升，因而烟气向地面扩散。
- 图8-19（e）和（f）：不利的工厂因素和地形因素引起烟流下沉，影响烟流抬升。

![影响烟气抬升和扩散的有利和不利因素](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\影响烟气抬升和扩散的有利和不利因素.png)

#### 2.2烟气抬升高度的计算公式

##### 2.2.1我国国标（GB3840-83）推荐公式

- 当$Q_{h}≥500{\times}4.18kJ/s$或$T_{s}-T_{a}≥35K$时，有：

$$
\Delta{H}=n_{0}Q_{h}^{n_{1}}H_{s}^{n_{2}}{\overline{u}}^{-1}\tag{2-2}
$$

$$
Q_{h}=0.35p_{a}Q_{v}\frac{\Delta{T}}{T_{s}}\tag{2-3}
$$

$$
\Delta{T}=T_{s}-T_{a}
$$

- $n_{0}$：烟气热状况及地表系数，见表2-1。
- $n_{1}$：烟气热释放率指数，见表2-1。
- $n_{2}$：排气筒高度指数，见表2-1。
- $Q_{h}$：单位时间内排出烟气的热量，$kJ/s$。
- $H_{s}$：排气筒距地面几何高度，m，超过240m时，取$H_{s}=240m$。
- $p_{a}$：大气压力，kPa，如无实测值，可取邻近气象台（站）季或年平均值。
- $Q_{v}$：实际排烟率，$m^3/s$。
- $\Delta{T}$：烟气出口温度与环境温度差，K。
- $T_{s}$：烟气出口温度，K。
- $T_{a}$：环境大气温度，K，如无实测值，可取邻近气象台（站）季或年平均值。
- $\overline{u}$：排气筒出口处平均风速，m/s。

<table>
	<tr>
		<th colspan=5 style="text-align:center">表2-1 n<sub>0</sub>、n<sub>1</sub>、n<sub>2</sub>的选取</th>
	</tr>
	<tr>
		<th style="text-align:center">Q<sub>h</sub>/(kJ/s)</th>
		<th style="text-align:center">地表状况（平原）</th>
		<th style="text-align:center">n<sub>0</sub></th>
		<th style="text-align:center">n<sub>1</sub></th>
		<th style="text-align:center">n<sub>2</sub></th>
	</tr>
    <tr>
    	<td rowspan=2 style="text-align:center">Q<sub>h</sub>&gt;5000</td>
    	<td style="text-align:center">农村或城市远郊区</td>
    	<td style="text-align:center">1.427</td>
    	<td style="text-align:center">1/3</td>
    	<td style="text-align:center">2/3</td>
    </tr>
    <tr>
        <td style="text-align:center">城市及近郊区</td>
    	<td style="text-align:center">1.303</td>
    	<td style="text-align:center">1/3</td>
    	<td style="text-align:center">2/3</td>
    </tr>
    <tr>
    	<td rowspan=2 style="text-align:center">2100≤Q<sub>h</sub>&lt;21000且∆T≥35K</td>
    	<td style="text-align:center">农村或城市远郊区</td>
    	<td style="text-align:center">0.332</td>
    	<td style="text-align:center">3/5</td>
    	<td style="text-align:center">2/5</td>
    </tr>
    <tr>
        <td style="text-align:center">城市及近郊区</td>
    	<td style="text-align:center">0.292</td>
    	<td style="text-align:center">3/5</td>
    	<td style="text-align:center">2/5</td>
    </tr>    
</table>
- 当$Q_{h}<500{\times}4.18kJ/s$或$T_{s}-T_{a}<35K$时，有：

$$
\Delta{H}=\frac{2(1.5{\nu_s}D+0.01Q_{h})}{\overline{u}}\tag{2-4}
$$

- $\nu_s$：烟气喷出速度，m/s。
- $D$：烟囱口内径，m。

##### 2.2.2霍兰德公式

$$
\Delta{H}=\frac{\nu_s{D}}{\overline{u}}\bigg(1.5+2.7\frac{T_s-T_a}{T_s}D\bigg)\\
=(1.5\nu_s{D}+9.6\times10^{-6}Q_h)/{\overline{u}}\tag{2-5}
$$

- 式（2-5）适用于中性条件。考虑大气稳定度的影响，霍兰德建议：
- - 在大气不稳定时：$\Delta{H}$增加$10\%～20\%$。
  - 大气稳定时减少$10\%～20\%$。
  - 常用的校正系数取值如表2-2所示。

<table>
	<tr>
		<th colspan=5 style="text-align:center">表2-2 ∆H的校正系数</th>
	</tr>
	<tr>
		<th style="text-align:center">稳定度差别</th>
		<th style="text-align:center">A,B</th>
		<th style="text-align:center">C</th>
		<th style="text-align:center">D</th>
		<th style="text-align:center">E,F</th>
	</tr>
	<tr>
		<td style="text-align:center">∆H的校正系数</td>
		<td style="text-align:center">1.15</td>
		<td style="text-align:center">1.10</td>
		<td style="text-align:center">1.0</td>
		<td style="text-align:center">0.85</td>
	</tr>
</table>
- 研究发现，霍兰德公式对大多数热源烟气抬升高度估算值偏低2~3倍。故在我国国标（GB3840—83）中规定：在当$Q_{h}<500{\times}4.18kJ/s$或$\Delta{T}<35K$时，仍用霍兰德公式，但取其计算值的2倍作为$\Delta{H}$。

##### 2.2.3博山克特公式

- 它是博山克特等人在1950年最早发表的一个理论公式。该式把烟气抬升高度（$\Delta{H}$）分成为由喷速引起的动力抬升高度（$\Delta{H_m}$）和由温差引起的浮力抬升高度（$\Delta{H_n}$）两个部分，即：

$$
\Delta{H}=\Delta{H_m}+\Delta{H_n}
$$

$$
\Delta{H_m}=\frac{4.77}{1+\frac{0.43\overline{u}}{\nu_s}}\frac{\sqrt{Q_0{\nu_s}}}{\overline{u}}\tag{2-6}
$$

$$
\Delta{H_n}=6.37g\frac{Q_0{\Delta{T}}}{\overline{u}^3{T_a}}\bigg(lnJ^2+\frac{2}{J}-2\bigg)\tag{2-7}
$$

$$
J=\frac{\overline{u}}{(Q_0{\nu_s})^{1/2}}\bigg(0.43\sqrt{\frac{T_a}{g(dQ/dz)}}-0.28\frac{\nu_s}{g}{\cdot}\frac{T_a}{\Delta{T}}\bigg)+1\tag{2-8}
$$

- $Q_0$：温度在$T_a$时的排气量，$m^3/s$。
- $g$：重力加速度，$m/s^2$。
- $dQ/dz$​：位温梯度，$K/m$：
- - 超绝热和中性：$dQ/dz=0.003 K/m$。
  - 等温：$dQ/dz=0.01 K/m$。
  - 中等逆温：$dQ/dz=0.02～0.03 K/m$。
- 本公式计算结果偏高，一般需乘以0.65的修正系数，即：

$$
\Delta{H}=0.65(\Delta{H_m}+\Delta{H_n})\tag{2-9}
$$

- 博山克特公式特别适用于大而强的热源。

### 3.污染物的落地浓度

#### 3.1高斯扩散模式的基本形式

##### 3.1.1高斯模式的坐标系

- 烟囱出口虽然都有一定大小，但只要不是讨论很近距离的污染问题，实用中都可以把它看作"点"源。在考虑这种理想化的点源坐标系时，总是将点源设于地面排放点或高架源排放点在地面的投影点，x轴沿平均风向水平延伸，y轴在水平面上垂直于x轴，z轴垂直xOy平面向上延伸。烟云中心平均路径沿x轴或平行x轴移动。下面介绍的模式都是在这种坐标系中导出的。

![高斯扩散模式的坐标系](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\高斯扩散模式的坐标系.png)

##### 3.1.2高斯模式的有关假定

- 大量的试验和理论研究表明，对于连续源的平均烟流，其浓度分布是符合正态分布的，高斯扩散模式正是在污染物浓度符合正态分布的前提下导出的。
- 其基本假设为：
- - 烟羽的扩散在水平方向和垂直方向都是正态分布.
  - 在扩散的整个空间风速是均匀、稳定的。
  - 污染源排放是连续、均匀的。
  - 污染物在扩散过程中没有衰减和增生。
  - 在x方向，平流作用远大于扩散作用。
  - 地面足够平坦。

- 从这些假定出发，可以导出高斯扩散模式。

##### 3.1.3无界情况的高斯模式

- 当污染源位于无界的空间中，x轴与烟流轴线重合时：

$$
\rho(x,y,z)=\frac{Q}{2\pi\overline{u}\sigma_y\sigma_z}exp\bigg[-\bigg(\frac{y^2}{2\sigma_y^2}+\frac{z^2}{2\sigma_z^2}\bigg)\bigg]\tag{3-1}
$$

- $\rho$：下风向空间某一位置的污染物浓度，$mg/m^3$。
- $\sigma_y$：y方向的标准差（水平扩散参数），$m$。
- $\sigma_x$：z方向的标准差（铅直扩散参数），$m$。
- $\overline{u}$：平均风速，$m/s$。
- $Q$：源强，$mg/s$。

##### 3.1.4有界情况的高斯模式

- 当污染源位于有界的空间中，x轴与烟流轴线不重合时，必须考虑地面对扩散的影响。根据前述假定，污染物在扩散过程中无衰减和增生，那么地面对污染物没有吸收、吸附作用，可以认为地面像镜面一样，对污染物起全反射作用。
- 假设源在空间的坐标位置为(0,0,H)，虚源的位置则为(0,0,-H)：

$$
\rho(x,y,z,H)=\frac{Q}{2\pi\overline{u}\sigma_y\sigma_z}exp\bigg(-\frac{y^2}{2\sigma_y^2}\bigg){\times}\\\bigg\{exp\bigg[-\frac{(z-H)^2}{2\sigma_z^2}\bigg]+exp\bigg[-\frac{(z+H)^2}{2\sigma_z^2}\bigg]\bigg\}\tag{3-2}
$$

- $H$的意义见式（2-1）。
- 式（3.2）即为通常所说的高斯扩散模式，也是**高架连续点源扩散**的基本公式。

#### 3.2一般气象条件下的扩散模式

##### 3.2.1高架连续点源

###### 3.2.1.1地面任意一点的浓度

- 将$z=0$代入式（3-2）：

$$
\rho(x,y,0,H)=\frac{Q}{\pi\overline{u}\sigma_y\sigma_z}exp\bigg(-\frac{y^2}{2\sigma_y^2}\bigg)exp\bigg(-\frac{H^2}{2\sigma_z^2}\bigg)\tag{3-3}
$$

###### 3.2.2.2地面轴线浓度

- 将$y=0$代入式（3-3）：

$$
\rho(x,0,0,H)=\frac{Q}{\pi\overline{u}\sigma_y\sigma_z}exp\bigg(-\frac{H^2}{2\sigma_z^2}\bigg)\tag{3-4}
$$

###### 3.2.2.3地面轴线最大浓度



- 由于扩散参数$\sigma_y$和$\sigma_z$均随下风距离$x$的增大而增大。
- 由式（3-4）可知：
- - 等号右边$Q/({\pi\overline{u}\sigma_y\sigma_z})$项随$x$的增大而减小。
  - $exp(-H^2/2\sigma_z^2)$项则随$x$增大而增大。

- 两项共同作用的结果，必然在下风某一距离$x_m$处出现地面轴线浓度的最大值。
- 假定$\sigma_y$和$\sigma_z$随$x$增大的倍数相同，即$\sigma_y/\sigma_z=k$（常数）。
- 代人式（3-4）后，便得到一个关于$\sigma_z$的单值函数式。
- 然后对$\sigma_z$求导，并令$d\rho/d\sigma_z=0$，则可得出地面轴线最大浓度$\rho_{max}$和出现$\rho_{max}$处的垂直扩散参数$\sigma_z\big|_{x=x_{max}}$的计算式：

$$
\rho_{max}=\frac{2Q}{\pi\overline{u}eH^2}\frac{\sigma_z}{\sigma_y}\tag{3-5}
$$

$$
\sigma_z\big|_{x=x_{max}}=\frac{H}{\sqrt{2}}\tag{3-6}
$$

- $e$：自然对数的底，$e=2.718$。
- 由于$\sigma_z$是距离的函数，故式（3-5）表示了最大浓度点与源高的关系。

##### 3.2.2地面连续点源

###### 3.2.2.1地面连续源在下风向地面上任一点的浓度

- 将$H=0$代入式（3-2）：

$$
\rho(x,y,0,0)=\frac{Q}{2\pi\overline{u}\sigma_y\sigma_z}exp\bigg[-\bigg(\frac{y^2}{2\sigma_y^2}+\frac{z^2}{2\sigma_z^2}\bigg)\bigg]\tag{3-7}
$$

###### 3.2.2.2地面连续点源在下风向地面轴线浓度：

- 将$y=0$代入式（3-7）：

$$
\rho(x,0,0,0)=\frac{Q}{2\pi\overline{u}\sigma_y\sigma_z}\tag{3-8}
$$

#### 3.3特殊气象条件下的扩散模式

##### 3.3.1有上部逆温层的扩散模式

- 如果大气低层处于不稳定状态，而某一高度以上有逆温层存在，这时上部逆温层就像一个“盖子”一样使污染物垂直扩散受到限制，扩散只能在地面和逆温层之间进行，所以又称为“封闭型”扩散。
- 推导这种扩散模式时，把逆温层底面看成和地面一样能起反射的镜面，污染物浓度可看成实源和无穷多对虚源作用之总和。这样，空间任一点的浓度可由下式确定：

![地面和逆温层对烟云多次反射模型](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\地面和逆温层对烟云多次反射模型.png)
$$
\rho(x,y,z,H)=\frac{Q}{2\pi\overline{u}\sigma_y\sigma_z}exp\bigg(-\frac{y^2}{2\sigma_y^2}\bigg){\times}\\\sum^{+\infty}_{n=-\infty}\bigg\{exp\bigg[-\frac{(z-H+2nL)^2}{2\sigma_z^2}\bigg]+exp\bigg[-\frac{(z+H+2nL)^2}{2\sigma_z^2}\bigg]\bigg\}\tag{3-9}
$$

- - $L$：逆温层高度，m。
  - $n$：—烟流在两界面之间的反射次数，一般n=3或4时已包括主要反射。
- 这个公式过于繁琐，实际中可作如下的简化处理：设$x_D$为烟羽边缘刚好达逆温层底时离烟源的水平距离，则：

![有上部逆温层的扩散](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\有上部逆温层的扩散.png)

- 当$x<x_D$时，烟流扩散不受逆温影响，仍可采用式（3-2）进行计算。
- 当$x≥2x_D$时，污染物经过多次反射后，在z方向的浓度逐渐均匀，水平方向仍呈正态分布：
- - 地面浓度的计算公式为：

$$
\rho(x,y,0,H)=\frac{Q}{\sqrt{2\pi}L\overline{u}\sigma_y}exp\bigg(-\frac{y^2}{2\sigma_y^2}\bigg)\tag{3-10}
$$

- - 地面轴线浓度公式为：

$$
\rho(x,0,0,H)=\frac{Q}{\sqrt{2\pi}L\overline{u}\sigma_y}\tag{3-11}
$$

- 当$x_D<x<2x_D$时，有浓度和距离的双对数坐标图上，取$x=x_D$和$x=2x_D$两点浓度的内插值。

##### 3.3.2熏烟扩散模式

- 夜间，若形成了辐射逆温，高架源的烟流排入稳定的逆温层中，垂直扩散很缓慢，在源高的下风向形成一个扇形污染区。日出后，辐射逆温层自下而上消失。当逆温消退到烟流下界时，污秽的烟气迅速向下扩散，此时上部仍为逆温，扩散只能向下发展，造成地面高浓度污染，这就是熏烟型扩散。

![熏烟型扩散](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\熏烟型扩散.png)

- 该过程持续发展，当逆温消退到烟流顶部时达到高潮。逆温继续向上消退后，烟气完全处于不稳定气层中，扩散在各个方向自由发展，原先的高浓度区不复存在，熏烟过程终止。熏烟型扩散一般发生在清晨，持续时间视各地情况及季节不同而异，一般为0.5~2h。
- 熏烟污染过程的浓度计算有以下几种模式（以下各式中下标$f$）代表熏烟：

###### 3.3.2.1模式一

- 当逆温刚消退到烟流顶高（$L_f$）时，可认为全部烟羽受上部逆温的抑制而向下混合。此时地面浓度公式可由式（3-10）导出，只是L应换成逆温消失高度（$L_f$）。
- 地面熏烟浓度：

$$
\rho_f(x,y,0,H)=\frac{Q}{\sqrt{2\pi}L_f\overline{u}\sigma_{yf}}exp\bigg(-\frac{y^2}{2\sigma_{yf}^2}\bigg)\tag{3-12}
$$

- 轴线熏烟浓度：

$$
\rho_f(x,0,0,H)=\frac{Q}{\sqrt{2\pi}L_f\overline{u}\sigma_{yf}}\tag{3-13}
$$

- 式中：

$$
L_f=H+2.15\sigma_z(稳定)\tag{3-14}
$$

$$
\sigma_{yf}=\sigma_y(稳定)+\frac{H}{8}\tag{3-15}
$$

###### 3.3.2.2模式二

- 若逆温消退到高度$z_f$，而$H<z_f<L$，此时只有$z_f$以下的烟气向下扩散，源强Q只包括$z_f$以下的部分，则地面浓度为：

$$
\rho_f(x,y,0,H)=\frac{Q\int\frac{1}{\sqrt{2\pi}}exp\big(-\frac{1}{2}p^2\big)dp}{\sqrt{2\pi}z_f\overline{u}\sigma_{yf}}exp\bigg(-\frac{y^2}{2\sigma_{yf}^2}\bigg)\tag{3-16}
$$

- 式中：

$$
p=\frac{z_f-H}{\sigma_z}\tag{3-17}
$$

###### 3.3.2.3模式三

- 若逆温消退到有效源高$H$，即$z_f=H$，$p=0$，上式积分项等于$1/2$，表示有一半烟气向下扩散。
- 地面熏烟浓度：

$$
\rho_f(x,y,0,H)=\frac{Q}{2\sqrt{2\pi}H\overline{u}\sigma_{yf}}exp\bigg(-\frac{y^2}{2\sigma_{yf}^2}\bigg)\tag{3-18}
$$

- 地面轴线熏烟浓度：

$$
x \rho_f(x,0,0,H)=\frac{Q}{2\sqrt{2\pi}H\overline{u}\sigma_{yf}}\tag{3-19}
$$

#### 3.4扩散参数的确定

- 从上述扩散模式可以看出，扩散参数$\sigma_y$、$\sigma_z$是估算大气污染物浓度的两个重要参数。
- 扩散参数直接与大气湍流性质有关，它的定量规律可以通过大气扩散理论研究和实验两方面获得。
- 但目前实用的扩散参数以实验资料为主要依据。通常$\sigma_y$和$\sigma_z$都是通过野外现场实验得到，再把这些数据表示为扩散距离、大气稳定度和下垫面粗糙度的函数，从而获得一些经验扩散参数公式。

##### 3.4.1Passquill扩散参数

- Passquill在1961年推荐了一种仅需要常规气象观测资料就可以估算烟云扩散参数的方法。Gifford进一步将它制成应用更为方便的图表，因此这种方法又称**P-G曲线法**。
- 大气稳定度分类按Passquill分类法，**公式适用范围为下风向100km**。
- 图8-25和图8-26示出了不同稳定度下$\sigma_y$和$\sigma_z$随下风距离变化的经验曲线（取样时间10 min）。
- 一旦知道某地某时的大气稳定度，就可以从这些曲线上查到各下风距离$x$上的$\sigma_y$和$\sigma_z$值。
- 计算**地面轴线最大浓度***（$\rho_{max}$）和它出现的距离（$x_{max}$）时，可先按$\sigma_z=H/\sqrt{2}$ 计算出$\sigma_z\big|_{x=x_{max}}$，再从图8-26上查出对应的$x$值，此值即为该稳定度下的$x_{max}$，再从图8-25上查出与$x_{max}$对应的$\sigma_y$值，代入式（3-7）即可算出$\rho_{max}$值。

![下风距离和水平扩散参数关系](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\下风距离和水平扩散参数关系.png)

![下风距离和铅直扩散参数关系](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\下风距离和铅直扩散参数关系.png)

- 计算**非最大地面浓度**时，不能用$\sigma_z=H/\sqrt{2}$计算，而是根据下风距离$x$，由P-G曲线直接查得$\sigma_y$和$\sigma_z$，然后根据需要代入式（3-3）和式（3-4）进行计算。
- 为了克服从书刊资料中扩散曲线上确定$\sigma_y$和$\sigma_z$的误差，英国伦敦气象局给出了相应的查算表（表3-1），从这个表上可以用内插法求出在$20km$范围内的$\sigma_y$和$\sigma_z$值。

![扩散参数表](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\扩散参数表.png)

- Passquill这套数据适用于平原地区，对于粗糙度较大的地区，则应向不稳定方向提高1～2级后再查表或图。

##### 3.4.2Briggs扩散参数

- Briggs在前人研究的基础上，考虑到下垫面和烟囱高度的影响，提出了一套估算平原地区和城市地区的扩散参数公式，这套公式对于高烟囱排放适用于下风向20~30km左右的范围。表8-9和表8-10分别列出了这套估算$\sigma_y$和$\sigma_z$的公式（取样时间30min）。

![Briggs扩散参数](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\Briggs扩散参数.png)

##### 3.4.3国标推荐的扩散参数

- **平原地区农村及城市远郊区**：A、B、C级稳定度直接由表7-19和表7-20查出扩散参数$\sigma_y$和$\sigma_z$幂指数，D、E、F级稳定度则需要向不稳定方向提半级后查算。
- **工业区或城区**：
- - 工业区A、B级不提级，C级提到B级，D、E、F级向不稳定方向提一级半。
  - 非工业区的城区，A、B 级不提级，C级提到B级或C级，D、E、F级向不稳定方向提一级。
  - 再查表7-19和表7-20。
- **丘陵山区的农村或城市**：同城市工业区。
- **表中参数**：
- - $\sigma_y={\gamma_1}x^{\alpha_1}$
  - $\sigma_z={\gamma_2}x^{\alpha_2}$

![水平扩散参数幂函数表达式系数1](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\水平扩散参数幂函数表达式系数1.png)

![水平扩散参数幂函数表达式系数2](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\水平扩散参数幂函数表达式系数2.png)

![铅直扩散参数幂函数表达式系数](F:\Study\Python\PythonAdventure\Scraper\Dissertation\Data\Knowledge\picture\PollutantsGroundConcentration\铅直扩散参数幂函数表达式系数.png)

#### 3.5影响浓度的时间因素

- 大气扩散模式所估算的污染物浓度都是在一定时间内的平均值。
- 实践证明，随着时间的延长，平均浓度将降低，这是由于取样时间延长，风的摆动增大，从而使横向扩散参数$\sigma_y$随取样时间而增大。
- 但垂直方向的扩散因受地面限制，当时间延长到10~20秒以后，$\sigma_z$就不随取样时间而增大了。
- 污染物平均浓度随取样时间延长而降低的这一特性叫做**时间稀释作用**，可用如下关系表示：

$$
\rho_1=\rho_2\bigg(\frac{t_2}{t_1}\bigg)^P\tag{3-20}
$$

$$
\sigma_{y2}=\sigma_{y1}\bigg(\frac{t_2}{t_1}\bigg)^P\tag{3-21}
$$

- $\rho_1,\rho_2$：分别对应取样时间为$t_1、t_2$时的浓度。
- $\sigma_{y1},\sigma_{y2}$：分别对应取样时间为$t_1、t_2$时的水平扩散参数。
- $P$：时间稀释指数，查表3-2.

<table>
	<tr>
		<th colspan=6 style="text-align:center">表3-2 国标推荐的P值取法</th>
	</tr>
	<tr>
		<th style="text-align:center">稳定度</th>
		<th style="text-align:center">B</th>
		<th style="text-align:center">B~C</th>
		<th style="text-align:center">C</th>
		<th style="text-align:center">C~D</th>
		<th style="text-align:center">D</th>
	</tr>
	<tr>
		<td style="text-align:center">t=0.5~2h</td>
		<td style="text-align:center">0.27</td>
		<td style="text-align:center">0.29</td>
		<td style="text-align:center">0.31</td>
		<td style="text-align:center">0.32</td>
		<td style="text-align:center">0.35</td>
	</tr>	
	<tr>
		<td style="text-align:center">t=2~24h</td>
		<td style="text-align:center">0.36</td>
		<td style="text-align:center">0.39</td>
		<td style="text-align:center">0.42</td>
		<td style="text-align:center">0.45</td>
		<td style="text-align:center">0.48</td>
	</tr>	
</table>	

### 4.烟囱计算

#### 4.1烟囱高度计算

##### 4.1.1精确计算法

- 该法计算过程是先假定一个烟囱高度（$H_s$），再计算抬升高度（$\Delta{H}$），然后将当地的气象条件、地形条件和污染源条件代人扩散模式进行计算，得出下风向地面浓度分布，如浓度分布数据达不到规定的要求，则另取一个较大的$H_s$值，重复以上过程：如达到要求，可降低烟囱高度，重复上述过程，直到所取的$H_s$值为满足地面浓度要求的最小值。

##### 4.1.2简化计算法

- 该法以地面最大浓度不超过规定要求为依据，直接由最大浓度公式求出烟囱高度。这种方法简单快速，应用广泛。设允许地面浓度为$\rho_k$，则按式（3-5）导出的烟囱高度为：

$$
H_s=\sqrt{\frac{2Q}{\pi{e}\overline{u}\rho_k}{\cdot}\frac{\sigma_z}{\sigma_y}}-\Delta{H}\tag{3-22}
$$

- $\Delta{H}、\sigma_y、\sigma_z$参照前面的内容确定。

###### 4.1.2.1风速$\overline{u}$

- 风速对污染物的地面浓度有很大影响。
- 当同时考虑风速对烟气抬升高度和扩散稀释的作用时，其作用是相反的。因此最大着地浓度随风速的变化不是单调的，使最大着地浓度达到极大值的风速称为危险风速或临界风速，用$\overline{u}_c$表示。此时所对应的浓度称为绝对最大着地浓度，以$\rho_{absm}$表示。
- 危险风速$\overline{u}_c$与绝对最大着地浓度$\rho_{absm}$的关系：

$$
\rho_{absm}=\frac{Q}{2\pi{e}H_s^2\overline{u}_c}\frac{\sigma_z}{\sigma_y}\tag{3-23}
$$

- 此时烟囱高度为：

$$
H_s\geq\sqrt{\frac{Q}{2\pi{e}\overline{u}_c(\rho_0-\rho_B)}{\cdot}\frac{\sigma_z}{\sigma_y}}\tag{3-24}
$$

- $\rho_0,\rho_B$：见下式（3-25）。

- 如果烟囱高度选用危险风速来设计，将保证地面污染物浓度在任何情况下不会超过允许标准，然而设计出的烟囱也是最高的，在经济实力雄厚时是一种可取的办法。
- 事实上，各地的气象资料表明，危险风速出现频率很小，为满足这种很少出现的情况而花过多的投资是不合算的。
- 如果按常年平均风速来设计烟囱，则其高度较小，投资较省，但只能保证有50%的几率使地面污染物浓度不超过允许值，当风速小于平均风速时，就可能超标。
- 因此，从环保和经济两方面来看，选择一个具有可接受的保证率的风速来设计烟囱高度是比较合理的，它可以保证在可接受的保证率下地面污染物浓度不超过允许标准。对于污染较大但出现频率较低的气象条件，可以通过污染预报，用调节生产的办法来解决。

###### 4.1.2.2允许标准$\rho_k$

$$
\rho_k=\frac{fp}{k}(\rho_0-\rho_B)\tag{3-25}
$$

- $\rho_0$：当地执行的大气环境质量标准。
- $\rho_B$：当地目前的本底浓度。
- $f$：该项目可占的污染权重，通常取：$f=70\%$。
- $k$：污染源密集系数，参照表3-3取值。
- $p$：地形因子，取值由当地环保部门决定，也可参照表3-4取值。

<table>
	<tr>
		<th colspan=2 style="text-align:center">表3-3 多烟囱污染源的密集系数</th>
	</tr>
	<tr>
		<th style="text-align:center">同一高度的烟囱数</th>
		<th style="text-align:center">k</th>
	</tr>
	<tr>
		<td style="text-align:center">2</td>
		<td style="text-align:center">1.7</td>
	</tr>
	<tr>
		<td style="text-align:center">3</td>
		<td style="text-align:center">2.41</td>
	</tr>	
	<tr>
		<td style="text-align:center">4</td>
		<td style="text-align:center">3.0</td>
	</tr>	
 	<tr>
		<td style="text-align:center">5</td>
		<td style="text-align:center">3.6</td>
	</tr>	
 	<tr>
		<td style="text-align:center">6</td>
		<td style="text-align:center">4.2</td>
	</tr>	
	<tr>
		<td style="text-align:center">7</td>
		<td style="text-align:center">4.71</td>
	</tr>	
	<tr>
		<td style="text-align:center">8</td>
		<td style="text-align:center">5.3</td>
	</tr>	 
	<tr>
		<td style="text-align:center">9</td>
		<td style="text-align:center">5.8</td>
	</tr>
	<tr>
		<td style="text-align:center">10</td>
		<td style="text-align:center">6.3</td>
	</tr>    
</table>

<table>
	<tr>
		<th colspan=4 style="text-align:center">表3-4 p的取值</th>
	</tr>
	<tr>
		<th style="text-align:center">地形条件</th>
		<th style="text-align:center">平原</th>
		<th style="text-align:center">丘陵</th>
		<th style="text-align:center">山区</th>
	</tr>
	<tr>
		<td style="text-align:center">p</td>
		<td style="text-align:center">1.0</td>
		<td style="text-align:center">0.7</td>
		<td style="text-align:center">0.5</td>
	</tr>	
</table>
- 进行烟囱高度设计时，还应注意以下问题：
- - 避免气流下洗现象或下沉现象对烟囱的影响，要求烟囱高度至少为邻近建筑物或障碍物高度的2.5倍。
  - 避免烟囱有效高度（$H$）与出现频率最高或较多的混合层高度相等。因为此时的情况最坏，地面污染浓度为一般情况下的2倍。

#### 4.2烟囱出口直径计算

$$
D=\sqrt{\frac{4Q_y}{\pi{\nu_s}}}\tag{3-26}
$$

- $D$：烟囱出口直径，$m$。
- $Q_y$：烟气排放量，$m^3/s$。
- $\nu_s$：烟气出口速度，$m/s$。
- 通常选取$\nu_s/u>2.0$作为设计准则。
- 烟气出口速度的大小对烟流抬升影响很大。$\nu_s$大，烟气的动量也大，但却促进了与周围空气的混合，反而减少了烟流的整个抬升。因此应适当选择烟气出口速度，一般取：$\nu_s=20～30m/s$。

### 5.例题

- 在东经$104°$、北纬$31°$的某平原郊区，建有一个工厂。工厂产生的含$SO_2$废气是通过一座高$110m$、出口内径为$2m$的烟囱排放的。废气量为$4×10^5m^3/h$（烟囱出口状态），烟气出口温度$150℃$，$SO_2$排放量为$400kg/h$。在1989年7月13日北京时间13时，当地的气象状况是气温$35℃$、云量$2/2$、地面风速$3m/s$，试计算此时距烟囱$3000m$的轴向浓度和由该厂造成的$SO_2$最大地面浓度及产生距离。

#### 5.1确定已知量

- 经度：$\lambda=104^o$

- 纬度：$\varphi=31^o$
- 烟囱实体高度：$H_{s}=110m$
- 烟囱出口直径：$D=2m$
- 烟气（实际）排放量：$Q_v=Q_y=4{\times}10^5m^3/h=111.11m^3/s$
- 烟气出口温度：$T_s=273.15+150=423.15K$
- 环境大气温度：$T_a=273.15+35=308.15K$
- 源强：$Q=400kg/h=1.11{\times}10^5mg/s$
- 观测进行时的北京时间：$t=13h$
- 水平扩散距离：$x=3000m$

#### 5.2确定大气稳定度

- 查表1-5得7月13日的太阳倾角：$\theta=21^o$
- $15t+\lambda-300=15{\times}13+104-300=-1(^o)$
- 将参数代入式（1-7）得太阳高度角：

$$
h_0=arcsin[sin31^osin21^o+cos31^ocos21^ocos(-1)^o]=arcsin0.985\approx80.0^o
$$

- 根据云量$2/2$和$h_0=80.0^0$查表1-4得太阳辐射等级为：$+3$
- 有太阳辐射等级$+3$和地面风速$3m/s$查表1-3得此时大气稳定度为：$C类$

#### 5.3确定烟囱口平均风速

- 根据烟囱高度$z=H_s=110m$查表1-2确定风速指数：$m=0.20$
- 高度$10m$处的风速近似为地面风速：$u_10=3m/s$
- 代入式（1-2）得烟囱口处平均风速：

$$
\overline{u}=u_{10}\bigg(\frac{z}{10}\bigg)^m=3{\times}\bigg(\frac{110}{10}\bigg)^{0.20}=4.85m/s
$$

#### 5.4确定有效源高

- 单位时间内排出烟气的热量，公式（2-3）：

$$
Q_h=0.35p_aQ_v\frac{T_s-T_a}{T_s}\\=0.35{\times}101.325{\times}111.11{\times}\frac{423.15-308.15}{423.15}=1070.88kJ/s
$$

- 烟气抬升公式采用国标推荐公式，由于$Q_{h}=1070.88kJ/s<500{\times}4.18=2090kJ/s$，采用公式（2-4）进行计算：

$$
\Delta{H}=\frac{2(1.5{\nu_s}D+0.01Q_{h})}{\overline{u}}\\
=\frac{2(1.5{\frac{Q_v}{\pi{D}^2/4}}D+0.01Q_{h})}{\overline{u}}\\
=\frac{2{\times}(1.5{\times}{\frac{111.11}{\pi{\times}{2}^2/4}}{\times}2+0.01{\times}1070.88)}{4.85}=48.16m
$$

- 根据式（2-1）算出有效源高：

$$
H=H_s+\Delta{H}=110+48.16=158.16m
$$

#### 5.5 确定扩散参数

- 由平原郊区、大气稳定度为$C$类且$x=3000m$，查表3-1得：
- $\sigma_y=269$
- $\sigma_z=167$

#### 5.6 确定$3000m$处轴线浓度

- 根据高架连续点源地面轴线浓度公式（3-4）得：

$$
\rho(3000,0,0,H)=\frac{Q}{\pi\overline{u}\sigma_y\sigma_z}exp\bigg(-\frac{H^2}{2\sigma_z^2}\bigg)\\
=\frac{1.11{\times}10^5}{\pi{\times}4.85{\times}269{\times}167}exp\bigg(-\frac{158.16^2}{2{\times}167^2}\bigg)=0.104mg/m^3
$$

#### 5.7确定地面最大浓度及产生距离

- 由式（3-6）求得最大距离：

$$
\sigma_z\big|_{x=x_{max}}=\frac{H}{\sqrt{2}}=\frac{158.16}{\sqrt{2}}=111.83m
$$

- 由式（3-5）求得地面最大浓度：

$$
\rho_{max}=\frac{2Q}{\pi\overline{u}eH^2}\frac{\sigma_z}{\sigma_y}=\frac{2{\times}1.11{\times}10^5}{\pi{\times}4.85{\times}e{\times}158.16^2}{\times}\frac{167}{269}=0.133mg/m^3
$$
