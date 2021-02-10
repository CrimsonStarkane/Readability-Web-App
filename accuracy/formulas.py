from . import util
from math import sqrt

def flesch_kin(text):
    words = util.count_words(text)
    sentences = util.count_sentences(text)
    syllables = util.text_syllables(text)

    return round(0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59)


def smog(text):
    sentences = util.count_sentences(text)
    polysyllables = util.poly_syllables(text)

    return round(1.0430 * sqrt(polysyllables * (30 / sentences)) + 3.1291)


def coleman(text):
    avg_letters_per_word = util.letters_per_word(text)
    avg_sents_per_word = util.sents_per_word(text)

    return round(0.0588 * (avg_letters_per_word * 100) - 0.296 * (avg_sents_per_word * 100) - 15.8)


def auto(text):
    characters = util.count_chars(text)
    words = util.count_words(text)
    sentences = util.count_sentences(text)

    return round(4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43)


def linsear(text):
    words = text.split()

    if len(words) < 100:
        return None

    sample_size = words[:100]
    text = " ".join(sample_size)

    easy_words = util.mono_syllables(text)
    difficult_words = util.poly_syllables(text)
    sentences = util.count_sentences(text)

    r = (easy_words + 3 * difficult_words) / sentences

    return round(r / 2 if r > 20 else r / 2 - 1)


def rix(text):
    long_words = util.count_long_words(text)
    sentences = util.count_sentences(text)

    result = long_words / sentences

    grade_levels = {
        result < 0.2: "1",
        result >= 0.2: "2",
        result >= 0.5: "3",
        result >= 0.8: "4",
        result >= 1.3: "5",
        result >= 1.8: "6",
        result >= 2.4: "7",
        result >= 3.0: "8",
        result >= 3.7: "9",
        result >= 4.5: "10",
        result >= 5.3: "11",
        result >= 6.2: "12",
        result >= 7.2: "13+"
    }

    for key, value in grade_levels.items():
        if key:
            return value