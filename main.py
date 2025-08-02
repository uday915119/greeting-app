def main():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print(f"Addition: {a + b}")
        print(f"Subtraction: {a - b}")
        print(f"Multiplication: {a * b}")
        print(f"Division: {a / b if b != 0 else 'Infinity'}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
