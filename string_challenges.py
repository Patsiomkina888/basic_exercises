# Вывести последнюю букву в слове
word = "Архангельск"


def last_letter(word):
    list_of_words = word.split()
    return list_of_words[0][-1]


print(last_letter(word))


def last_letter_another(word):
    char_list = list(word)

    return char_list[-1]


print(last_letter_another(word))

# Вывести количество букв "а" в слове
word = "Архангельск"


def letter_counting(word, letter):
    word_lower = word.lower()
    return word_lower.count(letter)


print(letter_counting("Архангельск", "а"))


# Вывести количество гласных букв в слове
word = "Архангельск"


def vowels_quantity(word):
    count = 0
    word_lower = word.lower()
    for i in word_lower:
        if i in ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"]:
            count += 1

    return count


print(vowels_quantity(word))


# Вывести количество слов в предложении
sentence = "Мы приехали в гости"


def words_quntity(sentence):
    list_of_words = sentence.split()
    return len(list_of_words)


print(words_quntity(sentence))


# Вывести первую букву каждого слова на отдельной строке
sentence = "Мы приехали в гости"


def first_word_letter(sentence):
    list_of_words = sentence.split()
    for word in list_of_words:
        print(word[0])


first_word_letter(sentence)

# Вывести усреднённую длину слова в предложении
sentence = "Мы приехали в гости"


def sentence_avg(sentence):
    list_of_words = sentence.split()
    list_of_length = []
    sum_of_numbers = 0
    for word in list_of_words:
        word_length = len(word)
        list_of_length.append(word_length)

    for number in list_of_length:
        sum_of_numbers += number
    return sum_of_numbers / len(list_of_length)


print(sentence_avg(sentence))
