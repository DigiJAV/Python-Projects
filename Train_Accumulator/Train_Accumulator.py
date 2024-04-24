import numpy as np
import random
import pygame
import os
from dataclasses import dataclass
   
@dataclass
class Object:
    object_box: pygame.Rect
    image_id: int

@dataclass
class Train:
    direction: str
    train_box: pygame.Rect
    train_surface: pygame.Surface

def add_train_zero(train_list: list[Train], obstacle_list: list[Object], node_list: list[Object]):
    """Constructs first instance of Train, train0. Assigns random values within defined parameters to the position."""
    #train_direction.direction = DIRECTION_VALUES[np.random.randint(3)]  #Assign random direction value
    coord = generate_random_coord(TEXT_SPACE)
    col = coord[0]
    row = coord[1]
    if pygame.Rect(col, row, CELL_SIZE, CELL_SIZE).collidelist([node.object_box for node in node_list]) == -1 and pygame.Rect(col, row, CELL_SIZE, CELL_SIZE).collidelist([obstacle.object_box for obstacle in obstacle_list]) == -1 and col != -CELL_SIZE and col != SURFACE_WIDTH and row != -CELL_SIZE and row != SURFACE_LENGTH:
        train0_box = pygame.Rect(col,row, CELL_SIZE, CELL_SIZE)
        train0_surface = pygame.Surface((CELL_SIZE, CELL_SIZE))
        train0 = Train("None", train0_box, train0_surface)
        train_list.append(train0)
    
   
def update_direction(train_list: list[Train], key: pygame.event):
    """Will take user input via arrow keys."""
    if key == pygame.K_LEFT:
        if len(train_list) == 1:
            train_list[0].direction = "Left"
        elif len(train_list) > 1 and train_list[0].direction != "Right":
            train_list[0].direction = "Left"
    
    elif key == pygame.K_RIGHT:
        if len(train_list) == 1:
            train_list[0].direction = "Right"
        elif len(train_list) > 1 and train_list[0].direction != "Left":
            train_list[0].direction = "Right"

    elif key == pygame.K_DOWN:
        if len(train_list) == 1:
            train_list[0].direction = "Down"
        elif len(train_list) > 1 and train_list[0].direction != "Up":
            train_list[0].direction = "Down"

    elif key == pygame.K_UP:
        if len(train_list) == 1:
            train_list[0].direction = "Up"    
        elif len(train_list) > 1 and train_list[0].direction != "Down":
            train_list[0].direction = "Up"

def update_position(train0: Train):
    """Updates position of train0 by adding or subtracing amount = train_dimension to its row or col value, depending on its direction. """
    if train0.direction == 'Up':
        train0.train_box.move_ip(0,-CELL_SIZE)
    elif train0.direction == 'Down':
        train0.train_box.move_ip(0,CELL_SIZE)
    elif train0.direction == 'Left':
        train0.train_box.move_ip(-CELL_SIZE,0)
    elif train0.direction == 'Right':
        train0.train_box.move_ip(CELL_SIZE,0)

def check_position(train_list: list[Train], node_list: list[Object], obstacle_list: list[Object]):
    """ Checks the position of train0. 
        If it == to obstacle, or train, or screen edge position, return 1.
        If it == to node position, return 2. 
        If neither, return 0."""  
    if train_list[0].train_box.collidelist([obstacle.object_box for obstacle in obstacle_list]) != -1 or train_list[0].train_box.collidelist([train.train_box for train in train_list[1:]]) != -1 or  train_list[0].train_box.x == -CELL_SIZE or train_list[0].train_box.x == SURFACE_WIDTH or train_list[0].train_box.y == -CELL_SIZE or train_list[0].train_box.y == SURFACE_LENGTH:
            return 1
    if train_list[0].train_box.collidelist([node.object_box for node in node_list]) != -1:
            return 2
    else:
        return 0 

def add_train(train_list: list[Train]):
    """Contructs instance of Train, appends it to train list."""                                              
    train_box = pygame.Rect(-CELL_SIZE,-CELL_SIZE, CELL_SIZE, CELL_SIZE)
    train_surface = pygame.Surface((CELL_SIZE, CELL_SIZE))
    train_list.append(Train("None", train_box, train_surface))

