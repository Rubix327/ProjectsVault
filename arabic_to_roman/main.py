import unittest

arabic = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}


def calculate_arabic(num):
    roman_string = ""
    while num != 0:
        for key, value in arabic.items():
            if num / key >= 1:
                num -= key
                roman_string += value
                break

    return roman_string


class TestRoman(unittest.TestCase):

    def test1(self):
        self.run_test("VI", 6)

    def test2(self):
        self.run_test("CCCXLIV", 344)

    def test3(self):
        self.run_test("LXXXI", 81)

    def test4(self):
        self.run_test("XCIX", 99)

    def run_test(self, rom, arabic):
        self.assertEqual(rom, calculate_arabic(arabic))
        print(f"Arabic number %s is a roman number %s" % (rom, arabic))


if __name__ == '__main__':
    unittest.main()
