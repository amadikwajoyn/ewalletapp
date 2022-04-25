# me = [2,2,3,3,4,5]
# mme = set(me)

# print(mme)

def is_palindrome(word):
    k = word.lower()
    word_reverse = k[::-1]
    if k == word_reverse:
        print(True)
    else:
        print(False)


is_palindrome("Nurses run")
is_palindrome("Nurses all run")
is_palindrome("Alamala")
is_palindrome("aLAmala")
is_palindrome("amala")
