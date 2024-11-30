def main(nums):

    print(f"the input is {nums}")
    print(f"choose : \n 1. pop \t 2.push \t 3.exit:")
    user_input = input()
    try:
        if user_input == "pop":
            print(nums.pop())
            main(nums)
        elif user_input == "push":
            nums.append(input("Please enter an element to push : "))
            print(f"the new arr is {nums}")
            main(nums)
        elif user_input == "exit":
            exit
        else:
            print(f"wrong input brother")
            main(nums)
    except Exception as e:
        print(f"Oops!! an exception occured : {e}")


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    main(nums)
