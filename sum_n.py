def recurSum(n):
    
    # base case
    if n == 0:
        return 0
        
        # recursive case
    return n + recurSum(n - 1)


# Driver code
if __name__ == "__main__":
    n = 3
    print(recurSum(n))