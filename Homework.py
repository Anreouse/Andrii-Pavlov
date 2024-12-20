def popular_words(text, words):
    text = text.lower()
    word_list = text.split()

    result = {}

    for word in words:
        count = word_list.count(word)
        result[word] = count

    return result

    text = '''The quick brown fox jumps over the lazy dog. The dog barked.'''
    words = ['the', 'dog', 'fox', 'cat']
    assert popular_words(text, words) == {'the': 2, 'dog': 2, 'fox': 1, 'cat': 0}