from collections import deque

from hackerrank.stack_queue_day16.deque.my_deque import Deque


def is_it_a_palindrome_1(word):
    """Define two Deques, symbols are added to the front of one Deque and to the end of another.

    At the end the Deques are compared"""
    d1 = Deque()
    d2 = Deque()
    for w in word:
        d1.add_front(w)
        d2.add_rear(w)
    if d1.items == d2.items:
        print("Word {} IS a palindrome".format(word))
    else:
        print("Word {} ISN'T a palindrome".format(word))


def is_it_a_palindrome_2(word):
    """Add symbols to the end of Deque,

    As long as the Deque's size is greater than two, remove the front-most item and the rear-most item from the deck,
    and store each of those in their own variables.
    If those two variables aren't equivalent, return false right away.
    """
    d = Deque()
    for w in word:
        d.add_rear(w)
    while d.size() >= 2:
        s1 = d.remove_rear()
        s2 = d.remove_front()
        if s1 != s2:
            print("Word {} ISN'T a palindrome".format(word))
            return
    print("Word {} IS a palindrome".format(word))


if __name__ == '__main__':
    d1 = deque()
    d2 = deque()

    d1.extend('radar')
    d2.extendleft('radar')
    print(d1 == d2)

    d1.clear()
    d2.clear()
    d1.extend('cellac')
    d2.extendleft('cellac')
    print(d1 == d2)

    is_it_a_palindrome_1("abba")
    is_it_a_palindrome_1("abbba")
    is_it_a_palindrome_1("qabbbaq")
    is_it_a_palindrome_1("qabbtaq")
    print("-*-" * 15)
    is_it_a_palindrome_2("abba")
    is_it_a_palindrome_2("abbba")
    is_it_a_palindrome_2("qabbbaq")
    is_it_a_palindrome_2("qabbtaq")
