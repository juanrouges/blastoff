vowel = ['a', 'e', 'i', 'o', 'u']

def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    string = phrase.lower()
    result = {}

    for i in vowel:
        if string.count(i):
            result[i] = string.count(i)
        
    return result