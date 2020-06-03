def palindrome(num):

    '''Function takes a number converts it to string, reverses it and checks if both are same.If both are same it returns True else Flase.'''

    #convering num to string
    num = str(num)

    #reversing the number
    rev_num = num[::-1]

    if num == rev_num:
        return True
    
    return False

if __name__ == "__main__":
    
    #taking input
    i = int(input("Enter a Number: "))
    
    if palindrome(i):
        print("The number is palindrome")
    else:
        print("The number is not palindrome")