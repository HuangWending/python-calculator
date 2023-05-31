# python-calculator
Python计算器程序
def calculator(): - 定义了一个名为 calculator 的函数。
num1 = float(input("请输入第一个数字: ")) - 提示用户输入第一个数字，并将其转换为浮点数类型，并将其赋值给变量 num1。
num2 = float(input("请输入第二个数字: ")) - 提示用户输入第二个数字，并将其转换为浮点数类型，并将其赋值给变量 num2。
operator = input("请输入要执行的操作 (+, -, *, /): ") - 提示用户输入要执行的操作符，并将其赋值给变量 operator。
if operator == '+': - 如果操作符是 '+'，执行下面的代码块。
result = num1 + num2 - 将 num1 和 num2 相加，并将结果赋值给变量 result。
print("结果:", result) - 输出计算结果。
elif operator == '-': - 如果操作符是 '-'，执行下面的代码块，依此类推。
elif operator == '*':
elif operator == '/':
if num2 != 0: - 检查除数是否为零。
result = num1 / num2 - 如果除数不为零，将 num1 除以 num2，并将结果赋值给变量 result。
print("结果:", result) - 输出计算结果。
else: - 如果除数为零，执行下面的代码块。
print("除数不能为零！") - 输出除数不能为零的错误信息。
else: - 如果操作符不是 '+', '-', '*', '/' 中的任何一个，执行下面的代码块。
print("无效的操作符！") - 输出无效操作符的错误信息。
最后，通过调用 calculator() 函数，程序会开始运行，并提示用户输入数字和操作符，然后执行相应的计算操作，并将结果输出到控制台。
