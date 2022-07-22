def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str


def is_palindrome(input_string):
    new_string = input_string.strip()
    reverse_string = reverse(new_string)
    if new_string.lower() == reverse_string.lower():
        return True
    return False 




print(is_palindrome("NeverOddorEven")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
