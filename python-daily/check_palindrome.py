
def palindrome(str_input):
    n = len(str_input)-1
    for i in range(round(n/2)):
        if str_input[i]!=str_input[n-i]:
            return False
    return True
def main():
    # Your code goes here
    str_input = input("enter string - ")
    if palindrome(str_input):
        print(str_input, "is palindrome")
    else:
        print(str_input, "is not palindrome")
    
if __name__ == "__main__":
    main()

