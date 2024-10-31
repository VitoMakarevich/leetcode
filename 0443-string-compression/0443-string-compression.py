class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("*")
        assign_pointer = 0
        cur_read_pointer = 1
        prev_char_read_pointer = 0
        prev_char = chars[0]
        while cur_read_pointer < len(chars):
            cur_char = chars[cur_read_pointer]
            if cur_char != prev_char:
                chars[assign_pointer] = prev_char
                assign_pointer += 1
                count = cur_read_pointer - prev_char_read_pointer
                if count > 1:
                    for c in str(count):
                        chars[assign_pointer] = c
                        assign_pointer += 1
                prev_char = cur_char
                prev_char_read_pointer = cur_read_pointer
            cur_read_pointer += 1
        return assign_pointer

                    