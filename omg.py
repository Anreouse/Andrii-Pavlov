import string


input_string = input("Введіть рядок: ")

translator = str.maketrans('', '', string.punctuation)
cleaned_string = input_string.translate(translator)

words = cleaned_string.split()

capitalized_words = [word.capitalize() for word in words]

hashtag = '#' + ''.join(capitalized_words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)