"""def add_train_connection(train_number: int, train_list:list[pygame.Rect], train_connection_list: list[Train_Connection]):

    "Creates train_connection instance using train1 and train2 inputs. Names the train_connection with number ID using train_number input.
    Appends created train_connection to train_connection_list"
    train_connection = f"train_connection{train_number}"
    exec(f"{train_connection} = {Train_Connection(train_list[train_number-1], train_list[train_number])}")
    train_connection_list.append(train_connection)
"""

def update_train_values(train_list: list[Train]):
    """Updates position values of each train based on position of train after it. Updates position and direction of train0."""
    if len(train_list) > 1:
        for index in range(len(train_list)-1):
            col = list(train_list)[::-1][index+1].train_box.x
            row = list(train_list)[::-1][index+1].train_box.y
            direction = list(train_list)[::-1][index+1].direction
            list(train_list)[::-1][index].train_box.x = col
            list(train_list)[::-1][index].train_box.y = row
            list(train_list)[::-1][index].direction = direction
    update_position(train_list[0])

def remove_symbol(surface, col, row):
    """Replaces symbol in given coords in matrix with '.'."""
    surface[col][row] = '.'

def generate_nodes(node_list: list[Object], obstacle_list: list[Object], train_list: list[Train]):
    """Creates node object instances. Number of nodes determined by ROW, COL, and NODE_RATE contants. Will generate objects until 
    desired number reached. Checks row and col to avoid placing node on a train, obstacle, or other node."""
    while len(node_list) < SURFACE_LENGTH*SURFACE_WIDTH*NODES_RATE:
        for node_number in range(int(SURFACE_LENGTH*SURFACE_WIDTH*NODES_RATE) - len(node_list)):      #If number of objects less than desired, generate objects until satisfied
            coord = generate_random_coord(TEXT_SPACE)
            col = coord[0]
            row = coord[1]
            if pygame.Rect(col, row, CELL_SIZE, CELL_SIZE).collidelist([node.object_box for node in node_list]) == -1 and pygame.Rect(col, row, CELL_SIZE, CELL_SIZE).collidelist([obstacle.object_box for obstacle in obstacle_list]) == -1 and pygame.Rect(col, row, CELL_SIZE, CELL_SIZE).collidelist([train.train_box for train in train_list]) == -1:
                node_box = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
                image_id = 0
                node_list.append(Object(node_box, image_id))
                                     
def generate_obstacles(obstacle_list: list[Object], node_list: list[Object], train_list: list[Train]):
    """Creates obstacle object instances. Number of nodes determined by ROW, COL, and NODE_RATE contants. Will generate objects until 
    desired number reached. Checks row and col to avoid placing obstacle on top of a train, node, or other obstacle."""
    while len(obstacle_list) < SURFACE_LENGTH*SURFACE_WIDTH*OBSTACLES_RATE:
        for obstacle_number in range(int(SURFACE_LENGTH*SURFACE_WIDTH*OBSTACLES_RATE) - len(obstacle_list)):  #If number of objects less than desired, generate objects until satisfied
            coord = generate_random_coord(TEXT_SPACE)
            col = coord[0]
            row = coord[1]
            if pygame.Rect(col, row, CELL_SIZE, CELL_SIZE).collidelist([node.object_box for node in node_list] ) == -1 and pygame.Rect(col, row, CELL_SIZE, CELL_SIZE).collidelist([obstacle.object_box for obstacle in obstacle_list]) == -1 and pygame.Rect(col, row, CELL_SIZE, CELL_SIZE).colliderect(train_list[0].train_box) != True:
                obstacle_box = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
                image_id = generate_random_int(0,2)
                obstacle_list.append(Object(obstacle_box, image_id))
                
def place_nodes(surface: pygame.Surface, node_list: list[Object], node_image_list: list[pygame.Surface]):
    """Places growth nodes at random points in the matrix. Default number of nodes: 1% of total matrix poins."""
    for node in node_list:
        pygame.draw.rect(surface, NODE_COLOR, node.object_box, width=0)
        object_surface = pygame.Surface((CELL_SIZE, CELL_SIZE))
        object_surface.blit(node_image_list[node.image_id], (0,0))
        surface.blit(object_surface, (node.object_box.x, node.object_box.y))

