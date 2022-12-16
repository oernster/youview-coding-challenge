from __future__ import print_function

import sys

from interview import KeyCalculator
from fixtures import TESTS


class TestHandler(object):
    def __init__(self):
        self.KC = KeyCalculator()
        
    def run_test(self, input_text):
        """Test harness for `keys_to_press`.

        :param input_text str: Input to function
        """
        expected_output = TESTS.get(input_text)
        print(f'Input :          {input_text}')
        print(f'Expected Output: {expected_output}')
        output = self.KC.keys_to_press(input_text)
        print('Output:          {output}')
        passed = output == expected_output
        if passed:
            print("PASS")
        else:
            print("!!! ERROR")
        return passed


if __name__ == '__main__':
    TH = TestHandler()
    if len(sys.argv) > 1:
        TH.run_test(sys.argv[1])
    else:
        passed_count = 0
        for input_text in TESTS:
            print("=" * 10)
            if TH.run_test(input_text):
                passed_count += 1
        print(f"{passed_count} of {len(TESTS)} tests passed")
