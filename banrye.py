def f2(n): return True if n%2 == 0 else False

def f5(n): return True if n%5 == 0 else False

a, b = map(int, input().split())

n1 , n2= list(range(a,a-b,-1)), list(range(1,b+1))

print(min(sum(map(f2,n1)) , sum(map(f5,n1)), sum(map(f2,n2)) , sum(map(f5,n2))))
print(map(f2,n1))