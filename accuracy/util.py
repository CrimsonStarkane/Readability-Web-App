import re
import string

vowels = ['a', 'e', 'i', 'o', 'u', 'y', '&']
diphthongs = ['ou', 'ie', 'oi', 'oo', 'ee', 'ea', 'ai', 'ei', 'oe']
triphthong = 'eau'

def word_syllables(word):
    syllables = 0

    word = word.strip(string.punctuation).casefold()

    word_len = len(word)
    diphthongs_re = diphthongs[:]

    for letter in word:
        if letter in vowels:
            syllables += 1

    if triphthong in word:
        syllables -= 2
        diphthongs_re.remove('ea')

    if 'oi' in word and word.endswith('ing'):
        diphthongs_re.remove('oi')

    for diphthong in diphthongs_re:
        if diphthong in word:
            syllables -= 1

    if 'io' in word and word_len > 4:
        syllables -= 1

    if (word.endswith('le') or word.endswith('les')) and word[word.rfind('l') - 1] in vowels:
        syllables -= 1
    elif word.endswith('e') and word_len > 2:
        if word_len == 3:
            if word[0] in vowels:
                syllables -= 1
        else:
            syllables -= 1

    if word.endswith('ed'):
        if not word[word.rfind('e') - 1] in ['o', 'e', 'i'] and (word_len == 4 and word[0] in vowels or word_len > 4):
            syllables -= 1

    indexes = [pos for pos, char in enumerate(word) if char == 'y']

    if word != "" and word[0] == 'y':
        syllables -= 1
        indexes.remove(0)

    for index in indexes:
        if word[index - 1] in vowels or index < word_len - 1 and word[index + 1] in vowels:
            syllables -= 1
    
    return syllables


def text_syllables(text):
    counter = 0

    for word in text.split():
        counter += word_syllables(word)

    return counter


def mono_syllables(text):
    counter = 0

    for word in text.split():
        if word_syllables(word) <= 2:
            counter += 1
    
    return counter


def poly_syllables(text):
    counter = 0

    for word in text.split():
        if word_syllables(word) >= 3:
            counter += 1
    
    return counter

def is_word(word):
    word = word.casefold()

    if word == '&':
        return True

    for char in word:
        if char.isalpha():
            return True

    return False

def count_words(text):
    words = text.split()

    for word in words:
        if not is_word(word):
            words.remove(word)
    
    return len(words)


def count_long_words(text):
    pattern = re.compile("[" + re.escape(string.punctuation) + "]")
    text = pattern.sub("", text)

    words = text.split()
    counter = 0

    for word in words:
        if len(word) > 6:
            counter += 1

    return counter


def count_sentences(text):
    return len(re.split("[.] |[?] |[!] |[.]\r|[?]\r|[!]\r", text))


def count_letters(text):
    letters = 0

    for char in text:
        if char.isalpha():
            letters += 1

    return letters


def count_chars(text):
    return len(''.join(text.split()))


def letters_per_word(text):
    return count_letters(text) / count_words(text)


def sents_per_word(text):
    return count_sentences(text) / count_words(text)