def place_obstacles(surface: pygame.Surface, obstacle_list: list[Object], obstacle_image_list: list[pygame.Surface]):
    """Places obstacles at random points in the matrix."""
    for obstacle in obstacle_list:
            pygame.draw.rect(surface, OBSTACLE_COLOR, obstacle.object_box, width=0)
            obstacle_surface = pygame.Surface((CELL_SIZE, CELL_SIZE))
            obstacle_surface.blit(obstacle_image_list[obstacle.image_id], (0,0))
            surface.blit(obstacle_surface, (obstacle.object_box.x, obstacle.object_box.y))
            
def place_trains(surface: pygame.Surface, train_list: list[Train], train0_image_list: list[pygame.Surface], train_image_list: list[pygame.Surface]):
    """Draws train rectangles from train box list into main game surface. Blits train surfaces from train surface list into main game surface,
    on same location as the respective train box."""
    for index in range(len(train_list)):
        if train_list[index].direction == "Up" or train_list[index].direction == "None":
            if index == 0:
                train_list[index].train_surface.blit(train0_image_list[0],(0,0))
            else:
                train_list[index].train_surface.blit(train_image_list[0],(0,0))
        elif train_list[index].direction == "Down":
            if index == 0:
                train_list[index].train_surface.blit(train0_image_list[1],(0,0))
            else:
                train_list[index].train_surface.blit(train_image_list[1],(0,0))
        elif train_list[index].direction == "Right":
            if index == 0:
                train_list[index].train_surface.blit(train0_image_list[2],(0,0))
            else:
                train_list[index].train_surface.blit(train_image_list[2],(0,0))
        elif train_list[index].direction == "Left":
            if index == 0:
                train_list[index].train_surface.blit(train0_image_list[3],(0,0))
            else:
                train_list[index].train_surface.blit(train_image_list[3],(0,0))
        pygame.draw.rect(surface, TRAIN_COLOR, train_list[index].train_box, width=0)
        surface.blit(train_list[index].train_surface, (train_list[index].train_box.x, train_list[index].train_box.y))

def generate_random_int(min_val:int, max_val:int):
    """Returns a random int within the parameters in argument."""
    return random.randint(min_val,max_val)

def generate_random_coord(TEXT_SPACE: int):
    """Generates random coords within screen. Satisfies cell constraints."""
    while True:
        col = generate_random_int(0, SURFACE_WIDTH)   #Generate random col value
        row = generate_random_int(TEXT_SPACE, SURFACE_LENGTH)   #Generate random row value
        if col % CELL_SIZE == 0 and row % CELL_SIZE == 0:
            return (col, row)

def remove_node(node_list: list[Object], col: int, row: int):
    """Removes node with given col and row values."""
    for node in node_list:
        if node.object_box.x == col and node.object_box.y == row:
            node_list.remove(node)

def remove_all_nodes(node_list: list[pygame.Rect]):
    """Removes all nodes from node_list"""
    for node in node_list:
            node_list.remove(node)

def update_objects(train_list: list[Train], node_list: list[pygame.Rect], obstacle_list: list[pygame.Rect], train0_image_list: list[pygame.Surface], train_image_list: list[pygame.Surface], obstacle_image_list: list[pygame.Surface], node_image_list: list[pygame.Surface], sounds: list[pygame.mixer.Sound]):
    """Calls functions that update position and direction values of trains, and generate instances of nodes and obstacles to desired amount."""
    update_train_values(train_list)  #Update position and direction values of all trains, from back to front. Front train is updated via user input.
    check = check_position(train_list, node_list, obstacle_list)
    if check:
        if check == 1:
            """Code that shows user that train has crashed. Saves score. Start game over"""
            generate_score(train_list, screen) 
            place_objects(surface, train_list, obstacle_list, node_list, train0_image_list, train_image_list, obstacle_image_list, node_image_list)
            crash_Popup()
            screen.blit(surface,(0, TEXT_SPACE))
            sounds[0].stop()
            sounds[1].play()
            pygame.display.flip()
            pygame.time.delay(2000)
            sounds[1].stop()
            return 1
        elif check == 2:
            sounds[2].play()
            add_train(train_list)
            remove_node(node_list, train_list[0].train_box.x, train_list[0].train_box.y)  
            
    generate_nodes(node_list, obstacle_list, train_list)                   #Update nodes: generate new to desired amount
    generate_obstacles(obstacle_list, node_list, train_list)           #Update obstacles:  generate new to reach desired amount

