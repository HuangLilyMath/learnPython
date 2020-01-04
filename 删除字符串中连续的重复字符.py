# 通过键盘输入一串小写字母（a~z）组成的字符串，
# 编写一个测试程序，将字符串中连续出现的重复字符删去（即在一个字符串中，如果遇到连续重复的字符只出现一次），
# 然后输出处理后的字符串。例如：
# str1="aabbccddaabbccdd"，输出结果为："abcdabcd"。

def myFun(string):
    if len(string) == 0:
        return ""
    pre=string[0]
    result=""
    result+=pre
    for i in range(1,len(string)):
        current=string[i]
        if pre == current:
            continue
        pre=current
        result+=pre
    return result

string = input()
print(myFun(string))

    