total = int(input())
for i in range(int(input())):
    a, b = map(int, input().split())
    total -= a*b

print("Yes") if total == 0 else print("No")