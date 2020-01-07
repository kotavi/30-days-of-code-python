def remove_vowels(str_line):
    new_str = str()
    vowels = "euioa"
    for s in str_line:
        if s not in vowels:
            new_str += s
    return new_str

print(remove_vowels("remote: Resolving deltas: 100% (1/1), completed with 1 local object."))

