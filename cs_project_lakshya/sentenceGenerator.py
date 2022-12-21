def generate_sentence(n):
    import nltk.corpus
    import random

    sentences = nltk.corpus.brown.sents()

    n_grams = {}

    for sentence in sentences:
        words = [word for word in sentence if word[0].isalpha()]
        for ix in range(len(words) - 1):
            try:
                n_grams[words[ix]].append(words[ix + 1])
            except KeyError as _:
                n_grams[words[ix]] = []
                n_grams[words[ix]].append(words[ix + 1])

    words = []
    next_word = random.choice(list(n_grams.keys()))
    words.append(next_word)
    while len(words) < n:
        next_word = random.choice(n_grams[next_word])
        words.append(next_word)

    # print(" ".join(words))
    return " ".join(words)
