def calculator():
    num1 = float(input("请输入第一个数字: "))
    num2 = float(input("请输入第二个数字: "))
    operator = input("请输入要执行的操作 (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
        print("结果:", result)
    elif operator == '-':
        result = num1 - num2
        print("结果:", result)
    elif operator == '*':
        result = num1 * num2
        print("结果:", result)
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
            print("结果:", result)
        else:
            print("除数不能为零！")
    else:
        print("无效的操作符！")

calculator()