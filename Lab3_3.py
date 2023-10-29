def count_letters(text):
    letter_counts = {}
    for letter in text:
        if letter.isalpha() and letter.islower():
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    return letter_counts

def calculate_frequency(letter_counts):
    total_count = sum(letter_counts.values())
    frequency_dict = {}
    for letter in letter_counts:
        frequency_dict[letter] = round(letter_counts[letter] / total_count, 2)
    return frequency_dict

text = "Какое-то очень умное предложения для подсчета частотности буков в нём"
letter_counts = count_letters(text)
frequency_dict = calculate_frequency(letter_counts)

for letter in frequency_dict:
    print(letter + ": " + str(frequency_dict[letter]))