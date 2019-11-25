import unittest

class TestCases(unittest.TestCase):

    def blanked(self, word, revealed_letters):
        result_string = ''
        for a_letter in word:
            if a_letter in revealed_letters:
                result_string += a_letter
            else:
                result_string += '_'
        return result_string

    """
    Return value test cases
    """
    def blanked_test_1(self):
        expected_result = "u_d__"
        actual_result = self.blanked("under", "ud")
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def blanked_test_2(self):
        expected_result = "pr__r_ss___"
        actual_result = self.blanked("progressive", "prs")
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def blanked_test_3(self):
        expected_result = "_e__e_e__a_i_e"
        actual_result = self.blanked("representative", "iouea")
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def blanked_test_4(self):
        expected_result = "______"
        actual_result = self.blanked("family", "")
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def blanked_test_5(self):
        expected_result = "______"
        actual_result = self.blanked("family", "qwrto")
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))

    def blanked_test_6(self):
        expected_result = "present"
        actual_result = self.blanked("present", "plareysevnt")
        self.assertEqual(expected_result, actual_result, "Test Failed: expected '{}' but got '{}'"
                         .format(expected_result, actual_result))



if __name__ == '__main__':
    unittest.main()
