class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
      self.food_version = {food: 0 for food in foods}
      self.cuisine_rating = {}
      self.food_to_cuisine = {}
      for food, cuisine, rating in zip(foods, cuisines, ratings):
        self.food_to_cuisine[food] = cuisine
        if not cuisine in self.cuisine_rating:
          self.cuisine_rating[cuisine] = []
        heapq.heappush(self.cuisine_rating[cuisine], (-rating, food, 0))

    def changeRating(self, food: str, newRating: int) -> None:
      cuisine = self.food_to_cuisine[food]
      self.food_version[food] += 1
      heapq.heappush(self.cuisine_rating[cuisine], (-newRating, food, self.food_version[food]))

    def highestRated(self, cuisine: str) -> str:
      biggest_rating, food, version = self.cuisine_rating[cuisine][0]

      while self.food_version[food] != version:
        heapq.heappop(self.cuisine_rating[cuisine])
        biggest_rating, food, version = self.cuisine_rating[cuisine][0]

      return food
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)