def main():
    celsius = int(input("Enter the temp in degrees celsius: "))
    fahrenheit = celsius*9/5 + 32
    print(f"fahrenheit: \t {fahrenheit:.2f}")

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
