"""
WAP to count and display the no. of vovels,consonant,upper case,lower case &
characters in string.
"""
s = str(input("Enter a word: "))
ucase,lcase,vowel,consonant = 0,0,0,0
for ch in s:
    if ch>= 'A' and ch<= 'Z':
        ucase += 1
    if ch>= 'a' and ch<= 'z':
        lcase += 1
for ch in s:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'
       or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        vowel += 1
    else:
        consonant += 1

print("No. of capital letters: ",ucase)
print("No. of small letters: ",lcase)
print("No. of vowels: ",vowel)
print("No. of consonants: ",consonant)
