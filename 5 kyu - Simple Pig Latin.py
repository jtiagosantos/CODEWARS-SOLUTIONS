'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''

letters = "abcdefghijklmnopqrstuvwxyz"
def pig_it(text):
    new_text = []
    for i in text.split():
        i = list(i)
        if i[0].lower() in letters:
            first_letter = i.pop(0)
            i.append(first_letter)
            i.append('ay')
            new_text.append(''.join(i))
        else:
            new_text.append(i[0])
    return ' '.join(new_text)