import unittest


def is_valid(s):
    if len(s) % 2 != 0:
        return False
    couples = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    stack = []
    for i in s:
        if i in couples.keys():
            stack.append(i)
        else:
            if not stack:
                return False
            a = stack.pop()
            if i != couples[a]:
                return False
    return stack == []


class TestCases(unittest.TestCase):

    def test1(self):
        self.assertTrue(is_valid("()"))

    def test2(self):
        self.assertTrue(is_valid("()[]{}"))

    def test3(self):
        self.assertFalse(is_valid("(]"))

    def test4(self):
        self.assertTrue(is_valid("([{()}])"))

    def test5(self):
        self.assertFalse(is_valid("([{])}"))


if __name__ == '__main__':
    unittest.main()