# The 'continue' statement skips numbers > 800.
for number in numbers:
    # 1. Skip check: If the number is greater than 800, skip to the next iteration.
    if number > 800:
        continue
        
    # 2. Print check: If the number is divisible by 3 (remainder is 0).
    if number % 3 == 0:
        print(number)