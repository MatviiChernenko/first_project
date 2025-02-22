from data import *

class Human(pygame.Rect):
    def __init__(self,x,y,width,height,image_list,step):
        super().__init__(x,y,width,height)
        self.image_list = image_list
        self.image = self.image_list[0]
        self.image_now = self.image
        self.image_count = 0

    def move_image(self):
        if self.image_count == len(self.image_list * 10) - 1:
            self.image_count = 0
        if self.image_count % 10 == 0:
            self.image = self.image_list[self.image_count // 10]
        self.image_count+=1

class Hero (Human):
    def __init__(self,x,y,width,height,image_list,step):
        super().__init__(x,y,width,height,image_list,step)

    def move(self,window):
        self.move_image()
        window.blit(self.image, (self.x, self.y)) 

class Wall(pygame.Rect):
    def __init__(self,x,y,width,height,color):
        super().__init__(x,y,width,height)
        self.color = color

def creat_wall(new_map):
    x,y = 0,0
    width, height = 15,15
    for line in new_map:
        for elem in line:
            if elem == "1":
                wall_list.append(Wall(x,y,width,height,WHITE))
            x += width
        x = 0
        y += height
def creat_wall2(new_map):
    x,y = 0,0
    width, height = 15,15
    for line in new_map:
        for elem in line:
            if elem == "2":
                wall_list.append(Wall(x,y,width,height,BLUE))
            x += width
        x = 0
        y += height
creat_wall(maps["LVL1"]["map"])
creat_wall2(maps["LVL1"]["map"])
