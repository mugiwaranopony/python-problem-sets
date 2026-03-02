def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    return n % 2 == 0


    # return True if n % 2 == 0 else False


    # if n % 2 == 0:
    #      return True
    # else:
    #     return False

# if x % 2 == 0:
#     print("even")
# else:
#     print("odd")

main()
