def getNthFib(n):
   if n < 3:
      return n - 1

   return getNthFib(n - 2) + getNthFib(n - 1)