def place_objects(screen: pygame.Surface, train_list: list[Train], obstacle_list: list[pygame.Rect], node_list: list[pygame.Rect], train0_image_list: list[pygame.Surface], train_image_list: list[pygame.Surface], obstacle_image_list: list[pygame.Surface], node_image_list: list[pygame.Surface]):
    """Places trains, nodes, and obstacles visually on given surface, using respective position values."""
    place_obstacles(screen, obstacle_list, obstacle_image_list)
    place_nodes(screen, node_list, node_image_list)
    place_trains(screen, train_list, train0_image_list, train_image_list)

def crash_Popup():
    """Generates popup text onto screen/game surface."""
    crash_text = popup_font.render("You Crashed!", True, (0,0,0))
    text_width, text_length = crash_text.get_size()
    popup.blit(crash_text, (POPUP_WIDTH/2 - text_width/2, POPUP_LENGTH/2 - text_length/2 ))
    surface.blit(popup, (SCREEN_WIDTH/2 - POPUP_WIDTH/2, SCREEN_LENGTH/2 - POPUP_LENGTH/2))
    
def generate_score(train_list: list[Train], screen: pygame.display):
    score = (len(train_list) - 1)*5
    text = score_font.render(f"Score: {score}", True, (237, 237, 201))
    screen.blit(text, (0, 0))

#Matrix parameters
TEXT_SPACE = 30
SCREEN_LENGTH = 800 + TEXT_SPACE
SCREEN_WIDTH = 1000
SURFACE_LENGTH = SCREEN_LENGTH - TEXT_SPACE
SURFACE_WIDTH = SCREEN_WIDTH
CELL_SIZE = 25
POPUP_LENGTH = 70
POPUP_WIDTH = 200
POPUP_COLOR = (253, 240, 0)
NODES_RATE = 0.0001           # % of matrix composed of nodes
OBSTACLES_RATE = 0.0001       # % of matrix composed of obstacles
DIRECTION_VALUES = ['Up','Down','Left','Right']
NODE_COLOR = (154, 151, 5)
OBSTACLE_COLOR = (40, 43, 40)
TRAIN_COLOR = (128, 67, 8)
FPS = 4                         #Frames per second

#pygame setup
running = True
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))

script_dir = os.path.dirname(os.path.abspath(__file__))   # Get the directory where the script is located
os.chdir(script_dir)                                                    # Set this directory as the current working directory
                                                    
#Loading of Images
surface = pygame.image.load(r"Train Accumulator Images\background\train_accumulator_Background0.jpg")
surface_copy = pygame.image.load(r"Train Accumulator Images\background\train_accumulator_Background0.jpg")    #For updating image surface per frame
train0_image_up = pygame.image.load(r"Train Accumulator Images\train0\train0_up.png")
train0_image_down = pygame.image.load(r"Train Accumulator Images\train0\train0_down.png")
train0_image_right = pygame.image.load(r"Train Accumulator Images\train0\train0_right.png")
train0_image_left = pygame.image.load(r"Train Accumulator Images\train0\train0_left.png")
train_image_up = pygame.image.load(r"Train Accumulator Images\carts\Cart low\cart_up.png")
train_image_down = pygame.image.load(r"Train Accumulator Images\carts\Cart low\cart_down.png")
train_image_right = pygame.image.load(r"Train Accumulator Images\carts\Cart low\cart_right.png")
train_image_left = pygame.image.load(r"Train Accumulator Images\carts\Cart low\cart_left.png")
node_image = pygame.image.load(r"Train Accumulator Images\Nodes\coin_topdown1.png")
obstacle1_image = pygame.image.load(r"Train Accumulator Images\Obstacles\obstacle1.png")
obstacle2_image = pygame.image.load(r"Train Accumulator Images\Obstacles\obstacle2.png")
obstacle3_image = pygame.image.load(r"Train Accumulator Images\Obstacles\obstacle3.png")
obstacle4_image = pygame.image.load(r"Train Accumulator Images\Obstacles\obstacle4.png")

