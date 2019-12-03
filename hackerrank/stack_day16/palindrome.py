from hackerrank.stack_day16.my_stack import Stack


def palindrome(word):
    n = len(word)
    word = word.lower()
    if n % 2 != 0:
        edge1 = int(n / 2)
        edge2 = edge1 + 1
    else:
        edge1 = int(n / 2)
        edge2 = edge1

    s = Stack()
    for l in word[:edge1]:
        s.push(l)
    for l in word[edge2:]:
        if l != s.pop():
            return False
    return True

def clean_text(word):
    symbols = "'.?, "
    cleaned_word = ""
    for letter in word:
        if letter not in symbols:
            cleaned_word += letter
    return cleaned_word

lst = ["Anna", "Civic", "Kayak", "Level", "Redder", "racecar"]
for word in lst:
    print(palindrome(word))

phrases = ["Don't nod.", "I did, did I?", "My gym", "Red rum, sir, is murder", "Step on no pets", "Top spot"]

for phrase in phrases:
    cleaned_word = clean_text(phrase)
    print(palindrome(cleaned_word))

print(palindrome("letter"))
