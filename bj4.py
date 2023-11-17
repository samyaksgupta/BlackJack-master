import tkinter as tk
from tkinter import messagebox
import plotly.graph_objs as go

# Initialize global variables for tracking outcomes
total_games = 0
wins = 0
losses = 0
draws = 0

# Create a Plotly figure
fig = go.Figure()

# Function to simulate the blackjack game
def play_blackjack():
    global total_games, wins, losses, draws

    # ... (existing game logic remains the same)

    # Update outcome statistics
    if player_total > 21:
        losses += 1
    elif dealer_total > 21:
        wins += 1
    elif player_total > dealer_total:
        wins += 1
    elif player_total < dealer_total:
        losses += 1
    else:
        draws += 1

    total_games += 1

    # Update probabilities and display the graph
    update_probabilities()

# Update probabilities and display the graph
def update_probabilities():
    global wins, losses, draws, total_games

    # Calculate probabilities
    win_prob = wins / total_games if total_games > 0 else 0
    loss_prob = losses / total_games if total_games > 0 else 0
    draw_prob = draws / total_games if total_games > 0 else 0

    # Update Plotly figure with new data
    fig.data = []
    fig.add_trace(go.Scatter3d(x=['Win'], y=['Lose'], z=['Draw'],
                               mode='markers',
                               marker=dict(size=[win_prob * 100, loss_prob * 100, draw_prob * 100],
                                           color=['green', 'red', 'blue'],
                                           opacity=0.7)))

    fig.update_layout(scene=dict(xaxis_title='Win', yaxis_title='Lose', zaxis_title='Draw'),
                      title='Blackjack Winning Probabilities',
                      margin=dict(l=0, r=0, b=0, t=0))

    # Display the updated 3D scatter plot
    fig.show()

# Create the main window
root = tk.Tk()
root.title('Blackjack Game')

# Create a button to play blackjack
play_button = tk.Button(root, text='Play Blackjack', command=play_blackjack)
play_button.pack()

root.mainloop()
