class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        pass_idx = 0
        passenger_set = set(passengers)

        for bus in buses:
            count = 0
            while pass_idx < len(passengers) and passengers[pass_idx] <= bus and count < capacity:
                pass_idx += 1
                count += 1

        if count < capacity:
            candidate = buses[-1]
        else:
            candidate = passengers[pass_idx - 1] - 1

        while candidate in passenger_set:
            candidate -= 1

        return candidate
