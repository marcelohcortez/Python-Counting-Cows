class Counting_Cows:
   
    def cows_number(self, year: int) -> int:
      if year < 0:
        return -1
      elif year >= 0 and year <= 2:
        return 1
      else:
        return year -1

    def get_total(self, year: int) -> int:
      total = 0
      i = 0
      for i in range(year):
        total += self.cows_number(i)

      print(total)

count = Counting_Cows()

count.get_total(5)