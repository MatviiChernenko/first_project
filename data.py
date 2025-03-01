import pygame
import os

pygame.init()

size_window = (1248,505)
size_hero = (25,25)
size_snake = (25,85)
size_slime = (25,20)
size_gun = (28,45)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (107, 52, 235)

FPS = 60

wall_list = list()

abs_path = os.path.abspath(__file__+"/..")
hero_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path,"image", "hero1.png")),size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path,"image", "hero2.png")),size_hero)
]
snake_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path,"image", "snake1.png")),size_snake),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path,"image", "snake2.png")),size_snake)
]
slime_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path,"image", "slime1.png")),size_slime),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path,"image", "slime2.png")),size_slime)
]
gun_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path,"image", "gun1.png")),size_gun),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path,"image", "gun2.png")),size_gun)
]


maps = {
    "LVL1":{
        "map":["11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
               "00000000000000000000000000000000000000000000000000000000000010000000000010000000000010000000000000000001",
               "00000000000000000000000000000000000000000000000000000000000010000000000010000000000010000000000000000001",
               "00000000000000000000000000000000000000000000000000000000000020000000000020000000000020000000000000000001",
               "00000000000000000000000000000000000000000000000000000020000000000020000000000020000000000020000000000001",
               "00000000000000000000000000000000000000000000000000000010000000000010000000000010000000000010000000000001",
               "00000000000000000000000000000000000000000000000000000010000000000010000000000010000000000010000000000001",
               "11111111111111111111111111111111111112000002111111111111111111111111111111111111111111111111112000000021",
               "10000000000002000000000000111111111112000002110000000000000000000000000000000000000000000000012220000021",
               "10000000000000000000000000111111111112000002110000000000000000000000000000000000000000000000011111000021",
               "10000000000000000000000000111111111112000002110000000000000000000000000000000000000000000000012000000021",
               "10000000000000000000000000111111111112000002110000000000000000000000000000000000000000000000012000000021",
               "10000000000002000000000000111111111112000002110000000000000000000000000000000000000000000000012000000021",
               "11200000211111111112000211111111111112000002111200000211111111111111111111111111111100000000012000002221",
               "10000000001111111112000211111111111112000002112000000021000000000011111111100000000100000000012000011111",
               "10000000001111111120000021111111111112000002112000000021000000000011111111100000000100000000012000000021",
               "10000000001111111120000021111111111112000002112000000021000000000011111111100000000100000000012000000021",
               "10000000001111111120000021111111111112000002112000000021000000000011111111100000000100000000012000000021",
               "10000000001111111120000021111111111112000002112000000021000000000011111111100000000100000000012000000021",
               "10000000001111111120000021111111111112000002112000000021000000000011111111100000000100000000012220000021",
               "10000000001111111200000002111111111112000002112000000021000000000011111111100000000100000000011111000021",
               "10000000001111111200000002111111111112000002112000000021000000000011111111100000000100000000012000000021",
               "10000000001111111200000002111111111112000002112000000021000000000000000000000000000100000000012000000021",
               "10000000001111111200000002111111111112000002112000000021000000000000000000000000000100000000012000000021",
               "10000000001111111000000000000000000000000000012000000021000000000000000000000000000100000000012000002221",
               "10000000001111111000000000000000000000000000012000000021000000000000000000000000000100000000012000011111",
               "10000000001111111000000000000000000000000000012000000021000000000000000000000000000100000000012000000021",
               "10000000001111111000000000000000000000000000012000000021000000000011111111100000000100000000012000000021",
               "10000000001111111000000000000000000000000000012000000021000000000011111111100000000100000000012000000021",
               "10000000001111111000000000000000000000000000012000000021000000000011111111100000000100000000012220000021",
               "10000000001111111000000000000000000000000000012000000021000000000000000000100000000000000000011111000021",
               "10000000001111111000000000000000000000000000012000000021000000000000000000100000000000000000012000000021",
               "10000000001111111000000000000000000000000000012000000021000000000000000000100000000000000000012000000021",
               "11200000211111111111111111111111111111111111111200000211000000000000000000100000000000000000012000000021",
               "10000000000100000000000000000010000000000000000000000001222222222200000000100000000000000000011120002111",
               "10000000000100000000000000000010000000000000000000000001111111111100000000111111111111111111111120002111",
               "10000000000100000000000000000010000000000000000000000001111111111100000000110000000000000000000000000001",
               "10000000000200000000020000000020000000020000000000000001111111111100000000110000000000000000000000000001",
               "10000000000000000000010000000000000000010000000000000001111111111100000000110000000000000000000000000001",
               "10000000000000000000010000000000000000010000000000000001111111111100000000110000000000000000000002222221",
               "10000000000000000000010000000000000000010000000000000001111111111100000000110000000000000000000002221111",
               "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",]
    }
}