# Step 1: Tokenize text into lowercase words
def tokenize(text):
    return text.lower().split()
    pass

# Step 2: Build vocabulary from list of texts
def build_vocab(texts):
    vocab = {}
    idx = 1
    for text in texts:
        for word in tokenize(text):
            if word not in vocab:
                vocab[word] = idx
                idx += 1
    return vocab
    pass

# Step 3: Convert text to sequence of word indices, pad/truncate to fixed length
def text_to_sequence(text, vocab, max_len):
    seq = [vocab.get(word, 0) for word in tokenize(text)]
    if len(seq) < max_len:
        seq += [0] * (max_len - len(seq))
    else:
        seq = seq[:max_len]
    return seq
    pass

# Example test cases:
example_text = "Hello World!"
print(tokenize(example_text))

texts = ["Hello world", "world of NLP"]
vocab = build_vocab(texts)
print(vocab)

seq = text_to_sequence("Hello NLP", vocab, 4)
print(seq)
