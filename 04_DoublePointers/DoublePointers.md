# 双指针

双指针能够将嵌套的双循环转换成单循环问题，能够减小算法时间复杂度  
一般来说，能够将O($n^2$)优化为O($n$)

滑窗条件能够优化时间复杂度的本质在于，题目求解答案有隐含关系：  
例如，两数之和，排序后的数组，隐含了元素大小和两个指针一大一小。  
盛水问题隐含了，一定要有两个大的板子才能装水。  
如果能发现类似的隐含条件，可以考虑使用滑窗算法。

## 追逐指针
解决无重复最长子串，长度最小子数组等问题  
如你所见，如果是有约束的子数组或者子字符，就可以考虑追逐指针滑窗。
关键在于，厘清终止条件，防止遗漏情况。(例如，到底前后哪个指针遍历结束为止)

### 例题
1. [和为s的连续正数序列](./findContinuousSequence.py)  
   https://leetcode.cn/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
   
2. [无重复字符的最长子串](./lengthOfLongestSubstring.py)  
   https://leetcode.cn/problems/longest-substring-without-repeating-characters/

## 夹击指针
解决盛水最多容器，接雨水，两(三)数之和等  
夹击指针的指针更新关系往往不如追逐指针的直观，但是一般搞清楚更新条件，这题也就做出来了。
典型的就比较前后指针对应元素的大小，终止条件一般为两指针交汇时。  

### 例题
1. [和为s的两个数字](./twoSumInSortArray.py)  
   https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/description/

2. [三数之和](./threeSum.py)   
   https://leetcode.cn/problems/3sum/

3. [TODO 接雨水(ZiJie必考)](./rainWater.py)  
   https://leetcode.cn/problems/trapping-rain-water/

## 编号指针
其他双指针算法在我的理解中不算是滑窗算法。  
严格来说，就是一个指针用于遍历，一个指针记录数组编号的位置，满足条件则进行交互。  
典型的是快排的交互。  

### 例题
1. [TODO 调整奇偶数](./adjustPlan.py)  
   https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/

## 快慢指针
快慢指针是指两个指针，以不同的速度遍历，之所以是快慢指针而不是追逐指针，是因为两个指针遍历的速度是不一样的，常用的就是slow = slow.next; fast = fast.next.next;  
该方法常常用于，判断是否陷入无限循环，寻找中间或者几分之处的点。使用时，要注意判断结束条件，避免空指针等问题。

### 例题
1. [TODO 环形链表](./cycleLinkedList.py)  
   https://leetcode.cn/problems/linked-list-cycle-ii/

## 中心扩展指针
用于解决回文问题  
判断是否为互文串时使用中心扩展法

### 例题
1. [最长回文串](./longestHuiwenSubstring.py)  
   https://leetcode.cn/problems/longest-palindromic-substring/
