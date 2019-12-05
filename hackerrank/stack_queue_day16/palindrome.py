class Solution:
    def __init__(self):
        self.stack_items = []
        self.queue_items = []

    def push_character(self, ch):
        self.stack_items.append(ch)

    def pop_character(self):
        if self.stack_items:
            return self.stack_items.pop()
        return None

    def enqueue_character(self, ch):
        self.queue_items.insert(0, ch)

    def dequeue_character(self):
        return self.queue_items.pop()


if __name__ == '__main__':
    s = input("Enter a word: ")
    obj = Solution()

    l = len(s)
    # push/enqueue all the characters of string s to stack
    for i in range(l):
        obj.push_character(s[i])
        obj.enqueue_character(s[i])

    isPalindrome = True
    '''
    pop the top character from stack
    dequeue the first character from queue
    compare both the characters
    '''
    for i in range(l // 2):
        if obj.pop_character() != obj.dequeue_character():
            isPalindrome = False
            break
    # finally print whether string s is palindrome or not.
    if isPalindrome:
        print("The word, " + s + ", is a palindrome.")
    else:
        print("The word, " + s + ", is not a palindrome.")
