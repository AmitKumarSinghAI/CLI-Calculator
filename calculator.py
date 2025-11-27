# Import library 
import time

# Define all operations using dictionary mapping
operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: "❌ Error: Division by zero!" if b == 0 else a / b
}

# Stylish banner
def banner():
    print("\n" + "="*40)
    print("🧮 Welcome to PYTHON 3 CLI Calculator 3000 🧮")
    print("="*40)

# Show operation choices
def menu():
    print("""
Choose your operation:
    ➕  +  : Addition
    ➖  -  : Subtraction
    ✖️  *  : Multiplication
    ➗  /  : Division
    ❌  exit : Quit Calculator
""")

# Safely get number from user
def get_number(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("⚠️  Please enter a valid number!")

# Run calculator logic
def run_calculator():
    banner()
    while True:
        menu()
        op = input("👉 Enter operation (+, -, *, /) or 'exit': ").strip()

        if op == 'exit':
            print("\n👋 Thank you for using Calculator 3000. Goodbye!")
            break

        if op not in operations:
            print("🚫 Invalid operation! Try again.")
            continue

        num1 = get_number("🔢 Enter first number: ")
        num2 = get_number("🔢 Enter second number: ")
        result = operations[op](num1, num2)

        print(f"\n✅ Result: {num1} {op} {num2} = {result}")
        print("-"*40)
        time.sleep(1)

if __name__ == "__main__":
    run_calculator()
