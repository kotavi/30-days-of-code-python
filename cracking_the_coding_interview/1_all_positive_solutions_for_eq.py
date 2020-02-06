"""
Print all possible solutions for the equation: a^3 + b^3 = c^3 + d^3,
where a, b, c and d are integers between 1 and 1000.
"""

def approach1(n=1000):
    """
    Runtime is O(n^4)
    """
    for a in range(1, 1001):
        for b in range(1, 1001):
            for c in range(1, 1001):
                for d in range(1, 1001):
                    if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                        print(a,b,c,d)
                        break

def approach2(n=1000):
    """
    Runtime is O(n^3)
    """
    for a in range(1, 1001):
        for b in range(1, 1001):
            for c in range(1, 1001):
                d = round(pow(a ** 3 + b ** 3 - c ** 3, 1 / 3))
                if a ** 3 + b ** 3 == c ** 3 + d ** 3 and 0 < d < n:
                    print(a, b, c, d)
                    break

def approach3(n=1000):
    """
    Runtime is O(n^2)
    """
    hm = {}
    for a in range(1, 1001):
        for b in range(1, 1001):
            res = a**3 + b**3
            hm[res] = [a, b]
    for c in range(1, 1001):
        for d in range(1, 1001):
            res = c**3 + d**3
            if res in hm:
                print(hm[res], [c, d])
approach3()
