# Hash
## 为啥使用Hash？
Hash快，根据索引直接访问。  
完成Hash的索引构建后，查找速度可以视为常数。

## 如何使用Hash？
分析查找需求，选择合适的<key, value>键值对。  
例如，Q1中，就将数组大小作为key，数组索引作为value。

## 遍历构建Hash：
构建Hash时的直观思路时先构建，再查找。  
但实际编程中，有时可以通一遍遍历，将构建和查找同步进行。  
不过有时确实需要两遍遍历，注意判断。

## 例题
1. [两数之和](./twoSum.py)  
   https://leetcode.cn/problems/two-sum/
   
