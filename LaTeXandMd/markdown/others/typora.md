

- [图与网络模型](#图与网络模型)
  - [哥尼斯堡七桥问题](#哥尼斯堡七桥问题)
  - [图与网络的基本概念](#图与网络的基本概念)
    - [无向图](#无向图)
    - [有向图](#有向图)
    - [完全图、二分图](#完全图二分图)
    - [子图](#子图)
    - [顶点的度](#顶点的度)
    - [图与网络的数据结构](#图与网络的数据结构)
    - [轨与联通](#轨与联通)
  - [应用——最短路问题](#应用最短路问题)
    - [两个指定顶点之间的最短路径](#两个指定顶点之间的最短路径)
      - [$Dijkstra$算法](#mathsemanticsmrowmidmimiimimijmimikmimismimitmimirmimiamimrowannotation-encodingapplicationx-texdijkstraannotationsemanticsmathdijkstra算法)
      - [数学规划模型](#数学规划模型)
    - [每对顶点的最短路径](#每对顶点的最短路径)
  - [最小生成树问题](#最小生成树问题)
    - [prim 算法构造最小生成树](#prim-算法构造最小生成树)
    - [Kruskal 算法构造最小生成树](#kruskal-算法构造最小生成树)
  - [匹配问题](#匹配问题)
    - [人员分派问题&匈牙利算法](#人员分派问题匈牙利算法)
    - [最优分派问题&Kuhn-Munkres 算法](#最优分派问题kuhn-munkres-算法)
  - [Euler 图和Hamilton 图](#euler-图和hamilton-图)


<a id="markdown-图与网络模型" name="图与网络模型"></a>
# 图与网络模型

<a id="markdown-哥尼斯堡七桥问题" name="哥尼斯堡七桥问题"></a>
## 哥尼斯堡七桥问题
通过一些例子来了解网络优化问题。
+ 最短路问题
+ 公路连接问题
+ 指派问题（assignment problem）
+ 中国邮递员问题（Cpp－Chinese postman problem）
+ 旅行商问题（TSP－traveling salesman problem）
+ 运输问题（transportation problem）
<a id="markdown-图与网络的基本概念" name="图与网络的基本概念"></a>
## 图与网络的基本概念
<a id="markdown-无向图" name="无向图"></a>
### 无向图
+ 顶点集或节点集  无序对/边
+ 赋权无向图或无向网络
+ 环：端点重合为一点的边
+ 简单图，既没有环也没有两条边连接同一对顶点
<a id="markdown-有向图" name="有向图"></a>
### 有向图
+ 与无向类似
+ 弧$a_{k}=v_{ij}$,称$v_{i}$为$a_{k}$的尾,$v_{j}$为$a_{k}$的头，并称弧$a_{k}$为$v_{i}$的出弧，称弧$a_{k}$为$v_{j}$的入弧
<a id="markdown-完全图二分图" name="完全图二分图"></a>
### 完全图、二分图
&emsp;每一对不同的顶点都有一条边相连的简单图称为完全图$(complete graph)$。$n$ 个顶点的完全图记为$K_{n}$。
+ 二分图 完全二分图
<a id="markdown-子图" name="子图"></a>
### 子图
+ 子图与母图
+ 生成子图
<a id="markdown-顶点的度" name="顶点的度"></a>
### 顶点的度
&emsp;设$v\epsilon V(G)$，$G$中与$v$关联的边数（每个环算作两条边）称为$v$的度$(degree)$，记作$d(v)$。若$d(v)$是奇数，称$v$是奇顶点$(odd point)；d(v)$是偶数，称v是偶顶点$(even point)$。关于顶点的度，我们有如下结果：
+ $$\begin{aligned}\sum_{v\epsilon V}d(v)=2\varepsilon \\\end{aligned} $$
+ 任意一个图的奇顶点的个数是偶数。
<a id="markdown-图与网络的数据结构" name="图与网络的数据结构"></a>
### 图与网络的数据结构
&emsp;计算机上用来描述图与网络的5 种常用表示方法：邻接矩阵表示法、关联矩阵表示法、弧表表示法、邻接表表示法和星形表示法。
+ 邻接矩阵表示法
  图$G = (V, A)$的邻接矩阵是如下定义的：$C$是一个$n\times n$的0-1矩阵，即
$$
\begin{aligned}
  C=(c_{ij})_{n\times n}\epsilon \{0,1\}^{n\times n},\\
  (c_{ij})=\begin{cases}1,&(i,j)\in A，\\0,&(i,j)\notin A.\\\end{cases}\end{aligned}
$$
+ 关联矩阵表示法
  &emsp;图$G = (V, A)$的关联矩阵$B$是如下定义的：$B$是一个$n ×m$ 的矩阵，即
$$
\begin{aligned} 
  B&=(b_{ik})_{n \times m}\in\{-1,0,1\}^{n\times m}\\
  b_{ik}&=\begin{cases}
  1, &\exists j\in V,k=(i,j)\in A,\\
  -1, &\exists j\in V,k=(j,i)\in A,\\
  0, &其他\\\end{cases}\end{aligned}
$$
  &emsp;在关联矩阵中，每行对应于图的一个节点，每列对应于图的一条弧。如果一个节点是一条弧的起点，则关联矩阵中对应的元素为 $1$；如果一个节点是一条弧的终点，则关联矩阵中对应的元素为−1；如果一个节点与一条弧不关联，则关联矩阵中对应的元素为 0

+ 弧表表示法
  &emsp;弧表表示法直接列出所有弧的起点和终点，共需$2m$个存储单元。
+ 邻接表表示法 
  &emsp;所谓图的邻接表，也就是图的所有节点的邻接表的集合；而对每个节点，它的邻接表就是它的所有出弧。邻接表表示法就是对图的每个节点，用一个单向链表列出从该节点出发的所有弧，链表中每个单元对应于一条出弧。为了记录弧上的权，链表中每个单元除列出弧的另一个端点外，还可以包含弧上的权等作为数据域。
+ 星形表示法。
  &emsp;在该数组中首先存放从节点1 出发的所有弧，然后接着存放从节点2出发的所有孤，依此类推，最后存放从节点n 出发的所有孤。对每条弧，要依次存放其起点、终点、权的数值等有关信息。这实际上相当于对所有弧给出了一个顺序和编号，只是从同一节点出发的弧的顺序可以任意排列。为了能够快速检索从每个节点出发的所有弧，我们一般还用一个数组记录每个节点出发的弧的起始地址（即弧的编号）。

<a id="markdown-轨与联通" name="轨与联通"></a>
### 轨与联通

&emsp;$W=v_0e_1v_1e_2v_2···e_kv_k$，其中$e_i\in E(G),1\leq i\leq k,v_j\in (G),0\leq j\leq k,e_i$与$
v_{i-1},v_i$ 关联，称$W$是图$G$的一条道路(walk)。

&emsp;若道路$W$的边互不相同，则$W$称为迹(trail)。若道路$W $的顶点互不相同，则$W$ 称为轨(path)。称一条道路是闭的，如果它有正的长且起点和终点相同。起点和终点重合的轨叫做圈(cycle)。

&emsp;联通(connected)    距离$d (u,v)$   联通图(任意二点均联通)

+ 图$P$是一条轨的充要条件是$P$是连通的，且有两个一度的顶点，其余顶点的度为2；
+ 图C 是一个圈的充要条件是$C$是各顶点的度均为2 的联通图。

<a id="markdown-应用最短路问题" name="应用最短路问题"></a>
## 应用——最短路问题

<a id="markdown-两个指定顶点之间的最短路径" name="两个指定顶点之间的最短路径"></a>
### 两个指定顶点之间的最短路径

<a id="markdown-dijkstra算法" name="dijkstra算法"></a>
#### $Dijkstra$算法
1. 令 $l(u_0)=0$，对$v\neq u_0$，令$l(v)=\infty$，$S={u_0}$，$i=0$
2. 对每个$v\in \overline{S_i}(\overline{S_i}=\frac{V}{S_i})$，用
  $$\underset{u\in S_i}{\operatorname{min}}\{l(v),l(u)+w(uv)\}$$
  代替$l(v)$。计算$\underset{v\in S_i}{\operatorname{min}}\{l(v)\}$， 把达到这个最小值的一个顶点记为$u_{i+1}$，令$S_{i+1}=S_i\bigcup \{u_{i+1}\}$。
3. 若$i=|V|-1$，停止；若$i<|V|-1$，用$i+1$代替$i$，转$2$

&emsp;算法结束时，$u_0$至各项点的最短路也在图上标示出来了。

从起点$sb$到终点$db$通用的$Dijkstra$算法程序如下：

>```matlab
>function [mydistance,mypath]=mydijkstra(a,sb,db);
>% 输入：a—邻接矩阵(aij)是指i到j之间的距离，可以是有向的
>% sb—起点的标号, db—终点的标号
>% 输出：mydistance—最短路的距离, mypath—最短路的路径
>n=size(a,1);visited(1:n)=0;
>distance(1:n)=inf; distance(sb)=0;%保存起点到各顶点的最短距离
>visited(sb)=1;u=sb;%u为最新的P顶点标号
>parent(1:n)=0;%前驱顶点的初始化
>for i=1:n-1
>	id=find(visited==0);%查找为标号的顶点
>	for v=id
>		if a(u,v)+distance(u)<distance(v)
>			distance(v)=a(u,v)+distance(u);%修改标号值
>			parent(v)=u;
>		end
>	end
>	temp=distance;
>	temp(visiten==1)=inf;%已标号点的距离换成无穷
>	[t,u]=min(temp);%找标号值最小的顶点
>	visited(u)=1;%标记已经标号的顶点
>end
>mypath=[];
>if parent(db)~=0
>	t=db;mypath=[db];
>	while t~=sb
>		t=parent(t);
>		mypath=[t mypath];
>	end
>end
>mydistance=distance(db);
>```

<a id="markdown-数学规划模型" name="数学规划模型"></a>
####  数学规划模型

+ 假设有向图有$n$个顶点，现需要求从顶点 $v_1$到顶点$v_n$的最短路。设$W=(v_{ij})_{n\times n}$ 为
  赋权邻接矩阵，其分量为
$$
w_{ij}=\begin{cases}弧v_i v_j的权值，&v_iv_k\in E\\\infty，&其他\end{cases}
$$
&emsp;&emsp;决策变量为$x_{ij}$，当 $x_{ij}=1$，说明弧 $v_iv_j$位于顶点 $v_1$ 至顶点$v_n$的路上；否则 $x_{ij}=0$。其
数学规划表达式为
$$
\mathrm{min}\sum\limits_{v_iv_j\in E}w_{ij}x_{ij}\\
\mathrm{s.t.}\begin{cases}\sum\limits_{\ j=1v_iv_{j}\in E}^n x_{ij}-\sum\limits_{\ j=1v_iv_{j}\in E}^n x_{ji}=\begin{cases}1,i=1,\\-1,i=n,\\0,i\neq 1,n,\end{cases}\\x_{ij}=0或1.\end{cases}
$$

+ 无向图最短路问题

<a id="markdown-每对顶点的最短路径" name="每对顶点的最短路径"></a>
### 每对顶点的最短路径

+ 可以 $\mathrm{Dijkstra}$算法，算法复杂度为$O(n^3)$

+ $\mathrm{Floyd}$算法
  对于赋权图$G=(V,E,A_0)$，其中顶点集$V={v_1,···,v_n}$，邻接矩阵
  $$
  \begin{aligned}
  	A_0&=\begin{bmatrix}
  	a_{11}&a_{12}&\dots&a_{1n}\\
  	a_{21}&a_{22}&\dots&a_{2n}\\
  	\vdots&\vdots&\ddots&\dots\\
  	a_{n1}&a_{n2}&\dots&a_{nn}\\
  	\end{bmatrix},\\
  	a_{ij}&=\begin{cases}权值,当v_i与v_j之间有边时,\\
  	\infty,当v_i与v_j之间无边时,\end{cases},i\neq j;\\
  	a_{ii}&=0,i=1,2,\dots,n。\end{aligned}
  $$

  对于无向图，$A_0$是对称矩阵，$a_{ij}=a_{ji}$。
  $Floyd$ 算法的基本思想是：递推产生一个矩阵序列$A_1,\dots,A_k,\dots,A_n$，其中矩阵$A_K$ 的第$i$行第$j$列元素$A_k(i,j)$表示从顶点$v_i$ 到顶点$v_j$的路径上所经过的顶点序号不大于$k$的最短路径长度。
  计算时用迭代公式
  $$
  A_k(i,j)=\mathrm{min}(A_{k-1}(i,j),A_{k-1}(i,k),+A_{k-1}(k,j),),\\
  $$
  $k$是迭代次数，$i,j,k=1,2,\dots,n$。
  
  从起点$sb$到终点$db$通用的$Floy$算法程序如下：
  
  > ```matlab
  > function [dist,mypath]=myfloyd(a,sb,db);
  > % 输入：a—邻接矩阵，元素(aij)是顶点i到j之间的直达距离，可以是有向的
  > % sb—起点的标号；db—终点的标号
  > % 输出：dist—最短路的距离；% mypath—最短路的路径
  > n=size(a,1); path=zeros(n);
  > for k=1:n
  >     for i=1:n
  >         for j=1:n
  >             if a(i,j)>a(i,k)+a(k,j)
  >                 a(i,j)=a(i,k)+a(k,j);
  >                 path(i,j)=k;
  >             end
  >         end
  >     end
  > end
  > dist=a(sb,db);
  > parent=path(sb,:); %从起点sb到终点db的最短路上各顶点的前驱顶点
  > parent(parent==0)=sb; %path中的分量为0，表示该顶点的前驱是起点
  > mypath=db; t=db;
  > while t~=sb
  >         p=parent(t); mypath=[p,mypath];
  >         t=p;
  > end
  > ```

<a id="markdown-最小生成树问题" name="最小生成树问题"></a>
## 最小生成树问题

<a id="markdown-prim-算法构造最小生成树" name="prim-算法构造最小生成树"></a>
### prim 算法构造最小生成树

1. $P={v_1},Q=\emptyset$.

2. while $P$~=$V$
   找最小边$pv$,其中$p\in P,v\in V-P$;
$$
   \begin{aligned}
   P&=P+{v};\\
   Q&=Q+{pv};
   \end{aligned}\\
$$
&emsp;&emsp;&emsp;end


<a id="markdown-kruskal-算法构造最小生成树" name="kruskal-算法构造最小生成树"></a>
### Kruskal 算法构造最小生成树

1. 选 $e_1\in E(G)$ ，使得 $w(e_1)=\mathrm{min}$。

2. 若$e_1,e_2,\dots,e_i$已选好，则从 $E(G)-{e_1,e_2,\dots,e_i}$中选取$e_{i+1}$ ，使得

   + $G[e_1,e_2,\dots,e_i,e_{i+1}]$中无圈，且

   + $w( e_{i+1} )min$
   
3. 直到选得 $e_{v-1}$为止
<a id="markdown-匹配问题" name="匹配问题"></a>
## 匹配问题

<a id="markdown-人员分派问题匈牙利算法" name="人员分派问题匈牙利算法"></a>
### 人员分派问题&匈牙利算法

工作人员$x_1,x_2,\dots,x_n$去做$n$件工作$y_1,y_2,\dots,y_n$，每人适合做其中一件或几件，问能否每人都有一份适合的工作？如果不能，最多几人可以有适合的工作？

这个问题的数学模型是： $G$​ 是二分图，顶点集划分为$V (G) = X \bigcup Y ,X=\{x_1,\dots,x_n\},Y=\{y_1,\dots,y_n\}$，当且仅当 $x_i$适合做工作$y_j$ 时，$x_iy_j\in E(G)$ ，求$G$ 中的最大对集。

匈牙利算法：

1. 从$G$ 中任意取定一个初始对集$M$ 。

2. 若$M$ 把$X$ 中的顶点皆许配，停止，$M$ 即完美对集；否则取$X$ 中未被$M$ 许
  配的一顶点u，记$S = {u}，T = Φ$。
  
3. 若$N(S) = T$ ，停止，无完美对集；否则取 $y∈N(S) − T$ 。

4. 若 $y$ 是被$M$ 许配的，设 $yz∈M ，S = S \bigcup\{z\}，T = T \bigcup\{y\}$，转（iii）；
  否则，取可增广轨$P(u, y)$，令$M = (M − E(P)) \bigcup(E(P) − M)$，转（ii）。
<a id="markdown-最优分派问题kuhn-munkres-算法" name="最优分派问题kuhn-munkres-算法"></a>
### 最优分派问题&Kuhn-Munkres 算法

在人员分派问题中，工作人员适合做的各项工作当中，效益未必一致，我们需要制定一个分派方案，使公司总效益最大。

这 个 问 题 的 数 学 模 型 是 ： 在 人 员 分 派 问 题 的 模 型 中 ， 图 $G$的每边加了权
$w(x_iy_j)\geq 0$，表示 $x_i$干$y_j$ 工作的效益，求加权图$G$ 上的权最大的完美对集。

<a id="markdown-euler-图和hamilton-图" name="euler-图和hamilton-图"></a>
## Euler 图和Hamilton 图
