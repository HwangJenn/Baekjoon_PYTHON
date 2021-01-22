n=int(input())
score=list(map(int, input().split()))
up=max(score)
result=0
for i in range(0,n):
    score[i]=score[i]/up*100
    result=result+score[i]
result=result/n
print(result)