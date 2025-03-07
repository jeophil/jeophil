def compute_sum(n):
    total = 0
    for k in range(n):
        total+= k**4
    return total
# Taking input as an integer

user_input = int(input("Enter an integer: "))
print("You entered:", user_input)
print(compute_sum(user_input))


