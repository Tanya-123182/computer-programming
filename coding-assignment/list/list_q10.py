#Word Ladder

from collections import deque
def word_ladder(begin_word, end_word, word_list):
    if end_word not in word_list:
        return 0
    word_list = set(word_list)
    queue = deque([(begin_word, 1)])
    while queue:
        word, length = queue.popleft()
        if word == end_word:
            return length
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + char + word[i+1:]
                if new_word in word_list:
                    word_list.remove(new_word)
                    queue.append((new_word, length + 1))
    return 0
