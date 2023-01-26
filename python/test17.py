n=int(input("enterr n:"))
score_list=[]

#get scores
for i in range(n):
    score=float(input("enter score:"))
    score_list.append(score)

#calculate mean
    sum=0
    for j in range(len(score_list)):
        sum+=score_list[j]

        print(sum/n)