
def is_palindrome(word):
    return word == word[::-1]


print(is_palindrome("kajajk"))


def is_palindrome2(word):
   first = 0
   end = len(word) - 1
   while first < end:
       if word[first] != word[end]:
           return False
       first += 1
       end -= 1
   return True
