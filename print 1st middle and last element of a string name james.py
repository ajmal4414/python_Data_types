# print 1st middle and last element of a string name james

str1="james"

result=str1[0]

l=len(str1)

mi=int(l/2)

result=result+str1[mi]
result=result+str1[l - 1]
print("new string:",result)
