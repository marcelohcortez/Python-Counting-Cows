""""
Count the number of cows after 'n' years. We start with 1 cow, and we know that: 
- Each cow gives birth to one calf every year;
- A calf grows into a cow after 2 years;
- Cows and calves never die.
"""
class Counting_Cows: #create the class that will handle the functions
    def cows_number(self, year: int) -> int: #count the cows after n years
      if year < 0:
        return -1
      elif year >= 0 and year <= 2:
        return 1
      else:
        return year -1

    def get_total(self, year: int) -> int:#get the total based on the input year
      total = 0
      i = 0
      for i in range(year):#iterate once for every year on the input
        total += self.cows_number(i)

      print(total)

count = Counting_Cows() #initialize the class and set it to the variable count

count.get_total(15) #use the get_total function inside the class to pass the number of years