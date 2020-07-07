import unittest


def from_binary(b_number):
    """

    :param b_number: binary number, for example: 11100
    :return: integer number
    """
    negative_number_error = "Number cannot be negative"
    not_0_or_1_error = "Binary number should contain only 1 and 0"
    if type(b_number) is str:
        if '-' in b_number:
            return negative_number_error
    if type(b_number) is int and  b_number < 0:
        return negative_number_error
    digits = "23456789"
    str_number = str(b_number)
    for d in str_number:
        if d in digits:
            return not_0_or_1_error
    result = 0
    k = 0
    i = len(str_number) - 1
    while i >= 0:
        result += 2 ** k * int(str_number[i])
        k += 1
        i -= 1
    return result


class TestCases(unittest.TestCase):

    """
    Testing Conditionals and Loops
    """

    def from_binary_test_1(self):
        expected_result = 0
        actual_result = from_binary(00000)
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def from_binary_test_2(self):
        expected_result = 0
        actual_result = from_binary("0000")
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def from_binary_test_3(self):
        expected_result = 1
        actual_result = from_binary("00001")
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def from_binary_test_4(self):
        expected_result = 255
        actual_result = from_binary(11111111)
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def from_binary_test_5(self):
        expected_result = 0
        actual_result = from_binary("")
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def from_binary_test_6(self):
        expected_result = "Number cannot be negative"
        actual_result = from_binary(-11)
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def from_binary_test_7(self):
        expected_result = "Binary number should contain only 1 and 0"
        actual_result = from_binary("1141")
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def from_binary_test_8(self):
        expected_result = 429
        actual_result = from_binary("110101101")
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))


if __name__ == '__main__':
    unittest.main()
