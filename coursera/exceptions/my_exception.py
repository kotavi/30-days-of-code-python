class Calculator:

    def power_(self, int1,int2):
        if int1 < 0 or int2 < 0:
            raise Exception("n and p should be non-negative")
        return int1**int2

myCalculator=Calculator()
pairs = [(2, 3), (-1, 2), (4, -5), (6, 7)]
for i in range(len(pairs)):
    n,p = pairs[i]
    try:
        ans=myCalculator.power_(n,p)
        print("{}: {}".format((n, p), ans))
    except Exception as e:
        print(e)