from collections import deque, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        word_dict = defaultdict(int)
		
        for word in words:
            word_dict[word] += 1

        total_length = len(words) * word_length
        res = []
        for i in range(word_length):
            queue = deque()
            word_dict_current = word_dict.copy()
            for j in range(i, len(s) - word_length + 1, word_length):
                word = s[j : j + word_length]
                if word_dict_current.get(word, 0) != 0:
                    word_dict_current[word] -= 1
                    queue.append(word)
                    if sum(word_dict_current.values()) == 0:
                        res.append(word_length + j - total_length)
                        first_word = queue.popleft()
                        word_dict_current[first_word] += 1
                else:
                    while queue:
                        first_word = queue.popleft()
                        if first_word == word:
                            queue.append(word)
                            break
                        else:
                            word_dict_current[first_word] = word_dict_current.get(first_word, 0) + 1
                            if word_dict_current[first_word] > word_dict[first_word]:
                                word_dict_current = word_dict.copy()

        return res