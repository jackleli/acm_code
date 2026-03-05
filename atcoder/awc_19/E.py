import heapq

n = int(input())
car = []
for i in range(n):
  w, d = map(int, input().split())
  car.append((w, d))
car.sort(key=lambda x: x[0] + x[1])

heap = []
tot_w = 0
for w, d in car:
  tot_w += w
  heapq.heappush(heap, -w)
  if tot_w > d + w:
    hv = -heapq.heappop(heap)
    tot_w -= hv
print(len(heap))