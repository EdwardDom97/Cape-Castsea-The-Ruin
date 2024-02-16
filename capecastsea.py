#Cape Castsea: The Ruins 3rd game jam submission


#starting the initial process with comments


#imports
import pygame
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





    # Game logic above this line # Rendering below this line
            




    if current_state == MENU:
        screen.fill((25, 25, 50))  # Clear the screen
        # Draw menu elements
        # Example: Draw a white rectangle as a placeholder button
        button_rect = pygame.Rect(100, 100, 200, 50)  # (x, y, width, height)
        pygame.draw.rect(screen, (255, 255, 255), button_rect)

        text_surface = font.render("Cape Castsea: The Ruins", True, menu_text_color)
        text_rect = text_surface.get_rect(center=(screen_width // 4, 50))  # Center the text horizontally
        screen.blit(text_surface, text_rect)

        # Render "Play" text on the button
        play_text = font.render("Play", True, (0, 0, 0))
        text_rect = play_text.get_rect(center=button_rect.center)
        screen.blit(play_text, text_rect)

         # Check for mouse clicks
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Check if mouse click is inside the button rectangle
                    if button_rect.collidepoint(event.pos):
                        # Perform button action
                        current_state = GAME







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
            
    # Draw UI elements


    # Rendering
    pygame.display.flip()


# Quit pygame
pygame.quit()


#here I am going to load more variables related to the overall structure of the game like colors, images, time, score, items, and more.



