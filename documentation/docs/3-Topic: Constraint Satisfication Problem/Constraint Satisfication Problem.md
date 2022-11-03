# Constraint Satisfaction Problems

## Outline

1. Defining Constraint Satisfaction Problems
2. Backtracking Search for Constraint Satisfaction Problems
3. Variable Selection (Heuristics)
	- Minimum Remaining Values
	- Degree Heuristic
4. Value Selection (Heuristics)
5. Interleaving Search and Inference
	- Forward Checking
	- Arc Consistency Algorithm
6. The Structure of Constraint Satisfaction Problems
7. Conditioning
8. Tree Decomposition

## Defining Constraint Satisfaction Problems

![](https://i.imgur.com/aivdM06.png)

### Definition
![](https://i.imgur.com/VgsHe8b.png)



### Examples
![](https://i.imgur.com/CHfN8xp.png)
![](https://i.imgur.com/upvJLOi.png)



### Constraint Graph

![](https://i.imgur.com/A7m8xZN.png)


### Varities of Constraints
![](https://i.imgur.com/HDEKgGa.png)



## Backtracking Search for Constraint Satisfaction Problems

### Standard Search Formulation

![](https://i.imgur.com/QkAHwoo.png)

![](https://i.imgur.com/noQrPgd.png)

### Backtracking Search
Backtracking Search

- We can drastically improve the naive approach by considering that variable assignments are **commutative**:
$[W A=$ red then $N T=$ green $]$ same as $[N T=$ green then $W A=$ red $]$
$\Rightarrow$ Only consider assignments to a single variable at each level
$\Rightarrow b=d$ and there are only $d^n$ leaves
- Depth-first search for CSPs with single-variable assignments is called *backtracking search*.
- Backtracking search is the basic uninformed algorithm for CSPs (e.g., solves the $n$-queens problem for $n \approx 25$ ).

![](https://i.imgur.com/4i4ghiX.png)

![](https://i.imgur.com/EHPm6eG.png)
![](https://i.imgur.com/JYnRDB5.png)
![](https://i.imgur.com/vGG4rJQ.png)
![](https://i.imgur.com/WvmK6JO.png)
![](https://i.imgur.com/m4ZG26v.png)


## Variable Selection (Heuristics)
![](https://i.imgur.com/uCv3xZW.png)

![](https://i.imgur.com/655LXBR.png)




## Value Selection (Heuristics)

![](https://i.imgur.com/W5VSEDK.png)

## Comments on Variable and Value Selection

![](https://i.imgur.com/8EK1szp.png)



## Interleaving Search and Inference 交织搜索和推理

![](https://i.imgur.com/2oveye9.png)

### Arc-Consistency

![](https://i.imgur.com/kKDTHUv.png)

![](https://i.imgur.com/QLLQPOe.png)

### Inference 1: Forward Checking
![](https://i.imgur.com/fCVxRVT.png)

![](https://i.imgur.com/m8VjY4G.png)

![](https://i.imgur.com/wTPuuY5.png)


![](https://i.imgur.com/qEio8bn.png)


### Inference 2: Arc Consistency Algorithm
![](https://i.imgur.com/5RomWQf.png)
![](https://i.imgur.com/m4qo8qn.png)

#### Example 

![](https://i.imgur.com/M3ZeqDy.png)

![](https://i.imgur.com/aIzt0uB.png)

![](https://i.imgur.com/EnD7yao.png)
![](https://i.imgur.com/AxjBCah.png)
![](https://i.imgur.com/s88Kumu.png)
![](https://i.imgur.com/dBpsXvS.png)
![](https://i.imgur.com/CRkq7LO.png)

![](https://i.imgur.com/PQ295xj.png)




## The Structure of Constraint Satisfaction Problems

### Problem Structure 

![](https://i.imgur.com/gekMvND.png)

### Complexity Reduction of Independent Problems
![](https://i.imgur.com/SFcgN8m.png)

### Tree-Structured CSPs
![](https://i.imgur.com/MA38lTl.png)
![](https://i.imgur.com/zA01LZB.png)

#### Examples
![](https://i.imgur.com/NK7NPis.png)
![](https://i.imgur.com/MvNQGlF.png)
![](https://i.imgur.com/EsuIqMV.png)

### Nearly tree-structured CSPs: Conditioning (1)
![](https://i.imgur.com/4znhObq.png)
![](https://i.imgur.com/YyMlZW4.png)






### Nearly tree-structured CSPs: Tree Decomposition

![](https://i.imgur.com/3QPEcqg.png)
![](https://i.imgur.com/Zk0jQsQ.png)
![](https://i.imgur.com/xOZ1ihu.png)


## Summary
![](https://i.imgur.com/ic85D5F.png)
![](https://i.imgur.com/JfPmBuw.png)
