import os
import random
import time

MAX_LINES = 30
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
REELS = 5

# Adjusted symbol counts and values for enhanced gameplay
symbol_count = {
    "$": 3,
    "A": 4,
    "%": 6,
    "#": 8,
    "B": 10,
    "D": 15,
    "X": 20,
    "WILD": 2  # Example of a special symbol
}

symbol_value = {
    "$": 20,
    "A": 18,
    "%": 16,
    "#": 14,
    "B": 12,
    "D": 10,
    "X": 8,
    "WILD": 50  # Example of a special symbol with higher value
}

# Function to check winnings based on the adjusted symbol counts and values
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for column in columns:
        for line in range(min(len(column), lines)):
            symbol = column[line]
            if all(symbol == column[i] for i in range(len(column))):
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)
    return winnings, winning_lines

# Function to animate spinning reels
def animate_spinning():
    for _ in range(3):
        print("Spinning reels...")
        time.sleep(1)
        clear_screen()

# Function to play sound effects
def play_sound(sound):
    # Placeholder for playing sound effects
    pass

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display winning animations
def display_winning_animation():
    print("Congratulations, you've won!")
    # Placeholder for displaying winning animations
    time.sleep(2)
    clear_screen()

# Function to print the slot machine
def print_slot_machine(columns):
    clear_screen()
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

# Function to update balance and display results
def update_balance_and_display_results(balance, winnings, total_bet, winning_lines):
    balance += winnings - total_bet
    print(f"YOU WON ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    print(f"Current balance is ${balance}")
    return balance

# Adjusted spin function to incorporate visual enhancements and sound effects
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough money to bet, here is your total balance right now ${balance}")

        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet} ")
    animate_spinning()  # Animate spinning reels
    slots = get_slot_machine_spin(ROWS, REELS, symbol_count)
    print_slot_machine(slots)

    # Check for winnings
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    play_sound("winning_sound") if winnings > 0 else play_sound("losing_sound")

    # Display winning animations if applicable
    display_winning_animation() if winnings > 0 else None

    # Update balance and display results
    balance = update_balance_and_display_results(balance, winnings, total_bet, winning_lines)

    return balance

# Function to get the bet amount
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The amount has to be between ${MAX_BET} - ${MAX_BET}.")

        else:
            print("Please enter a number.")

    return amount

# Function to get the number of lines
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")

        else:
            print("Please enter a number.")

    return lines

# Function to get the slot machine spin
def get_slot_machine_spin(rows, reels, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(reels):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# Main function to run the slot machine game
def main():
    balance = deposit()
    while True:
        #print(f"Current balance is ${balance}")
        answer = input("press enter to play (q to quit).")
        if answer == "q":
            break
        balance = spin(balance)

    print(f"You left with ${balance}")

# Function to deposit money
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount has to be greater than 0.")

        else:
            print("Please enter a number.")
    return amount

if __name__ == "__main__":
    main()
