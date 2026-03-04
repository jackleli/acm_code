n, q = map(int, input().split())
s = [input() for i in range(n)]
trans = [i for i in range(26)]
for i in range(q):
  a, b = input().split()
  ord_a = ord(a) - ord('a')
  ord_b = ord(b) - ord('a')
  for i in range(26):
    if trans[i] == ord_a:
      trans[i] = ord_b
  # print(*trans)
for i in range(n):
  v = []
  for c in s[i]:
    oc = ord(c) - ord('a')
    # print(oc, trans[oc])
    v.append(chr(trans[oc]+ ord('a')))
  print(*v, sep="")
