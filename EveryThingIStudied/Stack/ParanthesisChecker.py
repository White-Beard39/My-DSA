from collections import deque


def check_paranthesis():

    user_ip = input("Please enter only paranthesis : ")
    stack = deque()

    for x in user_ip:
        try:
            if x == "(":
                stack.append(x)
            else:
                stack.pop()
        except IndexError as e:
            print("Brother you have imbalenced paranthesis")
            return
    if len(stack) == 0:
        print("Success !!")
    else:
        print(f"Failure!! \n Here's the stack {stack}")


if __name__ == "__main__":
    check_paranthesis()
