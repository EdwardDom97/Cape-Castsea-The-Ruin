#Cape Castsea: The Ruins 3rd game jam submission 02/16/2024


#02/17/2024 going to make a few notes here, like how I did the sea, I also want to add a few colums of sand in between the ground and water. I think that would look visually awesome.
#





#starting the initial process with comments


#imports
import pygame
import sys
import random
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
GUI_font = pygame.font.SysFont(None, 46)
menu_text_color = (150, 150, 150)  # Example text color for the menu
WHITE_TEXT = (255, 255, 255)


#this is my caption heading the application itself
pygame.display.set_caption('Cape Castsea: The Ruins')



#here I want to load in my environment and related varibles
ground_tile = pygame.image.load('graphics/ground.png')
# Import the image for the tree border
tree_border_tile = pygame.image.load('graphics/treeborder.png')
#import water tile
sea_tile = pygame.image.load('graphics/sea_tile.png')
#importing an additional tile type for a beach
sand_tile = pygame.image.load('graphics/sand_tile.png')
#importing the base block for the ruins level
ruins_tile = pygame.image.load('graphics/ruinsbase.png')



# Define tile types (using numbers to represent different tile types)
GROUND = 0
WATER = 1
SAND = 2
ANCIENTRUINS = 3

# Define the size of the tiles
TILE_SIZE = 32



#world size variables for the town area
game_world_width = screen_width + TILE_SIZE * 10  # Assuming you want 10 additional columns for the beach
game_world_height = 1300

# Calculate the number of tiles in the map based on the game world size and tile size
GAME_MAP_SIZE_X = game_world_width // TILE_SIZE
GAME_MAP_SIZE_Y = game_world_height // TILE_SIZE

# Create a 2D list to represent the tilemap for the town
tilemap = [[GROUND for _ in range(GAME_MAP_SIZE_X)] for _ in range(GAME_MAP_SIZE_Y)]





#I am going to copy the town area code named GAME MAP SIZE and call it PASSAGES WIDTH, HEIGHT, PASSAGES MAP SIX X and so on.
passages_width = 1200
passages_height = 2500

# Calculate the number of tiles in the map based on the passage world size
PASSAGES_MAP_SIZE_X = passages_width // TILE_SIZE
PASSAGES_MAP_SIZE_Y = passages_height // TILE_SIZE

# Create a 2D list to represent the tilemap for the passages
passages_tilemap = [[GROUND for _ in range(PASSAGES_MAP_SIZE_X)] for _ in range(PASSAGES_MAP_SIZE_Y)]






#This is going to be the third implementation of a map for the ruins area

ruins_width = 2500
ruins_height = 2500


# Calculate the number of tiles in the map based on the ruins world size
RUINS_MAP_SIZE_X = ruins_width // TILE_SIZE
RUINS_MAP_SIZE_Y = ruins_height // TILE_SIZE


# Create a 2D list to represent the tilemap for the ruins
ruins_tilemap = [[ANCIENTRUINS for _ in range(RUINS_MAP_SIZE_X)] for _ in range(RUINS_MAP_SIZE_Y)]








# Camera variables #camera variable and player variables #some sort of camera or scroll function so the player can pan around the map
camera_x = 0
camera_y = 0

# Player variables
player_width = 32
player_height = 32
player_x, player_y = screen_width// 2, screen_height // 2
player_speed = 2
player_speed_multiplier = 1  # Adjust this value to change player speed created this because I felt liek the player was moving too fast
interact = False
player_gold = 2
player_health = 5
player_mana = 3






# Constants for game states
MENU = 'MENU'
GAME = 'GAME'
OPTIONS = 'OPTIONS'
PASSAGES = 'PASSAGES'
THERUINS = 'THERUINS'



#here I am going to load in my frist building image and assign it a position in the world.
cape_house = pygame.image.load('graphics/capehouse.png')
cape_house_position = (150,150)
cape_house_rect = cape_house.get_rect(topleft=cape_house_position)

