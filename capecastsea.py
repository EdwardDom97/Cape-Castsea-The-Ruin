#Cape Castsea: The Ruins 3rd game jam submission


#starting the initial process with comments


#imports
import pygame
import sys
from pygame.locals import *


#start/initialize the pygame library

pygame.init()

#usually declare window size and everything here

screen_height = 450
screen_width = 800
screen = pygame.display.set_mode((screen_width,screen_height))

# Declare font and text stuff
font = pygame.font.SysFont(None, 42)  # Example font and size
menu_text_color = (150, 150, 150)  # Example text color for the menu

#here I will declare a few separate game states for better management.
pygame.display.set_caption('Cape Castsea: The Ruins')




#here I want to load in my environment and related varibles
ground_tile = pygame.image.load('ground.png')
# Define tile types (you can use numbers to represent different tile types)
GROUND = 0
# Define the size of the tiles
TILE_SIZE = 32

#world size variables
world_width = 1000
world_height = 1200

# Create a 2D list to represent the tilemap
tilemap = [[GROUND for _ in range(world_width // TILE_SIZE)] for _ in range(world_height // TILE_SIZE)]


#some sort of camera or scroll function so the player can pan around the map
#camera variable and player variables
# Camera variables
camera_width = screen_width
camera_height = screen_height
camera_x = 0
camera_y = 0

# Player variables
player_width = 32
player_height = 32
player_x = world_width // 2
player_y = world_height // 2
player_speed = 1



# Constants for game states
MENU = 'MENU'
GAME = 'GAME'
OPTIONS = 'OPTIONS'



#here I am going to load in my frist building image and assign it a position in the world.
cape_house = pygame.image.load('capehouse.png')
cape_house_position = (150,150)
cape_house_rect = cape_house.get_rect(topleft=cape_house_position)





# Variable to track current game state
current_state = MENU  # Start with the menu state

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    


    if current_state == MENU:
       

        # Menu state logic
        pass



    elif current_state == GAME:
        # Game state logic

        keys = pygame.key.get_pressed()
        if keys[K_w]:
            player_y -= player_speed
        if keys[K_s]:
            player_y += player_speed
        if keys[K_a]:
            player_x -= player_speed
        if keys[K_d]:
            player_x += player_speed

            # Update camera position to center on the player
        camera_x = player_x - camera_width // 2
        camera_y = player_y - camera_height // 2

        # Clamp camera position to stay within the bounds of the game world
        camera_x = max(0, min(world_width - camera_width, camera_x))
        camera_y = max(0, min(world_height - camera_height, camera_y))

        # Listen for Esc key press to return to the menu state
        if keys[K_ESCAPE]:
            current_state = MENU


        pass


    elif current_state == OPTIONS:
        #options variables and logic
        keys = pygame.key.get_pressed()

        #checks for the escape key to return user to menu
        if keys[K_ESCAPE]:
            current_state = MENU
        pass







    # Game logic above this line # Rendering below this line
            






    if current_state == MENU:
        screen.fill((25, 25, 50))  # Clear the screen
        # Draw menu elements

        #placing this text display first because this will head the main or menu screen of the game
        text_surface = font.render("Cape Castsea: The Ruins", True, menu_text_color)
        text_rect = text_surface.get_rect(center=(screen_width // 4, 50))  # Center the text slightly towards the left side
        screen.blit(text_surface, text_rect)

        #1st button
        # Example: Draw a white rectangle as a placeholder button
        #now renaming first button_rect to playbutton_rect in order to add additional buttons
        playbutton_rect = pygame.Rect(100, 100, 200, 50)  # (x, y, width, height)
        pygame.draw.rect(screen, (255, 255, 255), playbutton_rect)

        # Render "Play" text on the button
        play_text = font.render("Play", True, (0, 0, 0))
        playtext_rect = play_text.get_rect(center=playbutton_rect.center)
        screen.blit(play_text, playtext_rect)


        #2nd button
        #this rectangle will be a placeholder for my options button which will allow optimization like sound, fullscreen, ect.
        optionsbutton_rect = pygame.Rect(100, 175, 200, 50)  # (x, y, width, height)
        pygame.draw.rect(screen, (255, 255, 255), optionsbutton_rect)

        # Render "options" text on the 2nd button
        options_text = font.render("Options", True, (0, 0, 0))
        optionstext_rect = options_text.get_rect(center=optionsbutton_rect.center)
        screen.blit(options_text, optionstext_rect)


        #3rd button
        exitbutton_rect = pygame.Rect(100,250, 200, 50)
        pygame.draw.rect(screen, (225,255,255), exitbutton_rect)

        #rendering the "exit" text on the 3rd button
        exit_text = font.render("Exit", True, (0, 0, 0))
        exittext_rect = exit_text.get_rect(center=exitbutton_rect.center)
        screen.blit(exit_text, exittext_rect)





         # Check for mouse clicks
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Check if mouse click is inside the button rectangle
                    if playbutton_rect.collidepoint(event.pos):
                        # Perform button action
                        current_state = GAME

                    elif optionsbutton_rect.collidepoint(event.pos):
                        current_state = OPTIONS

                    elif exitbutton_rect.collidepoint(event.pos):
                        running = False
                        pygame.quit()
                        sys.exit()




    elif current_state == GAME:
        screen.fill((0, 0, 0))  # Clear the screen
        # Render game elements
          # Rendering the ground tiles
        for row in range(len(tilemap)):
            for col in range(len(tilemap[0])):
                if tilemap[row][col] == GROUND:
                    tile_x = col * TILE_SIZE - camera_x
                    tile_y = row * TILE_SIZE - camera_y
                    screen.blit(ground_tile, (tile_x, tile_y))


        #render the first capehouse
        screen.blit(cape_house, (cape_house_position[0] - camera_x, cape_house_position[1] - camera_y))

         # Render player
        pygame.draw.rect(screen, (255, 255, 255), (player_x - camera_x, player_y - camera_y, player_width, player_height))


    # Draw game elements
    

    elif current_state == OPTIONS:
        screen.fill((25, 50, 65))  # Clear the screen
        # Draw menu elements
        # Example: Draw a white rectangle as a placeholder button
        button_rect = pygame.Rect(100, 100, 200, 50)  # (x, y, width, height)
        pygame.draw.rect(screen, (255, 255, 255), button_rect)

        # Render "Fullscreen" text on the button
        fullscreen_text = font.render("Fullscreen", True, (0, 0, 0))
        text_rect = fullscreen_text.get_rect(center=button_rect.center)
        screen.blit(fullscreen_text, text_rect)


    # Draw UI elements


    # Rendering
    pygame.display.flip()


# Quit pygame
pygame.quit()


#here I am going to load more variables related to the overall structure of the game like colors, images, time, score, items, and more.



