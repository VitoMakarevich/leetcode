from math import ceil

class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:
            return 1

        bit_count = n.bit_length()

        res = 1
        for i in range(1, bit_count):
            res += 2 ** (ceil(i / 2) - 1)

        half_len = (bit_count + 1) // 2
        bits = bin(n)[2:]
        prefix_bits = bits[:half_len]
        prefix = int(prefix_bits, 2)

        res += prefix - (1 << (half_len - 1))

        prefix_bin = prefix_bits.zfill(half_len)
        if bit_count % 2 == 0:
            pal = int(prefix_bin + prefix_bin[::-1], 2)
        else:
            pal = int(prefix_bin + prefix_bin[:-1][::-1], 2)

        if pal <= n:
            res += 1

        return res
