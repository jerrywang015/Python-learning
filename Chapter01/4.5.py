# chaos
def main():
    print("研究一下混沌现象")
    x = eval(input("输入任意一个0到1之间的数="))
    n = eval(input("选择打印出来值的数量="))
    for i in range(n):
        x = 3.9*x*(1-x)
        print(x)


main()
