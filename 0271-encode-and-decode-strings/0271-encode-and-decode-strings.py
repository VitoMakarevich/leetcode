class Codec:
    LENGTH_CHARS = 3
    ARRAY_LENGTH_CHARS = 5
    HEADER_SIZE = 9
    SPLIT = "|"
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        length = str(len(strs)).zfill(Codec.LENGTH_CHARS)
        each_count = Codec.SPLIT.join([str(len(item)) for item in strs])
        count_length = str(len(each_count)).zfill(Codec.ARRAY_LENGTH_CHARS)
        header = f"{length}{Codec.SPLIT}{count_length}"
        content = "".join(strs)
        message = f"{header}{each_count}{content}"
        return message


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        header = s[0:Codec.HEADER_SIZE]
        array_len_str, count_len_str = header.split(Codec.SPLIT)
        array_len, count_len = int(array_len_str), int(count_len_str)
        counts = s[Codec.HEADER_SIZE:Codec.HEADER_SIZE + count_len]
        lengths = counts.split(Codec.SPLIT)
        data_pointer = Codec.HEADER_SIZE + count_len
        
        res = [""] * array_len
        for idx, l in enumerate(lengths):
          l = int(l)
          item = s[data_pointer: data_pointer + l]
          data_pointer = data_pointer + l 
          res[idx] = item
        return res

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))