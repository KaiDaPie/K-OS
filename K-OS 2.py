import time
import os
from colorama import init, Fore, Back, Style
import os
import pygame
import random
import webbrowser
import sys
import select
import tty
import termios
import tkinter as tk
from tkinter import filedialog

def open_url():
    url = input("Enter the URL you want to open: ")

    # Check if the URL contains the protocol (http:// or https://)
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    try:
        webbrowser.open(url)
    except Exception as e:
        print("Error opening URL:", e)



def img():
    pygame.init()

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])

    if not file_path:
        print("No file selected.")
        return

    image = pygame.image.load(file_path)

    dis_width = 800
    dis_height = 600

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Image Viewer')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        dis.fill((255, 255, 255))
        dis.blit(image, (0, 0))

        pygame.display.update()




def main_loop():
    while True:
        home()


def noteapp():
    text = ""
    while True:
        clr()
        print(Fore.BLUE + "K-OS Text Editor")
        print(Fore.WHITE + "1. New")
        print("2. Open")
        print("3. Save")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            text = ""
        elif choice == "2":
            file_path = filedialog.askopenfilename(title="Open File", filetypes=[("Text Files", "*.txt")])
            if file_path:
                with open(file_path, 'r') as file:
                    text = file.read()
        elif choice == "3":
            file_path = filedialog.asksaveasfilename(title="Save File", defaultextension=".txt",
                                                    filetypes=[("Text Files", "*.txt")])
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(text)
        elif choice == "4":
            break
        
        clr()
        print(Fore.BLUE + "K-OS Text Editor")
        print(Fore.WHITE + "Editing file: Untitled.txt")
        print(text)
        
        input("Press Enter to continue...")




def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    input("Press Enter to stop the music.")
    pygame.mixer.music.stop()

def main():
    clr()
    music_folder = "music"  # Name of the folder where your music files are stored
    print("Welcome to K-OS Music Player!")
    print(f"Enter the filename of the music file to play from the '{music_folder}' folder.")
    print("Type 'quit' to exit the music player.")

    while True:
        file_name = input("Enter the filename: ")

        if file_name.lower() == 'quit':
            print("Exiting K-OS Music Player.")
            home()
            break

        file_path = os.path.join(music_folder, file_name)

        if not os.path.exists(file_path):
            print("File not found. Please try again.")
            continue

        try:
            play_music(file_path)
        except pygame.error:
            print("Error: Could not play the music. Make sure the file is in a supported format (e.g., mp3 or wav).")






def snake_game():
    pygame.init()

    # Game settings
    window_width, window_height = 640, 480
    snake_size = 20
    fps = 10

    # Colors
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)

    # Initialize the window
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('K-OS Snake Game')

    clock = pygame.time.Clock()

    # Initial snake position and movement
    snake_head = [window_width // 2, window_height // 2]
    snake = [snake_head]
    change_direction = [0, 0]

    # Initial food position
    food_position = [random.randrange(0, window_width // snake_size) * snake_size,
                     random.randrange(0, window_height // snake_size) * snake_size]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                home()

        # Rest of your game logic...


            # Handling arrow keys for movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_direction = [-snake_size, 0]
                elif event.key == pygame.K_RIGHT:
                    change_direction = [snake_size, 0]
                elif event.key == pygame.K_UP:
                    change_direction = [0, -snake_size]
                elif event.key == pygame.K_DOWN:
                    change_direction = [0, snake_size]

        # Update snake position and check collisions
        snake_head[0] += change_direction[0]
        snake_head[1] += change_direction[1]

        if snake_head[0] < 0 or snake_head[0] >= window_width or \
           snake_head[1] < 0 or snake_head[1] >= window_height:
            pygame.quit()
            return

        snake.insert(0, list(snake_head))
        if snake_head == food_position:
            food_position = [random.randrange(0, window_width // snake_size) * snake_size,
                             random.randrange(0, window_height // snake_size) * snake_size]
        else:
            snake.pop()

        # Draw the game
        window.fill(white)
        for segment in snake:
            pygame.draw.rect(window, green, pygame.Rect(segment[0], segment[1], snake_size, snake_size))
        pygame.draw.rect(window, red, pygame.Rect(food_position[0], food_position[1], snake_size, snake_size))

        pygame.display.update()
        clock.tick(fps)
		  
        



def htmlopener(file_name):
    try:
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, file_name)
        # Open the HTML file in the default web browser
        webbrowser.open(file_path)
    except Exception as e:
        print("Error:", e)





def bootup():
	print("Booting Up...")
	time.sleep(0.5)
	print("######")
	time.sleep(0.5)
	clr()
	load()


def calculator_app():
	operator = input("Enter an operator (+ - * /): ")
	num1 = float(input("Enter the 1st number: "))
	num2 = float(input("Enter the 2nd number: "))
	
	if operator == "+":
	    result = num1 + num2
	    print(round(result, 3))
	elif operator == "-":
	    result = num1 - num2
	    print(round(result, 3))
	elif operator == "*":
	    result = num1 * num2
	    print(round(result, 3))
	elif operator == "/":
	    result = num1 / num2
	    print(round(result, 3))
	else:
	    print(f"{operator} is not a valid operator")
	input("")
	home()


def home():
	clr()
	print(Fore.BLUE + "K-OS 2", Fore.GREEN + "v1")
	print(Fore.WHITE + "##APPS##")
	print("1. calculator.app")
	print("2. credits.text") 
	print("3. K-OS Tower Defense")
	print("4. K-Snake")
	print("5. K-Music")
	print("6. Notepad")
	print("7. Flappy Bird")
	print("8. K-OS Image View")
	print("9 'Web Browser' ")
	
	picked = input("")
	if picked == "1":
		calculator_app()
	elif picked == "2":
		clr()
		print("//CREDITS//")
		print("Me: coding & idea")
		print("ChatGPT: Help and teaching me Python")
		input("")
		clr()
		home()
	elif picked == "3":
			htmlopener("TD.html")
	elif picked == "4":
			htmlopener("snake.html")
	elif picked == "5":
			main()
	elif picked == "6":
			noteapp()
	elif picked == "7":
			htmlopener("flappy.html")
	elif picked == "8":
			img()
	elif picked == "9":
			open_url()


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')


def note():
	clr()
	print("im starting again... ")
	time.sleep(0.5)
	print("the old one was a buggy mess..")
	time.sleep(0.5)
	print("Anyways, enjoy...")
	time.sleep(0.75)
	print(Style.BRIGHT + Fore.BLUE + "K-OS 2!")
	time.sleep(1)
	load()

def entpass():
	password = "i <3 cheese"
	picked = input(Fore.RED + "Enter your password. ")
	if password == picked:
		print(Fore.WHITE + "Logging in.")
		clr()
		home()





def load():
    clr()
    print(Fore.GREEN + "Starting Machine...")
    time.sleep(1)
    print("Initiating...")
    time.sleep(1)
    print("Loading Files...")
    time.sleep(0.1)
    print("Loaded weenie.sys")
    time.sleep(0.1)
    print("Loaded BSOD.sys")
    time.sleep(0.1)
    print("Loaded therock.jpeg")
    time.sleep(0.1)
    print("Loaded calculator.app")
    time.sleep(0.1)
    print("Loaded BOOT.sys")
    time.sleep(0.1)
    print("You are logged in as `Kai`")


    time.sleep(0.75)
    clr()
    entpass()



bootup()



if __name__ == "__main__":
    main_loop()
