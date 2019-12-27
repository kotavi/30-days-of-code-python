import os
from os.path import join, getsize

path = os.path.dirname(os.path.abspath(__file__))
print(os.getcwd())
print("-*" * 60, "-")
print(os.path.exists(path))
print("-*" * 60, "-")
for root, dirs, files in os.walk(path):
    print(root, "consumes", end=" ")
    print(sum([getsize(join(root, name)) for name in files]), end=" ")
    print("bytes in", len(files), "non-directory files")
    # if 'CVS' in dirs:
    #     dirs.remove('CVS')  # don't visit CVS directories

print("-*" * 60, "-")
print([x[0] for x in os.walk(path)])
print("-*" * 60, "-")

def dig_deep(paths_lst):
    """
    http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html
    """
    if not paths_lst:
        return
    print(paths_lst[-1])
    paths_lst.pop()
    try:
        dig_deep(paths_lst)
    except RecursionError as e:
        print(e)


paths = [x[0] for x in os.walk(path)]
print(len(paths))
dig_deep(paths)