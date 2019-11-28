
# mutable, ordered collection of items that do not have to be of the same type
# implemented in C using a dynamic array
# Dynamic arrays use a contiguous chunk of memory
builtin_lists = [1, "Hello", "45", [0, 4.5], False, None]
print(builtin_lists)
# Dynamic arrays allow us to index directly to a slot in memory
print(builtin_lists[3]) # complexity O(1)
# Dynamic arrays allow us to append to the end of array in constant time
builtin_lists.append("The End")
print(builtin_lists)
