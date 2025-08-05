print("Hello, World!")
# This script prints "Hello, World!" to the console.
# It serves as a simple demonstration of a Python script.

# 接下来是一个简单的Python脚本，它打印一条问候消息。
# 它演示了Python中的基本语法和字符串格式化。
# 脚本还包括一个注释，解释了代码的目的。

name = "Winfred Hofheimer"
print(f"Hello, I'm {name}!")

# This script prints a greeting message with a variable.
# It demonstrates the use of f-strings for string interpolation in Python.

a = 1
b = 2

c = a + b
print(f"The sum of {a} and {b} is {c}.")
# This script demonstrates basic variable assignment and string formatting in Python.
# It assigns values to variables, performs a calculation, and prints the result.    

# 打井号时，则代表这一行为注释

# This is a simple Python script that prints a greeting message.
# It demonstrates basic syntax and string formatting in Python.

# The script also includes a comment explaining the purpose of the code.
# The following code defines a function to check if a string is a valid Python identifier.
def is_valid_identifier(name):
    """
    检查字符串是否为有效的Python标识符。
    仅用于教学演示，实际开发请勿随意使用exec。
    """
    try:
        exec(f"{name} = None")
        return True
    except Exception:
        return False

if __name__ == "__main__":
    # 1. 测试is_valid_identifier函数
    print(is_valid_identifier("2var"))  # False
    print(is_valid_identifier("var2"))  # True

    # 2. 打印一条问候消息，包含一个变量
    name = "Winfred Hofheimer"
    print(f"Hello, I'm {name}!")

    # 3. 计算两个变量的和，并打印结果
    a = 1
    b = 2
    c = a + b
    print(f"The sum of {a} and {b} is {c}.")

# 注释：
# 本脚本演示了Python的基本语法、变量赋值、字符串格式化和标识符检查函数。
# 所有测试代码均放在主程序入口，便于模块化和复用。