#BOJ-10039
score=list()
sum=0
for _ in range(5) :
    score.append(int(input()))
for i in range(5) :
    if score[i]<40 :
        score[i]=40
    sum+=score[i]
   
aver=int(sum/5)
print(aver)
