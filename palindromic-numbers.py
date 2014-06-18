

"""Problem from http://www.problemotd.com/problem/palindromic-numbers/. Check if numbers are palindromes or not without using string or array operations."""

def get_place_values(num):
    place_vals = []
    i = 1
    while True:
        q, r = divmod(num, 10**i)
        q1, r1 = divmod(r, 10**(i-1))
        place_vals.append(q1)
        if (r == num):
            break
        i += 1
    return place_vals

def is_palindrome(num):
    """The idea is to figure out the digits in the number from both directions using divmod on powers of 10. Once we get the corresponding digits, we compare and return False on mismatch."""
    MAX_NUM_DIGITS = 1

    while True:
        q, r = divmod(num, 10**MAX_NUM_DIGITS)
        if q == 0:
            break
        MAX_NUM_DIGITS += 1

    for i in range(1, MAX_NUM_DIGITS+1):
        q, r = divmod(num, 10**i)
        q1, r1 = divmod(r, 10**(i-1))
        
        ql, rl = divmod(num, 10**(MAX_NUM_DIGITS-i+1))
        ql1, rl1 = divmod(rl, 10**(MAX_NUM_DIGITS-i))
        if (q1 != ql1):
            return False

    return True


if __name__ == '__main__':
    print is_palindrome(123321)
    print is_palindrome(123456)
    print is_palindrome(987656789)
    print is_palindrome(99887766778899)
    print is_palindrome(1123455091019)

