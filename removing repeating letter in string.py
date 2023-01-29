# removing repeating letter in string

str1="let's google the pineapple"
print('given string is:', str1)
splitstr1=str1.split(" ")

newlist=[]

for i in splitstr1:
    k=" "
    for j in  i:
        if j in  k:
            continue
        else:
            k= k+j

    newlist.append(k)

newstring= " ".join((newlist))

print("removing repeating letter", newstring)