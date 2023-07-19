def ToggleCase(string):
    string=[i for i in string]
    for i in range(len(string)):
        string[i]=chr(ord(string[i])^(1<<5))
    return ''.join(string)
print(ToggleCase(input()))

"""
Toggle Case
You are given a character string A having length N, consisting of only lowercase and uppercase latin letters.

You have to toggle case of each character of string A. For e.g 'A' is changed to 'a', 'e' is changed to 'E', etc.

Example Input

Input 1:

A = "Hello"
Input 2:

A = "tHiSiSaStRiNg"


Example Output

Output 1:

hELLO
Output 2:

ThIsIsAsTrInG
"""
