a, b = map(int, input().split(" ")
c = int(input())
min = (b + c) % 60
hour = (b + c) // 60
if hour >= 24:
    hour -= 24
print(hour, min)
