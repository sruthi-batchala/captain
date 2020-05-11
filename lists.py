#test case1
n=int(input('enter number'))
lst=[]
for i in range(n):
    num=int(input('enter the value'))
    if num>0:
        lst.append(num)
print(lst)

#test case2
n=int(input())
val=[]
num=list(map(int,input().split()))
for i in range(len(num)):
    if num[i]>0:
        val.append(num[i])
print(val)
