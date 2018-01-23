def is_palindrome(word):
    for i in range(len(word) / 2):
        if word[i] != word[-1 - i]:
            return False

    return True


if __name__ == '__main__':
    print(is_palindrome(''))
    print(is_palindrome('racecar'))
    print(is_palindrome('cake'))
    print(is_palindrome('ana'))
    print(is_palindrome('cckkcc'))
