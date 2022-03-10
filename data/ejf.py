heap = []

def SiftUp(i):
    if i == 0:
        return
    p = (i - 1) // 2
    if heap[i] < heap[p]:
        heap[i], heap[p] = heap[p], heap[i]


def SiftDown(i):
    l = i * 2 + 1
    r = i * 2 + 2
    if l == len(heap):
        return
    if l == len(heap) - 1:
        r = l
    imin = l
    if heap[r] < heap[l]:
        imin = r
    if heap[i] > heap[imin]:
        heap[imin], heap[i] = heap[i], heap[imin]


def add(i):
    heap.append(i)
    SiftUp(len(heap) - 1)

def get(i):
    tmp = heap[0]
    heap[0] = heap[-1].pop()
    SiftDown(0)
    return tmp

n = int(input())
for i in range(n):
    add(int(input()))

for i in range(n):
    print(get())