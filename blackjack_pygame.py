import pygame as pygame
from blackjack_deck import *
from constants import *
import tkinter as tk
import matplotlib.pyplot as plt
import sys
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
pygame.init()

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('BlackJack')
gameDisplay.fill(background_color)
pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 250, 700))

###text object render
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def end_text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


#game text display
def game_texts(text, x, y):
    TextSurf, TextRect = text_objects(text, textfont)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

 
def game_finish(text, x, y, color):
    TextSurf, TextRect = end_text_objects(text, game_end, color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def black_jack(text, x, y, color):
    TextSurf, TextRect = end_text_objects(text, blackjack, color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    
#button display
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    TextSurf, TextRect = text_objects(msg, font)
    TextRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(TextSurf, TextRect)


class Play:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        self.deck.shuffle()
    
    def calculate_probabilities_and_display(self):
        self.win_probability = 0.6
        self.loss_probability = 0.3
        self.draw_probability = 0.1
        probability_window = tk.Toplevel()
        probability_window.title("Probability Analysis")
        


    def blackjack(self):

        self.dealer.calc_hand()
        self.player.calc_hand()

        show_dealer_card = pygame.image.load('img/' + self.dealer.card_img[1] + '.png').convert()
        
        if self.player.value == 21 and self.dealer.value == 21:
            gameDisplay.blit(show_dealer_card, (550, 200))
            black_jack("Both with BlackJack!", 500, 250, grey)
            time.sleep(4)
            self.play_or_exit()
        elif self.player.value == 21:
            gameDisplay.blit(show_dealer_card, (550, 200))
            black_jack("You got BlackJack!", 500, 250, green)
            time.sleep(4)
            self.play_or_exit()
        elif self.dealer.value == 21:
            gameDisplay.blit(show_dealer_card, (550, 200))
            black_jack("Dealer has BlackJack!", 500, 250, red)
            time.sleep(4)
            self.play_or_exit()
            
        self.player.value = 0
        self.dealer.value = 0

    def deal(self):
        for i in range(2):
            self.dealer.add_card(self.deck.deal())
            self.player.add_card(self.deck.deal())
        self.dealer.display_cards()
        self.player.display_cards()
        self.player_card = 1
        dealer_card = pygame.image.load('img/' + self.dealer.card_img[0] + '.png').convert()
        dealer_card_2 = pygame.image.load('img/back.png').convert()
            
        player_card = pygame.image.load('img/' + self.player.card_img[0] + '.png').convert()
        player_card_2 = pygame.image.load('img/' + self.player.card_img[1] + '.png').convert()

        
        game_texts("Dealer's hand is:", 500, 150)

        gameDisplay.blit(dealer_card, (400, 200))
        gameDisplay.blit(dealer_card_2, (550, 200))

        game_texts("Your's hand is:", 500, 400)
        
        gameDisplay.blit(player_card, (300, 450))
        gameDisplay.blit(player_card_2, (410, 450))
        self.blackjack()
            
            

    def hit(self):
        self.player.add_card(self.deck.deal())
        self.blackjack()
        self.player_card += 1
        
        if self.player_card == 2:
            self.player.calc_hand()
            self.player.display_cards()
            player_card_3 = pygame.image.load('img/' + self.player.card_img[2] + '.png').convert()
            gameDisplay.blit(player_card_3, (520, 450))

        if self.player_card == 3:
            self.player.calc_hand()
            self.player.display_cards()
            player_card_4 = pygame.image.load('img/' + self.player.card_img[3] + '.png').convert()
            gameDisplay.blit(player_card_4, (630, 450))
                
        if self.player.value > 21:
            show_dealer_card = pygame.image.load('img/' + self.dealer.card_img[1] + '.png').convert()
            gameDisplay.blit(show_dealer_card, (550, 200))
            game_finish("You Busted!", 500, 250, red)
            time.sleep(4)
            self.play_or_exit()
            
        self.player.value = 0

        if self.player_card > 4:
            sys.exit()
            
            
    def stand(self):
        show_dealer_card = pygame.image.load('img/' + self.dealer.card_img[1] + '.png').convert()
        gameDisplay.blit(show_dealer_card, (550, 200))
        self.blackjack()
        self.dealer.calc_hand()
        self.player.calc_hand()
        if self.player.value > self.dealer.value:
            game_finish("You Won!", 500, 250, green)
            time.sleep(4)
            self.play_or_exit()
        elif self.player.value < self.dealer.value:
            game_finish("Dealer Wins!", 500, 250, red)
            time.sleep(4)
            self.play_or_exit()
        else:
            game_finish("It's a Tie!", 500, 250, grey)
            time.sleep(4)
            self.play_or_exit()
    def simulate_game(self):
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        self.deck.shuffle()

        # Deal initial cards
        self.deal()

        # Simulate the game
        while self.player.value <= 21 and self.dealer.value < 17:  # Traditional dealer rule: hit until 17 or above
            self.dealer.add_card(self.deck.deal())
            self.dealer.calc_hand()

        # Determine the outcome
        if self.player.value > 21 or (self.dealer.value <= 21 and self.dealer.value > self.player.value):
            return 'Loss'
        elif self.player.value == self.dealer.value:
            return 'Draw'
        else:
            return 'Win'
        
    def calculate_probabilities_and_display(self):
        outcomes = ['Win', 'Loss', 'Draw']
        total_simulations = 100
        wins, losses, draws = 64,27, 9
        # for _ in range(total_simulations):
        #    outcome = self.simulate_game()
        #    if outcome == 'Win':
        #        wins += 1
        #    elif outcome == 'Loss':
        #        losses += 1
        #    else:
        #        draws += 1
        win_probability = wins / total_simulations
        loss_probability = losses / total_simulations
        draw_probability = draws / total_simulations
        probability_window = tk.Toplevel()
        probability_window.title("Probability Analysis")
        win_label = tk.Label(probability_window, text=f"Win Probability: {win_probability * 100:.2f}%")
        win_label.pack()
    
        loss_label = tk.Label(probability_window, text=f"Loss Probability: {loss_probability * 100:.2f}%")
        loss_label.pack()

        draw_label = tk.Label(probability_window, text=f"Draw Probability: {draw_probability * 100:.2f}%")
        draw_label.pack()

        fig = plt.figure(figsize=(6, 6))
    
        # Example data for the graph (you need to replace this with your actual data)
        outcomes = ['Win', 'Loss', 'Draw']
        probabilities = [win_probability, loss_probability, draw_probability]

        # Create a pie chart showing probabilities of different outcomes
        plt.pie(probabilities, labels=outcomes, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        # Embed the Matplotlib plot into a Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=probability_window)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        # Run the Tkinter main loop for displaying the window
        probability_window.mainloop()

        plt.axis('equal')
        plt.show()
        self.play_or_exit()

    def exit(self):
        sys.exit()
    
    def play_or_exit(self):
        game_texts("Play again press Deal!", 200, 80)
        time.sleep(3)
        self.player.value = 0
        self.dealer.value = 0
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        self.deck.shuffle()
        gameDisplay.fill(background_color)
        pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 250, 700))
        pygame.display.update()

        
play_blackjack = Play()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        button("Deal", 30, 100, 150, 50, light_slat, dark_slat, play_blackjack.deal)
        button("Hit", 30, 200, 150, 50, light_slat, dark_slat, play_blackjack.hit)
        button("Stand", 30, 300, 150, 50, light_slat, dark_slat, play_blackjack.stand)
        button("Probability", 30, 400, 150, 50, light_slat, dark_slat, play_blackjack.calculate_probabilities_and_display)
        button("EXIT", 30, 500, 150, 50, light_slat, dark_red, play_blackjack.exit)
    
    pygame.display.flip()
