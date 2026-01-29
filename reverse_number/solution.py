def reverse(num):
    # Define the maximum value for a 32-bit signed integer
    INT_MAX = 2**31 - 1

    # Initialize result to 0, which will store the reversed number
    result = 0

    # Check if the number is negative
    is_negative = num < 0

    # Work with the absolute value of num for simplicity
    if (is_negative):
        num = -num;

    # Loop through the digits of the number until num becomes 0
    while num != 0:
        # Extract the last digit of num
        digit = num % 10

        # Remove the last digit from num
        num //= 10

        # Check for overflow before updating the result
        # If adding the digit will cause an overflow, return 0
        if result > (INT_MAX - digit) // 10:
            return 0

        # Update the result by shifting the previous digits and adding the new digit
        result = result * 10 + digit

    # Return the result with the correct sign
    return -result if is_negative else result

def main():
    test_cases = [123, -1230, 12000, 0, 1534236469]

    for i, test_case in enumerate(test_cases, start=1):
        print(i, ".\tInput num:", test_case, sep="")
        print("\tReversed num:", reverse(test_case))
        print("-" *100)

if __name__ == "__main__":
    main()
