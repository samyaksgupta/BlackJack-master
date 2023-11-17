import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

# Function to simulate the blackjack game
def play_blackjack():
    # Initialize deck
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4  # Ace is considered as 11

    # Shuffle the deck
    np.random.shuffle(deck)

    # Deal cards to player and dealer
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Function to calculate hand value
    def calculate_hand_value(hand):
        total = sum(hand)
        if total > 21 and 11 in hand:  # Adjust for aces
            total -= 10
        return total

    # Function to check for blackjack (21 with 2 cards)
    def is_blackjack(hand):
        return len(hand) == 2 and calculate_hand_value(hand) == 21

    # Check for player blackjack
    if is_blackjack(player_hand):
        messagebox.showinfo("Result", "Blackjack! You win.")
        return

    # Player's turn
    while calculate_hand_value(player_hand) < 21:
        if messagebox.askyesno("Hit or Stand", f"Your cards: {player_hand}. Hit or Stand?"):
            player_hand.append(deck.pop())
        else:
            break

    player_total = calculate_hand_value(player_hand)

    # Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    dealer_total = calculate_hand_value(dealer_hand)

    # Determine the winner
    if player_total > 21:
        messagebox.showinfo("Result", f"You busted! Dealer wins. Your total: {player_total}")
    elif dealer_total > 21:
        messagebox.showinfo("Result", f"Dealer busted! You win. Dealer's total: {dealer_total}")
    elif player_total > dealer_total:
        messagebox.showinfo("Result", f"You win! Your total: {player_total}, Dealer's total: {dealer_total}")
    elif player_total < dealer_total:
        messagebox.showinfo("Result", f"Dealer wins! Your total: {player_total}, Dealer's total: {dealer_total}")
    else:
        messagebox.showinfo("Result", f"It's a draw! Your total: {player_total}, Dealer's total: {dealer_total}")

# Probability explanation
def show_probability():
    plt.figure(figsize=(6, 4))
    # Example of a graph representing winning probabilities
    outcomes = ['Win', 'Lose', 'Draw']
    probabilities = [0.4, 0.5, 0.1]  # Example probabilities, replace with actual values
    plt.bar(outcomes, probabilities)
    plt.title('Blackjack Winning Probabilities')
    plt.xlabel('Outcomes')
    plt.ylabel('Probabilities')
    plt.show()

# Create the main window
root = tk.Tk()
root.title('Blackjack Game')

# Create buttons
play_button = tk.Button(root, text='Play Blackjack', command=play_blackjack)
play_button.pack()

probability_button = tk.Button(root, text='Show Probabilities', command=show_probability)
probability_button.pack()

root.mainloop()
