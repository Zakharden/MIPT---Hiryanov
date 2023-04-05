votes = {}
stroka = 'И жили они долго и счастливо, пока смерть не разлучила их!'
stroka_list = stroka.split()
for i in stroka_list:
    if i in votes:
        votes[i]+=1
    else:
        votes[i] = 1

#вместо цикла можно D[i] = D.pop(name,0)+1
print(list(votes.items()))