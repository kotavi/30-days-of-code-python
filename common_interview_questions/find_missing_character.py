"""
Given two strings with all but one character in common (one character missing from the first string),
return the character that is in the 2nd string but not in the 1st.
"""
from collections import Counter


def find_missing_character(s1, s2):
    collection1 = Counter(s1)
    collection2 = Counter(s2)

    if sorted(collection1.values()) == sorted(collection2.values()):
        print("The same number of letters")
    else:
        missing = set(collection2.keys()) - set(collection1.keys())
        if missing:
            print("Missing: ", missing)
        else:
            for key, val in collection2.items():
                if val != collection1[key]:
                    print("Missing: ", key)


find_missing_character("kitten", "kitten")
find_missing_character("vocal", "vocation")
find_missing_character("knittinggstitchses", "knittingggstitchses")
