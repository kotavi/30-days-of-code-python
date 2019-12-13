
def all_palindrome_substring(s):
    """Searches all """
    n = len(s)
    lst = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            temp = s[i:j]
            temp_rev = temp[len(temp)::-1] # the complexity of slicing is O(M) where M is len(temp)
            if temp == temp_rev:
                lst.append(temp)
    return lst


print(all_palindrome_substring("knittingstitchses"))
