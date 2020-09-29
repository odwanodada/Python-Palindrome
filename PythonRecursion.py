def recursion(word):
    if len(word)<2:
        return True
    else:
        if word[0]==word[-1]:
            return  recursion(word[1:-1])
        else:
            return "Is not a palindrome"


put_word = str(input("Please enter a word"))
result=recursion(put_word)
print(result)

