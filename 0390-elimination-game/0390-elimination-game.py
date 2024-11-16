class Solution:
    def lastRemaining(self, n: int) -> int:
        vector = range(1, n + 1)
        start_left = True
        while len(vector) != 1:
            subrange = None
            if start_left:
                subrange = vector[1::2]
            elif len(vector) % 2 == 0:
                subrange = vector[::2]
            else:
                subrange = vector[1::2]
            start = subrange.start
            stop = subrange.stop
            step = subrange.step

            new_range = range(start, stop, step)
            start_left = not start_left
            vector = new_range
        return vector[0]


