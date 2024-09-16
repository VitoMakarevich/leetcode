class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            j = i
            word_count = 0
            words_size = 0
            while j < len(words) and self.min_size(words_size + len(words[j]), word_count + 1) <= maxWidth:
                words_size += len(words[j])
                word_count += 1
                j += 1

            if j == len(words):
                res.append(" ".join(words[i:j]).ljust(maxWidth))
            elif word_count == 1:
                res.append(words[i].ljust(maxWidth))
            else:
                number_of_spaces_in_line = maxWidth - words_size
                number_of_breaks = word_count - 1
                space_multiplier = floor(number_of_spaces_in_line / number_of_breaks)
                remainder = number_of_spaces_in_line % number_of_breaks
                from io import StringIO

                tmp_res = StringIO()
                for k in range(word_count + number_of_breaks):
                    if (k % 2) == 0:
                        tmp_res.write(words[i + int(k / 2)])
                    else:
                        if remainder > 0:
                            tmp_res.write(" " * (space_multiplier + 1))
                            remainder -= 1
                        else:
                            tmp_res.write(" " * space_multiplier)

                result = tmp_res.getvalue()
                tmp_res.close() 
                res.append(result)
            i = j
        return res
                    

    def min_size(self, words_length, word_count):
        return words_length + word_count - 1


                 