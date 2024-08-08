def fat(n: int) -> int:
    if n == 1:
        return 1
    
    else:  # This else ins't necessary
        return n * fat(n - 1)


print(fat(900))
