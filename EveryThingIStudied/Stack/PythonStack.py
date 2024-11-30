from collections import deque


def implement_stack():
    mystack = deque()

    while True:
        print(f"the mystack is {mystack} \n Please choose the operations")
        print(f"1.) Push \t 2.) Pop \t 3.) Exit")
        user_ip = int(input().strip())
        if user_ip == 1:
            ele = input("Please enter a number : ")
            mystack.append(ele)
            print(f"the mystack of adding ele is {mystack}")
        elif user_ip == 2:
            mystack.pop()
            print(f"the mystack of poping is {mystack}")
        elif user_ip == 3:
            exit()
        else:
            print("(*_*) wrong input brother, enter once more")


if __name__ == "__main__":
    implement_stack()
