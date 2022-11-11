# Logical Agents

![](https://i.imgur.com/RIzuJXV.png)

## The Wumpus World

![](https://i.imgur.com/ITR2E5C.png)

> - 洞穴由通道连接的房间组成。
> - 潜伏在某个地方的是可怕的 Wumpus，它会吃掉任何进入他房间的人。
> - 在找到一堆金子之前，你有一支箭射他。



<mark>**[x,y]表示第x列第y行**</mark>



![](https://i.imgur.com/AmzGUiE.png)

> - Wumpus旁边的广场很臭
> - 与坑相邻的广场微风轻拂
> - 如果黄金在同一个方格中，则闪闪发光
> - 如果你面对它，射击会杀死 Wumpus
> - 射击使用了唯一的箭头
> - 如果在同一个方格中，抓取会捡起金子
> - 释放掉金子在同一个正方形

![](https://i.imgur.com/OueKPvb.png)

![](https://i.imgur.com/eawxpkR.png)
![](https://i.imgur.com/M6qiNSQ.png)
![](https://i.imgur.com/74iVn0W.png)
![](https://i.imgur.com/LXvSB5e.png)
![](https://i.imgur.com/wo5Khn2.png)
![](https://i.imgur.com/klwkRdD.png)
![](https://i.imgur.com/u6d9OxL.png)

<div><iframe width="300" height="60" src="https://vocaroo.com/embed/1k19CWZjq4C0?autoplay=0" frameborder="0" allow="autoplay"></iframe><br><a href="https://voca.ro/1k19CWZjq4C0" title="Vocaroo Voice Recorder" target="_blank">View on Vocaroo >></a></div>
> https://voca.ro/1k19CWZjq4C0

## Logic

![](https://i.imgur.com/mbqDkVs.png)
![](https://i.imgur.com/wQtgAsx.png)

> - a推b
>   models: 可能出现的情况

### logical reasoning in the Wumpus Wolrd

![](https://i.imgur.com/7SERaLl.png)
![](https://i.imgur.com/1nTZjh5.png)
![](https://i.imgur.com/vJAR9Ur.png)
![](https://i.imgur.com/dwS7uXL.png)

## Propositional Logic

### syntax

![](https://i.imgur.com/tNMoMwX.png)
![](https://i.imgur.com/JMPVRZB.png)

### Semantics

![](https://i.imgur.com/wyZvtv7.png)

### Truth Tables

![](https://i.imgur.com/a6GzvdG.png)

### WW Sentences

![](https://i.imgur.com/txLZien.png)

### Inference by enumaration

![](https://i.imgur.com/c3MPI66.png)

## Propositional Theorem Proving

### Introduction to Theorem Proving

![](https://i.imgur.com/2TrDRgI.png)
![](https://i.imgur.com/aVi0SUh.png)
![](https://i.imgur.com/p6OAcyC.png)

> 这个“分号”的意思是推， 和 ==> 差不多

![](https://i.imgur.com/XQHXSXu.png)
![](https://i.imgur.com/7xpbDnR.png)

#### WW examples

![](https://i.imgur.com/mSMqnUa.png)

#### automated theorem proving

![](https://i.imgur.com/JTMLKA5.png)

### Proof by Resolution

![](https://i.imgur.com/rlOkynX.png)
![](https://i.imgur.com/rL4yKEg.png)
![](https://i.imgur.com/bXYYjv2.png)
![](https://i.imgur.com/nVcJOyy.png)


**Unit resolution rule:**

($I_1 \vee \ldots l_{i} \ldots \vee I_k$) $\land$ $m$, where $l_i \equiv \neg m$,

then: $I_1 \vee \ldots \vee I_{i-1} \vee I_{i+1} \vee \ldots \vee I_k$



**Full resolution rule**:

$\left(I_1 \vee \ldots l_i \ldots \vee I_k\right) \wedge (m_1 \vee \ldots m_{j} \vee \vee m_n)$, where $l_i \equiv \neg m_{j}$ then: $I_1 \vee \ldots \vee I_{i-1} \vee I_{i+1} \vee \ldots \vee I_k$

then: $I_1 \vee \ldots \vee I_{i-1} \vee I_{i+1} \vee \ldots \vee I_k \vee m_1 \vee \ldots \vee m_{j-1} \vee m_{j+1} \vee \ldots \vee m_n$

> 分析：
> 
> 如果上面式子为false, 则一定能推下面， 所以只考虑上面式子为true的情况
> 
> 不妨设li = false, mj = True, 则上面式子想要成立， li... $l_{i-1}$, $l_{i+1}$ ... lk 必须有一个成立， 这种情况下下面式子也成立





![](https://i.imgur.com/ip2DeWf.png)





#### Conjunctive Normal Form

![](https://i.imgur.com/neHRXoW.png)

> “非”在最里面， 然后是“或”， 最外面是“且”





![](https://i.imgur.com/67Hgb4N.png)





![](https://i.imgur.com/9JngD4k.png)



![](https://i.imgur.com/q8dtzw3.png)

![](https://i.imgur.com/aLFTLWA.png)

![](https://i.imgur.com/spcsIXh.png)

![](https://i.imgur.com/KYp0MB4.png)

![](https://i.imgur.com/lNmOYOv.png)





### Proof of Horn Clauses 自动推导

![](https://i.imgur.com/02jsDl5.png)





#### And-Or graph

![](https://i.imgur.com/9OA1DQ7.png) 

#### forward chaining

![](https://i.imgur.com/BegCzm7.png)
![](https://i.imgur.com/tlltFeD.png)
![](https://i.imgur.com/2Si83FC.png)
![](https://i.imgur.com/a5HNiLO.png)
![](https://i.imgur.com/JhrSlc6.png)
![](https://i.imgur.com/dnKXy1A.png)
![](https://i.imgur.com/mWZyEPW.png)
![](https://i.imgur.com/mGTQw94.png)

#### backward chaining

![](https://i.imgur.com/CnbEZ6G.png)
![](https://i.imgur.com/MwJMHXV.png)
![](https://i.imgur.com/HsCWc6x.png)
![](https://i.imgur.com/8mlg7mj.png)
![](https://i.imgur.com/5sD82vI.png)
![](https://i.imgur.com/JtjY3TR.png)
![](https://i.imgur.com/s8N7fAX.png)
![](https://i.imgur.com/AbiKDjq.png)
![](https://i.imgur.com/txbSIEh.png)
![](https://i.imgur.com/ZTeTedc.png)
![](https://i.imgur.com/j0LmmJX.png)

#### forward vs backward chaining

![](https://i.imgur.com/rwmb2sI.png)
