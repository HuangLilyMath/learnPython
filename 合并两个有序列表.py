s1=[int(i) for i in input().split(" ")]
s2=[int(i) for i in input().split(" ")]

if s1==[]:
    print(s2)
if s2==[]:
    print(s1)

result=[]
i=0
j=0
while True:
    if s1[i] < s2[j]:
        result.append(s1[i])
        i=i+1
    elif s1[i]>s2[j]:
        result.append(s2[j])
        j=j+1
    else:
        result.append(s1[i])
        result.append(s2[j])
        i+=1
        j+=1
    if i == len(s1):
        result.extend(s2[j:])
        break
    if j == len(s2):
        result.extend(s1[i:])
        break
print(result)