#here I am loading in the second building
cape_store = pygame.image.load('graphics/capestore.png')
cape_store_position = (400, 380)
cape_store_rect = cape_store.get_rect(topleft=cape_store_position)


#this will be the third building
cape_port = pygame.image.load('graphics/castseaport.png')
cape_port_position = (1505, 384)
cape_port_rect = cape_port.get_rect(topleft=cape_port_position)


#this could be a structure like a well or gates
cape_passgate = pygame.image.load ('graphics/passgate.png')
cape_passgate_position = (16,700)
cape_passgate_rect = cape_passgate.get_rect(topleft=cape_passgate_position)


#this is a structure for the PASSAGES AREA
cape_entrygate = pygame.image.load('graphics/towngate.png')
cape_entrygate_position =  (400, 10)
cape_entrygate_rect = cape_entrygate.get_rect(midleft=cape_entrygate_position)


#this will be the entry gate into the ruins area
ancient_ruins_gate = pygame.image.load('graphics/ruinsgate.png')
ancient_ruins_gate_position = (screen_width // 2, 2200)
ancient_ruins_gate_rect = ancient_ruins_gate.get_rect(midleft=ancient_ruins_gate_position)


#
#
#THIS IS THE FIRST GUI FOR THE GAME
player_scoreboard = pygame.image.load('graphics/firstgui.png')
player_scoreboard_position = (screen_width // 2, 800)
player_scoreboard_rect = player_scoreboard.get_rect(center=player_scoreboard_position)
#
#

#END OF GUI LOAD
#
#
#


#This will be the first enemy introduced into the game inside of the PASSAGES area
earth_slime_image = pygame.image.load('graphics/earthslime.png')
earth_slime_position = (random.randint(0, passages_width), random.randint(0, passages_height))

earth_slime_rect = earth_slime_image.get_rect(center = earth_slime_position)
earth_slime_speed = 1



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

        if interact == True:
            interact = False
        

        
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
            player_y = min(player_y, camera_y + screen_height - player_height - 32)


        # Listen for Esc key press to return to the menu state
        if keys[K_ESCAPE]:
            current_state = MENU


        if keys[K_SPACE]:
            interact = True

        # Key released event handling
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                interact = False

        
        

            # Update camera position based on player's position
        camera_x = player_x - screen_width // 2
        camera_y = player_y - screen_height // 2

        # Clamp camera position to stay within the world boundaries
        camera_x = max(0, min(camera_x, game_world_width - screen_width))
        camera_y = max(0, min(camera_y, game_world_height - screen_height - 28 ))

        # Render the visible portion of the tilemap based on camera position
        start_row = camera_y // TILE_SIZE
        end_row = min(start_row + (screen_height // TILE_SIZE) + 1, GAME_MAP_SIZE_Y)
        start_col = camera_x // TILE_SIZE
        end_col = min(start_col + (screen_width // TILE_SIZE) + 1, GAME_MAP_SIZE_X)

            


        pass






    elif current_state == PASSAGES:


        
        #passages variables and logic
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
            player_y = min(player_y, camera_y + screen_height - player_height - 32)


        # Listen for Esc key press to return to the menu state
        if keys[K_ESCAPE]:
            current_state = MENU


        if keys[K_SPACE]:
            interact = True

        # Key released event handling
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                interact = False


            # Update camera position based on player's position
        camera_x = player_x - screen_width // 2
        camera_y = player_y - screen_height // 2

        # Clamp camera position to stay within the world boundaries
        camera_x = max(0, min(camera_x, passages_width - screen_width))
        camera_y = max(0, min(camera_y, passages_height - screen_height - 28 ))

        # Render the visible portion of the tilemap based on camera position
        start_row = camera_y // TILE_SIZE
        end_row = min(start_row + (screen_height // TILE_SIZE) + 1, PASSAGES_MAP_SIZE_Y)
        start_col = camera_x // TILE_SIZE
        end_col = min(start_col + (screen_width // TILE_SIZE) + 1, PASSAGES_MAP_SIZE_X)

            

        pass

        




    elif current_state == THERUINS:
        #this is going to be intended as the core of the gameplay
        #The Ruins variables and logic
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
            player_y = min(player_y, camera_y + screen_height - player_height - 32)



        # Listen for Esc key press to return to the menu state
        if keys[K_ESCAPE]:
            current_state = MENU



        if keys[K_SPACE]:
            interact = True


        # Key released event handling
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                interact = False




            # Update camera position based on player's position
        camera_x = player_x - screen_width // 2
        camera_y = player_y - screen_height // 2

        # Clamp camera position to stay within the world boundaries
        camera_x = max(0, min(camera_x, ruins_width - screen_width))
        camera_y = max(0, min(camera_y, ruins_height - screen_height - 28 ))

        # Render the visible portion of the tilemap based on camera position
        start_row = camera_y // TILE_SIZE
        end_row = min(start_row + (screen_height // TILE_SIZE) + 1, RUINS_MAP_SIZE_Y)
        start_col = camera_x // TILE_SIZE
        end_col = min(start_col + (screen_width // TILE_SIZE) + 1, RUINS_MAP_SIZE_X)

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
        menu_caption_text = font.render("Cape Castsea: The Ruins", True, menu_text_color)
        menu_caption_text_rect = menu_caption_text.get_rect(center=(screen_width // 4, 50))  # Center the text slightly towards the left side
        screen.blit(menu_caption_text, menu_caption_text_rect)

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
        
        # Render game elements
        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                tile_type = tilemap[row][col]

                tile_x, tile_y = col * TILE_SIZE - camera_x, row * TILE_SIZE - camera_y

                # Rendering ground tiles
                if tile_type == GROUND:
                    screen.blit(ground_tile, (tile_x, tile_y))


                    #temp-perm fix ona thing
                    cape_passgate_position = (16,700)
                    cape_passgate_rect = cape_passgate.get_rect(topleft=cape_passgate_position)


                # Rendering sand tiles
                elif tile_type == SAND:
                    screen.blit(sand_tile, (tile_x, tile_y))
                # Rendering water tiles
              
                # Check for border tiles
                if row == 0 or row == GAME_MAP_SIZE_Y - 1 or col == 0 or col == GAME_MAP_SIZE_X - 1:
                    screen.blit(tree_border_tile, (tile_x, tile_y))


        #rendering a base of sand tiles at the right side of the screen
        for row in range(start_row, end_row):
            for col in range(GAME_MAP_SIZE_X - 10, GAME_MAP_SIZE_X):  # Rendering the last 10 columns as water tiles
                tile_x, tile_y = col * TILE_SIZE - camera_x, row * TILE_SIZE - camera_y
                screen.blit(sand_tile, (tile_x, tile_y))


        # Render the last few columns as water tiles
        for row in range(start_row, end_row):
            for col in range(GAME_MAP_SIZE_X - 7, GAME_MAP_SIZE_X):  # Rendering the last 10 columns as water tiles
                tile_x, tile_y = col * TILE_SIZE - camera_x, row * TILE_SIZE - camera_y
                screen.blit(sea_tile, (tile_x, tile_y))
                
        

        # Ensure player can only walk on ground tiles
        player_tile_row = (player_y + player_height // 2) // TILE_SIZE
        player_tile_col = (player_x + player_width // 2) // TILE_SIZE


        if tilemap[player_tile_row][player_tile_col] == WATER:
            # If the player is standing on water, prevent movement
            # You can adjust this to handle player movement based on surrounding tiles if needed
            player_x, player_y = prev_player_x, prev_player_y  # Revert to previous position

        # Update previous player position for collision detection
        prev_player_x, prev_player_y = player_x, player_y


        # Render player
        pygame.draw.rect(screen, (255, 255, 255), (player_x - camera_x, player_y - camera_y, player_width, player_height))

        



        #THIS IS INSIDE OF THE RENDERING PART OF THE GAME LOOP
        #
        #THIS IS THE GUI FOR THE ACTIVE GAME RENDERING
        #change this so it moves with the player across the screen instead of being static. also make a binding, preferably tab or e
        screen.blit(player_scoreboard, player_scoreboard_rect)
         #placing this text to represent the player's gold, health and mana onto the GUI in game
        #player_scoreboard_position = (screen_width // 2, 800) that is the location of the scoreboard 
        #Displays player's gold
        player_gold_text = GUI_font.render("G: " + str(player_gold), True, WHITE_TEXT)
        player_gold_text_rect = player_gold_text.get_rect(topleft=(500, 800))  # Position the text at the top-left corner
        screen.blit(player_gold_text, player_gold_text_rect)

        #Displays player's health
        player_health_text = GUI_font.render("Health: " + str(player_health), True, WHITE_TEXT)
        player_health_text_rect = player_health_text.get_rect(topleft=(800, 800))  # Position the text below player gold
        screen.blit(player_health_text, player_health_text_rect)

        #Displays player's mana
        player_mana_text = GUI_font.render("Mana: " + str(player_mana), True, WHITE_TEXT)
        player_mana_text_rect = player_mana_text.get_rect(topleft=(1100, 800))  # Position the text below player health
        screen.blit(player_mana_text, player_mana_text_rect)

        #END OF THE GUI AND GUI RELATED VARIABLES


        #render the first capehouse
        screen.blit(cape_house, (cape_house_position[0] - camera_x, cape_house_position[1] - camera_y))


        #rendering the capestore
        screen.blit(cape_store,(cape_store_position[0] - camera_x, cape_store_position[1] - camera_y))
 

        #rendering the cape castsea port or third building
        screen.blit(cape_port, (cape_port_position[0]- camera_x, cape_port_position[1] - camera_y))


        #this structure allows the player to enter the next area called the passages
        screen.blit(cape_passgate, (cape_passgate_position[0]- camera_x, cape_passgate_position[1] - camera_y))



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



            #here I am going to replicate the code for the capehouse but for the capestore
                
        if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(cape_store_rect):
            if player_x < cape_store_rect.left:
                player_x = cape_store_rect.left - player_width

            elif player_x > cape_store_rect.right - player_width:
                player_x = cape_store_rect.right

            if player_y < cape_store_rect.top:
                player_y = cape_store_rect.top - player_height

            elif player_y > cape_store_rect.bottom - player_height:
                player_y = cape_store_rect.bottom


            #here is the collision for the cape port and player
                
        if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(cape_port_rect):
            if player_x < cape_port_rect.left:
                player_x = cape_port_rect.left - player_width

            elif player_x > cape_port_rect.right - player_width:
                player_x = cape_port_rect.right

            if player_y < cape_port_rect.top:
                player_y = cape_port_rect.top - player_height

            elif player_y > cape_port_rect.bottom - player_height:
                player_y = cape_port_rect.bottom





        #here I am going to implement a collision action with the passgate to allow the player into another area of the game which will serve as a buffer between the town and the ruins
        if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(cape_passgate_rect):
            if interact:
                # Check conditions and perform interact actions
                player_x, player_y = screen_width // 2, screen_height // 2

                current_state = PASSAGES





    # Draw game elements
    
    #this handles what get's displayed during the rendering of The Passages
    elif current_state == PASSAGES:

        


        screen.fill((0, 0, 0))  # Clear the screen
        # Render game elements
          # Rendering the ground tiles
        # Rendering the ground and water tiles
    
        
            
        # Render game elements
        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                tile_type = passages_tilemap[row][col]

                tile_x, tile_y = col * TILE_SIZE - camera_x + 200, row * TILE_SIZE - camera_y

                # Rendering ground tiles
                if tile_type == GROUND:
                    screen.blit(ground_tile, (tile_x, tile_y))
                
              
                # Check for border tiles
                if row == 0 or row == PASSAGES_MAP_SIZE_Y - 1 or col == 0 or col == PASSAGES_MAP_SIZE_X - 1:
                    screen.blit(tree_border_tile, (tile_x, tile_y))




        

        
        

        # Ensure player can only walk on ground tiles
        player_tile_row = (player_y + player_height // 2) // TILE_SIZE
        player_tile_col = (player_x + player_width // 2) // TILE_SIZE



        
        #THIS IS INSIDE OF THE RENDERING PART OF THE PASSAGES LOOP
        #
        #THIS IS THE GUI FOR THE ACTIVE PASSAGES RENDERING
        #change this so it moves with the player across the screen instead of being static. also make a binding, preferably tab or e
        screen.blit(player_scoreboard, player_scoreboard_rect)
         #placing this text to represent the player's gold, health and mana onto the GUI in game
        #player_scoreboard_position = (screen_width // 2, 800) that is the location of the scoreboard 
        #Displays player's gold
        player_gold_text = GUI_font.render("G: " + str(player_gold), True, WHITE_TEXT)
        player_gold_text_rect = player_gold_text.get_rect(topleft=(500, 800))  # Position the text at the top-left corner
        screen.blit(player_gold_text, player_gold_text_rect)

        #Displays player's health
        player_health_text = GUI_font.render("Health: " + str(player_health), True, WHITE_TEXT)
        player_health_text_rect = player_health_text.get_rect(topleft=(800, 800))  # Position the text below player gold
        screen.blit(player_health_text, player_health_text_rect)

        #Displays player's mana
        player_mana_text = GUI_font.render("Mana: " + str(player_mana), True, WHITE_TEXT)
        player_mana_text_rect = player_mana_text.get_rect(topleft=(1100, 800))  # Position the text below player health
        screen.blit(player_mana_text, player_mana_text_rect)

        #END OF THE GUI AND GUI RELATED VARIABLES



        

        # Render player
        pygame.draw.rect(screen, (255, 255, 255), (player_x - camera_x, player_y - camera_y, player_width, player_height))
        pass



        #rendering the entry gate to the town area
        screen.blit(cape_entrygate, (cape_entrygate_position[0] - camera_x, cape_entrygate_position[1] - camera_y))


        #rendering the ancient gate onto the passages area
        screen.blit(ancient_ruins_gate, (ancient_ruins_gate_position[0] - camera_x, ancient_ruins_gate_position[1] - camera_y))


        #here I want to render my earthslime image into the passages area and handle a simple detection where if player_rect_x <= earth_slime_image_rect - 300: earthslime_rect_x, earthslime, so on...
        screen.blit(earth_slime_image, (earth_slime_position[0] - camera_x, earth_slime_position[1] - camera_y))
        #this is where I want to introduce the collision detection and follow logic similar to my other game slime ranger
        # distance = abs(player.players_rect.centerx - earth_slime_image_rect.centerx)
        #    if distance >= 50:
        #       earth_slime_position -= player_rect_position
        # Define distance threshold for enemy to start following player
        follow_threshold = 300

        # Calculate distance between player and enemy
        distance_to_player = ((player_x - earth_slime_position[0])**2 + (player_y - earth_slime_position[1])**2)**0.5

        # Check if player is within follow threshold distance
        if distance_to_player < follow_threshold:
            # Update enemy position based on player's position
            if player_x < earth_slime_position[0]:
                earth_slime_position = (earth_slime_position[0] - earth_slime_speed, earth_slime_position[1])
            elif player_x > earth_slime_position[0]:
                earth_slime_position = (earth_slime_position[0] + earth_slime_speed, earth_slime_position[1])

            if player_y < earth_slime_position[1]:
                earth_slime_position = (earth_slime_position[0], earth_slime_position[1] - earth_slime_speed)
            elif player_y > earth_slime_position[1]:
                earth_slime_position = (earth_slime_position[0], earth_slime_position[1] + earth_slime_speed)



        # Update earth slime rect after changing its position
        earth_slime_rect = earth_slime_image.get_rect(center=earth_slime_position)

        # Crude initial collision test with player object and enemy object
        if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(earth_slime_rect):
            player_health -= 1
            earth_slime_position = (random.randint(0, passages_width), random.randint(0, passages_height))
            



        #this code bit will handle collision logic between the player and the town gate allowing travelling between the two seemlessly
        if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(cape_entrygate_rect):
            if interact:
                # Check conditions and perform interact actions
                player_x, player_y = screen_width // 2, screen_height // 2

                current_state = GAME





          #this code bit will handle collision logic between the player and the ruins gate allowing travelling between the two seemlessly
        if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(ancient_ruins_gate_rect):
            if interact:
                # Check conditions and perform interact actions
                player_x, player_y = screen_width // 2, screen_height // 2

                current_state = THERUINS




        #attempting a different angle of collision for the player and environment in the passages instead of detecting collision 
        #between player and border tiles, just setting a crude minimum and maximum
        #minumim
        if player_x <= passages_width - 962:
            player_x += player_speed
            player_x = max(player_x, camera_x + player_width)


        #maximum
        if player_x >= passages_width + 96:
            player_x -= player_speed
            player_x = min(player_x, camera_x + screen_width - player_width-32)

            pass



    #this handles what get's displayed during the rendering of The Ruins
    elif current_state == THERUINS:
        


        screen.fill((0, 0, 0))  # Clear the screen
        # Render ruins game elements

       
        
        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                tile_type = ruins_tilemap[row][col]

                tile_x, tile_y = col * TILE_SIZE - camera_x , row * TILE_SIZE - camera_y

                # Rendering ground tiles
                if tile_type == ANCIENTRUINS:
                    screen.blit(ruins_tile, (tile_x, tile_y))

                     #changing these values specifically for the ruins
                    cape_passgate_position = (600,700)
                    cape_passgate_rect = cape_passgate.get_rect(topleft=cape_passgate_position)
                    
                
              
                # Check for border tiles
                if row == 0 or row == RUINS_MAP_SIZE_Y - 1 or col == 0 or col == RUINS_MAP_SIZE_X - 1:
                    screen.blit(tree_border_tile, (tile_x, tile_y))


        

        

        # Ensure player can only walk on ground tiles
        player_tile_row = (player_y + player_height // 2) // TILE_SIZE
        player_tile_col = (player_x + player_width // 2) // TILE_SIZE


        

        # Render player
        pygame.draw.rect(screen, (255, 255, 255), (player_x - camera_x, player_y - camera_y, player_width, player_height))

        #putting this inside of the ruins and using it to enter the passages
        screen.blit(cape_passgate, (cape_passgate_position[0]  -  camera_x, cape_passgate_position [1]  -   camera_y))





        #here I am going to implement a collision action with the passgate to allow the player into another area of the game which will serve as a buffer between the town and the ruins
        if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(cape_passgate_rect):
            if interact:
                # Check conditions and perform interact actions
                player_x, player_y = screen_width // 2, screen_height // 2

                current_state = PASSAGES






        pass





    #this handles what get's displayed during the rendering of options
    elif current_state == OPTIONS:
        screen.fill((25, 50, 65))  # Clear the screen
        # Draw menu elements

        # Example: Draw a white rectangle as a placeholder button
        fullscreen_rect = pygame.Rect(100, 100, 200, 50)  # (x, y, width, height) while named fullscreen it's the name of the rect itself, the text is below
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



