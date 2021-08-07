'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''

from string import punctuation
def pig_it(text: str) -> str:
    ans = [i[1:] + i[0] + 'ay' if i not in punctuation else i for i in text.split(' ')]
    return ' '.join(ans)

print(pig_it('Hello world !'))

'''
-----BEST PRACTICES-----
#1
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
'''