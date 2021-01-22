n=int(input())
for i in range(n):
    num=list(map(int,input().split()))
    avg=sum(num[1:])/num[0]
    count=0
    for score in num[1:]:
        if score>avg:
            count+=1
    rate=count/num[0]*100
    print(f'{rate:.3f}%')
