import heapq

class Element:
  def __init__(self, priority1, priority2, value):
    self.priority1 = priority1
    self.priority2 = priority2
    self.value = value

  # __lt__方法是只有一个元素可以比较大小时所调用的方法
  def __lt__(self, other):
    return self.priority1 >= other.priority1 and self.priority2 >= other.priority2


n, H, A = map(int, input().split())
line = input().split()
h = [int(s) for s in line]
line = input().split()
a = [int(s) for s in line]

nums = [0 for _ in range(n)]

pq = []
for i in range(len(h)):
    heapq.heappush(pq, Element(h[i], a[i], i))

count = 0
for i in range(n):
    e = heapq.heappop(pq)
    if H >= e.priority1 and A >= e.priority2:
        count += 1
        H = e.priority1
        A = e.priority2
    else:
        continue

print(count)
