# https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/

def trainingPlan(a):
    j = 0
    for i in range(len(a)):
        if a[i] % 2 == 1:
            swap(a, i, j)
            j += 1
    return a  

def swap(a, i, j):
    temp = a[j]
    a[j] = a[i]
    a[i] = temp

if __name__ == "__main__":
    actions = [1,2,3,4,5]
    print(trainingPlan(actions))