#Cape Castsea: The Ruins 3rd game jam submission


#starting the initial process with comments


#imports
import pygame
import sys
from pygame.locals import *


#start/initialize the pygame library

pygame.init()

#usually declare window size and everything here

screen_height = 900
screen_width = 1600
screen = pygame.display.set_mode((screen_width,screen_height))

#Set fullscreen flag initially to False
fullscreen = False

# Declare font and text stuff
font = pygame.font.SysFont(None, 42)  # Example font and size
menu_text_color = (150, 150, 150)  # Example text color for the menu

#this is my caption heading the application itself
pygame.display.set_caption('Cape Castsea: The Ruins')



#here I want to load in my environment and related varibles
ground_tile = pygame.image.load('graphics/ground.png')
# Import the image for the tree border
tree_border_tile = pygame.image.load('graphics/treeborder.png')
#import water tile
sea_tile = pygame.image.load('graphics/sea_tile.png')

# Define tile types (using numbers to represent different tile types)
GROUND = 0
WATER = 1




# Define the size of the tiles
TILE_SIZE = 32


#world size variables
#world_width = 1500
#world_height = 1200
#creating a temporary varible to reflect a previous project.
MAP_SIZE = 64
# Define the size of the playable area within the tree border



# Create a 2D list to represent the tilemap
#tilemap = [[GROUND for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)] (old/current)
# Modify the size of the playable area within the tree border
PLAYABLE_AREA_WIDTH = MAP_SIZE // 4

# Create a 2D list to represent the tilemap
tilemap = [[WATER if col >= 3 * PLAYABLE_AREA_WIDTH else GROUND for col in range(MAP_SIZE)] for _ in range(MAP_SIZE)]


#some sort of camera or scroll function so the player can pan around the map
#camera variable and player variables
# Camera variables
camera_x = 0
camera_y = 0

# Player variables
player_width = 32
player_height = 32
player_x, player_y = screen_width// 2, screen_height // 2
player_speed = 2
player_speed_multiplier = 1  # Adjust this value to change player speed created this because I felt liek the player was moving too fast



# Constants for game states
MENU = 'MENU'
GAME = 'GAME'
OPTIONS = 'OPTIONS'



#here I am going to load in my frist building image and assign it a position in the world.
cape_house = pygame.image.load('graphics/capehouse.png')
cape_house_position = (150,150)
cape_house_rect = cape_house.get_rect(topleft=cape_house_position)

#here I am loading in the second building
cape_store = pygame.image.load('graphics/capestore.png')
cape_store_position = (400, 380)
cape_store_rect = cape_store.get_rect(topleft=cape_store_position)


#this will be the third building




#this could be a structure like a well




# Create a Clock object
clock = pygame.time.Clock()  


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
        #player_rect.topleft = (player_x, player_y)


        keys = pygame.key.get_pressed()

        if keys[K_a]:
            player_x -= player_speed
            player_x = max(player_x, camera_x + player_width)


        if keys[K_d]:
            player_x += player_speed
            player_x = min(player_x, camera_x + screen_width - player_width-32)


        if keys[K_w]:
            player_y -= player_speed
            player_y = max(player_y, camera_y + player_height)


        if keys[K_s]:
            player_y += player_speed
            player_y = min(player_y, camera_y + screen_height - player_height-32)



        # Update camera position based on player's position
        camera_x = player_x - screen_width // 2
        camera_y = player_y - screen_height// 2
        # Clamp camera position to stay within the world boundaries
        camera_x = max(0, min(camera_x, (MAP_SIZE * TILE_SIZE) - screen_width))
        camera_y = max(0, min(camera_y, (MAP_SIZE * TILE_SIZE) - screen_height))

    
        # Render the visible portion of the tilemap based on camera position
        start_row = camera_y // TILE_SIZE
        end_row = start_row + (screen_height // TILE_SIZE) + 1
        start_col = camera_x // TILE_SIZE
        end_col = start_col + (screen_width // TILE_SIZE) + 1

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
        # Rendering the ground and water tiles
        for row in range(start_row, min(end_row + 1, MAP_SIZE)):
            for col in range(start_col, min(end_col, MAP_SIZE)):
                tile_type = tilemap[row][col]
                tile_x, tile_y = (col * TILE_SIZE) - camera_x, (row * TILE_SIZE) - camera_y

                if tile_type == GROUND:
                    screen.blit(ground_tile, (tile_x, tile_y))
                elif tile_type == WATER:
                    screen.blit(sea_tile, (tile_x, tile_y))

                # Check for border tiles
                if row == 0 or row == MAP_SIZE - 1 or col == 0 or col == MAP_SIZE + 1:
                    screen.blit(tree_border_tile, (tile_x, tile_y))


                # Ensure player can only walk on ground tiles
                player_tile_row = (player_y + player_height // 2) // TILE_SIZE
                player_tile_col = (player_x + player_width // 2) // TILE_SIZE
                if tilemap[player_tile_row][player_tile_col] == WATER:
                    # If the player is standing on water, prevent movement
                    # You can adjust this to handle player movement based on surrounding tiles if needed
                    player_x, player_y = prev_player_x, prev_player_y  # Revert to previous position

                # Update previous player position for collision detection
                prev_player_x, prev_player_y = player_x, player_y


        #render the first capehouse
        screen.blit(cape_house, (cape_house_position[0] - camera_x, cape_house_position[1] - camera_y))


        #rendering the capestore
        screen.blit(cape_store,(cape_store_position[0] - camera_x, cape_store_position[1] - camera_y))
 


         # Render player
        pygame.draw.rect(screen, (255, 255, 255), (player_x - camera_x, player_y - camera_y, player_width, player_height))



        #this is an extremely crude implementation of collision seeing as I will have to add it per building. will soon create a building class after i've loaded three or more structures.
        # Check for collision between player and cape house      
        if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(cape_house_rect):
            # If the player collides with the cape house, prevent player movement in that direction
            if player_x < cape_house_rect.left:
                player_x = cape_house_rect.left - player_width

            elif player_x > cape_house_rect.right - player_width:
                player_x = cape_house_rect.right

            if player_y < cape_house_rect.top:
                player_y = cape_house_rect.top - player_height

            elif player_y > cape_house_rect.bottom - player_height:
                player_y = cape_house_rect.bottom

    # Draw game elements
    



    elif current_state == OPTIONS:
        screen.fill((25, 50, 65))  # Clear the screen
        # Draw menu elements

        # Example: Draw a white rectangle as a placeholder button
        fullscreen_rect = pygame.Rect(100, 100, 200, 50)  # (x, y, width, height)
        pygame.draw.rect(screen, (255, 255, 255), fullscreen_rect)

        # Render "Fullscreen" text on the button
        fullscreen_text = font.render("Fullscreen", True, (0, 0, 0))
        text_rect = fullscreen_text.get_rect(center=fullscreen_rect.center)
        screen.blit(fullscreen_text, text_rect)


        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()

                    if fullscreen_rect.collidepoint(mouse_pos):
                        # Toggle fullscreen mode
                        fullscreen = not fullscreen
                        if fullscreen:
                            pygame.display.set_mode((screen_width, screen_height), FULLSCREEN)
                        else:
                            pygame.display.set_mode((screen_width, screen_height))


    # Draw UI elements



    # Rendering
    pygame.display.flip()
     

#sets the ingame frames to 60
clock.tick(60)

# Quit pygame
pygame.quit()


#here I am going to load more variables related to the overall structure of the game like colors, images, time, score, items, and more.



