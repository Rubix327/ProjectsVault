import unittest

roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def calculate_roman(number):
    i = 0
    counter = 0

    while i < len(number):
        current_num = roman.get(number[i])

        if i + 1 != len(number):
            next_num = roman.get(number[i + 1])

            if next_num > current_num:
                counter += next_num - current_num
                i += 2
                continue

        counter += current_num

        i += 1

    return counter


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
        self.assertEqual(calculate_roman(rom), arabic)
        print(f"Roman number %s is an arabic number %s" % (rom, arabic))


if __name__ == '__main__':
    unittest.main()
