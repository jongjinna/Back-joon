a = input()
num = 0
dic = {1:["A","B","C"], 2:["D","E","F"], 3:["G","H","I"], 4:["J","K","L"], 5:["M","N","O"], 6:["P","Q","R","S"], 7:["T","U","V"], 8:["W","X","Y","Z"]}
for k in a:
  for i in dic:
    for j in dic[i]:
        if k == j:
          num += (i+2)

print(num)