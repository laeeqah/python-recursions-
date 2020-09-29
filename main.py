#check if number is a palindrome

def is_palindrome(a_string):
    if len(a_string) <= 1:
        return True
    if a_string[0] == a_string[len(a_string) -1]:
        return is_palindrome(a_string[1:-1])
    else:
        return False

a_string = input("Please enter a string: ")

print(is_palindrome(a_string))
