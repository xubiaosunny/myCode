"""
This mission is the part of the set. Another one - Caesar cipher decriptor.

Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.) using Caesar cipher where each letter of input text is replaced by another that stands at a fixed distance. For example ("a b c", 3) == "d e f"

!()[https://d17mnqrx9pmt3e.cloudfront.net/media/missions/media/4732ed3675884800a345142a7d3607ba/drawing.png]

Input: A secret message as a string (lowercase letters only and white spaces)

Output: The same string, but encrypted

Example:

to_encrypt("a b c", 3) == "d e f"
to_encrypt("a b c", -3) == "x y z"
to_encrypt("simple text", 16) == "iycfbu junj"
to_encrypt("important text", 10) == "swzybdkxd dohd"
to_encrypt("state secret", -13) == "fgngr frperg"

How it is used: For cryptography and to save important information.

Precondition:
0 < len(text) < 50
-26 < delta < 26
"""
def to_encrypt(text, delta):
    result = ''
    for t in text:
        _t = ord(t)
        if 97 <= _t <= 122:
            _d = _t + delta
            if _d < 97:
                result += chr(122 + 1 - (97 - _d))
            elif _d > 122:
                result += chr(97 - 1 + _d - 122)
            else:
                result += chr(_d)
        else:
            result += t
    return result

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")