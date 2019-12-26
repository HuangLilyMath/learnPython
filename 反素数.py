# 判断是否为素数
def isPrime(i):
  for j in range(2,i):
    if i % j == 0:
      return False
  return True

# 把一个数反过来写
def reverse(i):
  number = i
  result = 0
  while number != 0:
    remainder = number % 10
    result = result * 10 + remainder
    number = number // 10
  return result



n = input()
n = int(n)
i = n + 1
count = 1
result=[]  #新建一个空列表
while count <= 10:
    j = reverse(i)
    if isPrime(i) and isPrime(j) and i != j:
        result.append(str(i))  #把i变成str后，加到列表尾部
        count = count + 1
    i = i + 1
print(' '.join(result)) #用‘ ’把列表的各个元素拼成一个字符串
