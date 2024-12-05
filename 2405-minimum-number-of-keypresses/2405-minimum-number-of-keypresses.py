class Solution:
    def minimumKeypresses(self, s: str) -> int:
        press_price = 1
        current_assignable = 1
        counts = Counter(s)
        sorted_counts = sorted(counts.values(), reverse = True)
        press_count = 0
        for amount in sorted_counts:
          press_count += amount * press_price
          current_assignable += 1
          if current_assignable == 10:
            current_assignable = 1
            press_price += 1
        return press_count