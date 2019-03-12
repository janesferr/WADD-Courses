def sum(lower, upper):
   """
   Arguments: A lower bound and an upper bound
   Returns: the sum of the numbers between the arguments
            and including them
   """
   result = 0
   while lower <= upper:
      result += lower
      lower += 1
   return result
