# chaos
def main():
    print("研究一下混沌现象")
    x = eval(input("输入任意一个0到1之间的数="))
    for i in range(20):
        x = 3.9*x*(1-x)
        print(x)


main()
