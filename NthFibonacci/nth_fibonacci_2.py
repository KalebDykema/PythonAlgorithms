def getNthFib(n, memoize={1: 0, 2: 1}):
   if n in memoize:
      return memoize[n]

   memoize[n] = getNthFib(n - 2, memoize) + getNthFib(n - 1, memoize)
   return memoize[n]
