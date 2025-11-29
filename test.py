def recurSum(n):
    if n == 0:
         return 0
    return n + recurSum(n-1)
