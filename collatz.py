# The number we will pwerform the Collatz operations on.
n = 20

# Keep looping until mwe reach 1.
# Note: this assumes the Collatz conjecture is true.
while n != 1:
    # Print the current value of n.
    print (n)
    # Check if n is even.
    if n % 2 == 0:
        # If n is even, divide it by two.
        n = n / 2
    else:
        # If n is odd, multiply by three and add 1.
        n = (3 * n) + 1
# Finally, print the 1.
print (n)