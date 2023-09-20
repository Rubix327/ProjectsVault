import unittest


def format_string(string):
    return (string.replace(",", "")
            .replace(" ", "")
            .replace("!", "")
            .replace("?", "")
            .lower())


def palindrome1(string):
    string = format_string(string)
    if string == string[::-1]:
        return True
    return False


def palindrome2(string):
    string = format_string(string)
    length = len(string)
    for i in range(length):
        if string[i] != string[length-1-i]:
            return False
    return True


class TestRoman(unittest.TestCase):

    def test1(self):
        self.run_test("Лёша на полке клопа нашёл")

    def test2(self):
        self.run_test("Молебен о коне белом")

    def test3(self):
        self.run_test("Учуя молоко, я около мяучу")

    def test4(self):
        self.run_test("Искать такси")

    def run_test(self, message):
        self.assertTrue(palindrome1(message))
        self.assertTrue(palindrome2(message))
        print(f"String '%s' is a palindrome!" % message)


if __name__ == '__main__':
    unittest.main()

