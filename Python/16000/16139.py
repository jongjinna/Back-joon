import sys
cnt = 0
S = sys.stdin.readline().strip()
arr = [[0 for i in range(26)] for i in range(len(S))]
arr[0][ord(S[0]) - 97] = 1
for i in range(1, len(S)):
    arr[i][ord(S[i]) - 97] = 1
    for j in range(26):
        arr[i][j] += arr[i - 1][j]

for i in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().split()
    if int(a[1]) > 0:
        res = arr[int(a[2])][ord(a[0]) - 97] - arr[int(a[1]) - 1][ord(a[0]) - 97]
    else:
        res = arr[int(a[2])][ord(a[0]) - 97]
    sys.stdout.write(str(res)+'\n')
