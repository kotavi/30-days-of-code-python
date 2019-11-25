import unittest

class TestCases(unittest.TestCase):

    def update_counts(self, letters, letters_count_dict):
        for a_letter in letters:
            if a_letter in letters_count_dict:
                letters_count_dict[a_letter] += 1
            else:
                letters_count_dict[a_letter] = 1
        return letters_count_dict

    """
    Side effect test cases
    """
    def update_counts_test_1(self):
        expected_result = {'a': 3, 'n': 3, 'u': 1, 'd': 1, 'e': 1, 'r': 1}
        actual_result = self.update_counts("under", {'a': 3, 'n': 2})
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def update_counts_test_2(self):
        expected_result = {'a': 7, 'n': 8}
        actual_result = self.update_counts("aaaannnnn", {'a': 3, 'n': 3})
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))


    def update_counts_test_3(self):
        expected_result = {'a': 4, 'n': 5}
        actual_result = self.update_counts("aaaannnnn", {})
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def update_counts_test_4(self):
        expected_result = {}
        actual_result = self.update_counts("", {})
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def update_counts_test_5(self):
        expected_result = {'a': 257, 'b': 257}
        actual_result = self.update_counts("a"*257 + "b" * 257, {})
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))




if __name__ == '__main__':
    unittest.main()
