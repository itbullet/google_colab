from nltk import word_tokenize, pos_tag

sentence = str(input())  # input sentence
tagged = pos_tag(word_tokenize(sentence))
# tags = ['VB', 'VBD', 'VBN', 'VBP', 'VBZ']
verbs = [word for word, pos in tagged if pos.startswith('VB')]
# verbs = list(filter(lambda x: x[1].startswith('VB'), tagged))
# verbs = list(filter(lambda x: re.match('VB.?|MD', x[1]), tagged))
print(verbs)
