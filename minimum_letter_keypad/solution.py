from collections import Counter
from collections import OrderedDict

def minimum_pushes(word):

    # Replace this placeholder return statement with your code
    word_count = Counter(word)
    ordered_letters = OrderedDict(sorted(dict(word_count).items(), key=lambda item: -item[1]))
    count = 0
    letter_weight = 1
    for index, v in enumerate(ordered_letters.values()):
        letter_weight = (index // 8) + 1
        for i in range(v):
            count = count + 1 * letter_weight
    return count
