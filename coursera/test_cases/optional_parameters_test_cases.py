import unittest


class TestCases(unittest.TestCase):

    def sort_a_list(self, lst, rev=False):
        return sorted(lst, reverse=rev)

    """
    Testing Optional Parameters
    """
    def sort_a_list_test_1(self):
        expected_result = []
        actual_result = self.sort_a_list([])
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def sort_a_list_test_2(self):
        expected_result = [1]
        actual_result = self.sort_a_list([1])
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def sort_a_list_test_3(self):
        expected_result = [-5, -2, 0, 1, 2, 3]
        actual_result = self.sort_a_list([1, 0, 3, -2, -5, 2])
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def sort_a_list_test_4(self):
        expected_result = [-5, -2, 0, 1, 2, 3]
        actual_result = self.sort_a_list([1, 0, 3, -2, -5, 2], False)
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def sort_a_list_test_5(self):
        expected_result = [3, 2, 1, 0, -2, -5]
        actual_result = self.sort_a_list([1, 0, 3, -2, -5, 2], True)
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def sort_a_list_test_6(self):
        expected_result = [3, 2, 1, 0, -2, -5]
        actual_result = self.sort_a_list([1, 0, 3, -2, -5, 2], 1)
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))


if __name__ == '__main__':
    unittest.main()
