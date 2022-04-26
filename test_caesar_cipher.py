from unittest import TestCase

import caesar_cipher


class Test(TestCase):
    def test_cipher(self):
        result1 = caesar_cipher.cipher("Hello", 5, "e")
        result2 = caesar_cipher.cipher("civilization", 189, "e")
        result3 = caesar_cipher.cipher("jpcpspghapvu", 189, "d")
        assert result1 == "Mjqqt"
        assert result2 == "jpcpspghapvu"
        assert result3 == "civilization"
