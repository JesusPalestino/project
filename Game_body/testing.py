var1 = "thxxg"
var2 = "hing"
count = 0 
for x in var1:
    for y in var2:
        print(x,y)
        if x==y:
            count+=1
 
print(count)

def hammer_distance(guess, answer):
    if len(guess) != len(answer):
        if len(guess)< len(answer):
            while len(guess)<len(answer):
                guess+=" "
        elif len(guess) > len(answer):
            answer += " "

    distacne = 0
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            distacne+=1
        
    return distacne
print(hammer_distance("thing","tping"))

