from hackerrank.stack_queue_day16.stack_day16.my_stack import Stack
import string

def palindrome(word):
    word = word.lower()
    start, end = 0, len(word) - 1
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True

def palindrome_with_stack(word):
    word = word.lower()
    n = len(word)
    s = Stack()
    for l in word[:n//2]:
        s.push(l)
    edge = n//2 if n % 2 == 0 else n//2+1
    for l in word[edge:]:
        if l != s.pop():
            return False
    return True


def clean_text(word):
    letters = string.ascii_lowercase + string.ascii_uppercase
    cleaned_word = ""
    for letter in word:
        if letter in letters:
            cleaned_word += letter
    return cleaned_word


lst = ["Anna", "Civic", "Kayak", "Level", "Redder", "racecar"]
for word in lst:
    print(word, "is a palindrome: ", palindrome(word))
    print(word, "is a palindrome: ", palindrome_with_stack(word))


phrases = ["Don't nod.", "I did, did I?", "My gym", "Red rum, sir, is murder", "Step on no pets", "Top spot"]

for phrase in phrases:
    cleaned_word = clean_text(phrase)
    print(palindrome(cleaned_word))

print(palindrome("letter"))