#Scaling of Images
train0_image_up_c = pygame.transform.scale(train0_image_up, (CELL_SIZE, CELL_SIZE))
train0_image_down_c = pygame.transform.scale(train0_image_down, (CELL_SIZE, CELL_SIZE))
train0_image_right_c = pygame.transform.scale(train0_image_right, (CELL_SIZE, CELL_SIZE))
train0_image_left_c = pygame.transform.scale(train0_image_left,(CELL_SIZE, CELL_SIZE))

train_image_up_c = pygame.transform.scale(train_image_up, (CELL_SIZE, CELL_SIZE))
train_image_down_c = pygame.transform.scale(train_image_down, (CELL_SIZE, CELL_SIZE))
train_image_right_c = pygame.transform.scale(train_image_right, (CELL_SIZE, CELL_SIZE))
train_image_left_c = pygame.transform.scale(train_image_left, (CELL_SIZE, CELL_SIZE))

node1_image_c = pygame.transform.scale(node_image, (CELL_SIZE, CELL_SIZE))

obstacle1_image_c = pygame.transform.scale(obstacle1_image, (CELL_SIZE,CELL_SIZE))
obstacle2_image_c = pygame.transform.scale(obstacle2_image,(CELL_SIZE,CELL_SIZE))
obstacle3_image_c = pygame.transform.scale(obstacle3_image,(CELL_SIZE, CELL_SIZE))
obstacle4_image_c = pygame.transform.scale(obstacle4_image, (CELL_SIZE, CELL_SIZE))

#Image Lists
train0_images = [train0_image_up_c, train0_image_down_c, train0_image_right_c, train0_image_left_c]
train_images = [train_image_up_c, train_image_down_c, train_image_right_c, train_image_left_c]
obstacle_images = [obstacle1_image_c, obstacle2_image_c, obstacle3_image_c, obstacle4_image_c]
node_images = [node1_image_c]
images = [train0_images, train_images, obstacle_images, node_images]

#Load Sounds 
train_sound = pygame.mixer.Sound(r"Sounds\orecart_move_1.wav")
obstacle_sound = pygame.mixer.Sound(r"Sounds\train_crash2.wav")
node_sound = pygame.mixer.Sound(r"Sounds\picked-coin-echo.wav")
sounds = [train_sound, obstacle_sound, node_sound]
print("train_sound length: ",pygame.mixer.Sound.get_length(train_sound))

popup = pygame.Surface((POPUP_WIDTH, POPUP_LENGTH))
popup.fill(POPUP_COLOR)

score_font = pygame.font.Font(None, 30)
popup_font = pygame.font.Font(None, 36)
pygame.display.set_caption("Train Accumulator")

clock = pygame.time.Clock()
while (running):
    train_list = []
    node_list = []
    obstacle_list = []
    add_train_zero(train_list, obstacle_list, node_list)    #Initial train 
    generate_nodes(node_list, obstacle_list, train_list)
    generate_obstacles(obstacle_list, node_list, train_list)
    score_coin_surface = pygame.Surface((CELL_SIZE, CELL_SIZE))
    custom_event_type = pygame.USEREVENT + 1

    while (running):    #Secondary loop
        screen.fill("black")
        #surface.fill("white")
        surface.blit(surface_copy,(0, 0))
        
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:  
                update_direction(train_list, event.key)
            if event.type == custom_event_type:
                train_sound.play()

        if update_objects(train_list, node_list, obstacle_list, train0_images, train_images, obstacle_images, node_images, sounds) == 1:         # update_objects returns 1 if train crashes.
            break
        if train_list[0].direction != "None":
            if pygame.mixer.get_busy() == False:
                train_sound.play()
                pygame.time.set_timer(custom_event_type, 3700)
        generate_score(train_list, screen)
        place_objects(surface, train_list, obstacle_list, node_list, train0_images, train_images, obstacle_images, node_images)
        surface.blit(node1_image_c,(20,0))
        screen.blit(surface,(0, TEXT_SPACE))
        score_coin_surface.blit(node1_image_c, (0,0))
        screen.blit(score_coin_surface,(120,0))
        pygame.display.flip()
        clock.tick(FPS)  

pygame.quit()