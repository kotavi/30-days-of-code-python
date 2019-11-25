"""
With try/except, you tell the python interpreter:

Try to execute a block of code, the “try” clause.
 * If the whole block of code executes without any run-time errors,
   just carry on with the rest of the program after the try/except statement.

If a run-time error does occur during execution of the block of code:
 * skip the rest of that block of code (but don’t exit the whole program)
 * execute a block of code in the “except” clause
 * then carry on with the rest of the program after the try/except statement
"""
import random
def catch_exception(x, y, lst, dict_):
    rnd = random.randrange(0, 10)
    try:
        division = y/x
        lst_value = lst[rnd]
        dict_value = dict_[rnd]
    except ZeroDivisionError:
        division = "ZeroDivisionError"
        print("Result of division {}/{}: {}".format(y, x, division))
    except IndexError:
        lst_value = "IndexError"
        print("Get value #{} from list {}: {}".format(rnd, lst, lst_value))
    except KeyError:
        print("{}, dict_[{}]: {}".format(dict_, rnd, "KeyError"))
    print("-" * 30)

catch_exception(2, 3, [], {})
catch_exception(0, 3, [1,2,3,4,5,6,7,8], {})
catch_exception(45, 3, [1,2,3,4,5,6,7,8,9,10], {1:"hello", 2: "Welcome"})