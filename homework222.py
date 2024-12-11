def correct_sentence(input_string: str) -> str:

    sentences = input_string.split('. ')
    corrected_sentences = []
    for sentence in sentences:

        sentence = sentence.strip()
        if sentence:
            corrected_sentence = sentence[0].upper() + sentence[1:]

            if not corrected_sentence.endswith('.'):
                corrected_sentence += '.'

            corrected_sentences.append(corrected_sentence)

    return ' '.join(corrected_sentences)

input_string = "привет, как дела? надеюсь, у тебя все хорошо. "
print(correct_sentence(input_string))