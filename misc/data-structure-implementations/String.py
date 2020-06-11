"""
Implementation of String class. Methods based on the JavaDoc implementation: https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"""
import unittest

class String:

    def __init__(self, input_string = None):
        if input_string is None:
            self._char_list = list()
        else:
            self._char_list = list(input_string)

    def char_at(self, index):
        self.__check_index(index)
        return self._char_list[index]

    def code_point_at(self, index):
        """
        Returns unicode integer representation.
        """
        return ord(self.char_at(index))

    def code_point_before(self, index):
        return self.code_point_at(index - 1)

    def code_point_count(self, start, end):
        self.__check_index(start)
        self.__check_index(end)
        return len(set([self.code_point_at(i) for i in range(start, end)]))

    def compare_to(self, another):
        """
        Compares the two strings lexographically.
        If they are the same, it returns 0.
        If the other string comes after, it returns a negative number.
        If the other string comes before, it returns a positive number.
        https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#compareTo(java.lang.String)
        """
        if self.is_empty() and another.is_empty():
            return 0
        elif another.is_empty():
            return self.code_point_at(0)
        elif self.is_empty():
            return -another.code_point_at(0)
        elif self.length() == another.length():
            if self.equals(another):
                return 0
            else:
                return self.length() - another.length()
        if self.length() < another.length():
            return self.__compare_to(self._char_list, another._char_list)
        else:
            return -self.__compare_to(another._char_list, self._char_list)


    @staticmethod
    def __compare_to(shorter, longer):
        if len(shorter) > len(longer):
            raise AssertionError("shorter must have less characters than longer")
        for i in range(len(shorter)):
            if ord(shorter[i]) != ord(longer[i]):
                return ord(shorter[i]) - ord(longer[i])
        return len(shorter) - len(longer)


    def equals(self, another):
        if self.is_empty() and another.is_empty():
            return True
        elif self.is_empty() or another.is_empty():
            return False
        elif self.length() != another.length():
            return False
        for i, j in zip(self._char_list, another.get_string()):
            if ord(i) != ord(j):
                return False
        return True

    def get_string(self):
        """
        toString
        """
        return "".join(self._char_list)

    def is_empty(self):
        return len(self._char_list) == 0

    def length(self):
        return len(self._char_list)

    def __check_index(self, index):
        if index >= len(self._char_list) or index < 0:
            raise IndexError()



class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.std_string = String(" Standard String ")

    def test_char_at(self):
        self.assertEqual(self.std_string.char_at(1), 'S')

    def test_code_point_at(self):
        self.assertEqual(self.std_string.code_point_at(1), 83)

    def test_code_point_before(self):
        self.assertEqual(self.std_string.code_point_before(1), 32)

    def test_code_point_count(self):
        self.assertEqual(self.std_string.code_point_count(1, 11), 7)

    def test_compare_to1(self):
        self.assertEqual(self.std_string.compare_to(String("")), 32)

    def test_compare_to2(self):
        self.assertEqual(String("123456").compare_to(String("1")), 5)

    def test_compare_to2(self):
        self.assertEqual(String("1").compare_to(String("123456")), -5)

if __name__ == '__main__':
    unittest.main()
