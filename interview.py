class KeyCalculator(object):
    def __init__(self):
        self.digit_keys = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
            0: " ",
        }

    def get_digit_keys(self):
        """Return digit_keys dict to those outside this class who are interested
        
        :params: None
        """
        return self.digit_keys

    def keys_to_press(self, text):
        """This method calculates the keys to press on a mobile keypad such that
        the correct letters in the text string can be created on an output
        
        :param text str: Input to function
        """
        output = ""
        for cnt, t in enumerate(text):
            for k, v in self.digit_keys.items():
                for idx, char in enumerate(v):
                    if t == char:
                        if str(k) == output[-1:]:
                            output += ' '
                        for i in range(0, idx+1):
                            output += str(k)
                        break
        return output
