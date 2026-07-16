def get_sum_of_odd_squares(n):
    sum = 0
    for i in range(1, n+1):
        if i * i % 2 != 0:
            sum += i * i
    return sum

print(get_sum_of_odd_squares(5)) 
print(get_sum_of_odd_squares(783000))  # Example usage

