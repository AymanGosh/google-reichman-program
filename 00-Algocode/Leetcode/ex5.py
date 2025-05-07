def longestPalindrome(s: str) -> str:
    longest_pali = ""

    def get_longest_palindrom(l, r):
        nonlocal longest_pali
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # Extract the valid palindrome (after breaking the loop)
        pali = s[l+1:r]
        if len(pali) > len(longest_pali):
            longest_pali = pali

    for i in range(len(s)):
        get_longest_palindrom(i, i)     # Odd-length palindrome
        get_longest_palindrom(i, i + 1) # Even-length palindrome

    return longest_pali

# Test the function
print(longestPalindrome("abbaba"))  # Output: "aba"
