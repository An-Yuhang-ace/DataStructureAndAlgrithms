# 链表
一种物理存储单元上非连续的存储结构，数据通过链表中的指针链接是实现逻辑连续
各类对象按照线性排列，单向，顺序由对象指针决定，每个元素有一个关键字和一个指针next。

相比于线性表的顺序结构，操作较为复杂，但是因为不必按顺序存储，可以充分利用计算机内存空间，实现灵活的内存动态管理。

## 链表的删除与插入
删除或者插入，涉及该节点以及其前后节点的连接。
实际实现中，为了便于操作，避免单向性带来的不便，常常使用hair技巧。
即在链表head前插入一空节点hair，在查找时统一向前一位，便于之后进行删除和插入。

hair技巧能够有效避免边界情况造成的nullpointerError。  
例如：https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/  
使用hair，删除方便，防止越界。

## 遍历查找技巧
遍历只能单向进行，O(n)，可以设置两个或多个指针同时遍历，从而方便查找特定位置的节点。

例如，[删除倒数第N个节点](./removeNthFromEnd.py)  
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/

## 哨兵技巧
设置一个哑对象L.nil，代表null，替换链表中的null，位置放置于表头，表尾之间。
使得代码简洁，但要注意短链表造成的存储空间浪费。

## 单链表练习题
1. [k个一组翻转链表]()
   https://leetcode-cn.com/problems/reverse-nodes-in-k-group/

2. [复杂链表的深拷贝]()
   https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/

## 合并链表练习题
1. [合并有序链表(链表形式归并)]()
   https://leetcode.cn/problems/merge-two-sorted-lists/

2. [合并k个有序链表]()
   https://leetcode-cn.com/problems/merge-k-sorted-lists/
   
## 双向链表
1. [LRU缓存]()
   https://leetcode.cn/problems/lru-cache/
