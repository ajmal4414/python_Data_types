# arrange string character such that lowercase letter should come first
str1="HeLLOWorld"

lower=[]
upper=[]
for i in (str1):
    if i.islower():
        lower.append(i)

    else:
        upper.append(i)
sorted_string = ''.join(lower+upper)
print("Newstring is :",sorted_string)

