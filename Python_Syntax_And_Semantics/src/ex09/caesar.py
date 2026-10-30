import sys


def is_cyrillic(s):
    for ch in s:
        if "А" <= ch <= "Я" or "а" <= ch <= "я" or ch == "Ё" or ch == "ё":
            return True
    return False


def shift_char(c, shift):
    if "a" <= c <= "z":
        return chr((ord(c) - ord("a") + shift) % 26 + ord("a"))
    if "A" <= c <= "Z":
        return chr((ord(c) - ord("A") + shift) % 26 + ord("A"))
    return c


def caesar(text, shift):
    return "".join(shift_char(ch, shift) for ch in text)


def main():
    if len(sys.argv) != 4:
        raise Exception("Incorrect number of arguments")

    mode = sys.argv[1].lower()
    text = sys.argv[2]
    shift_str = sys.argv[3]

    if not shift_str.lstrip("-").isdigit():
        raise Exception("Shift must be an integer")
    shift = int(shift_str)

    if is_cyrillic(text):
        raise Exception("The script does not support your language yet.")

    if mode == "encode":
        result = caesar(text, shift)
    elif mode == "decode":
        result = caesar(text, -shift)
    else:
        raise Exception("Mode must be 'encode' or 'decode'")

    print(result)


if __name__ == "__main__":
    main()
