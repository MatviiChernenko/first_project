from data import *

class Human(pygame.Rect):
    def __init__(self,x,y,width,height,image_list,step):
        super().__init__(x,y,width,height)
        self.image_list = image_list
        self.image = self.image_list[0]
        self.image_now = self.image
        self.image_count = 0
        self.step = step

    def move_image(self):
        if self.image_count == len(self.image_list * 10) - 1:
            self.image_count = 0
        if self.image_count % 10 == 0:
            self.image = self.image_list[self.image_count // 10]
        self.image_count+=1

class Hero (Human):
    def __init__(self,x,y,width,height,image_list,step):
        super().__init__(x,y,width,height,image_list,step)
        self.walk = {"up":False,"down":False,"left":False,"right":False}
        self.side = False

    def move(self,window):
        if self.walk["up"] and self.y > 0:
            self.y -= self.step
            if self.collidelist(wall_list) != -1:
                self.y+=self.step
        if self.walk["left"] and self.x > 0:
            self.x -= self.step
            if self.collidelist(wall_list) != -1:
                self.x+=self.step
            self.side = True
        if self.walk["down"] and self.y < size_window[1]:
            self.y += self.step
            if self.collidelist(wall_list) != -1:
                self.y-=self.step
        if self.walk["right"] and self.x < size_window[0]:
            self.x += self.step
            if self.collidelist(wall_list) != -1:
                self.x-=self.step
            self.side = False

        for value in list(self.walk.values()):
            if value:
                self.move_image()
                break
        else:
            self.image = self.image_list[0]
        if self.side:
            self.image_now = pygame.transform.flip(self.image,True,False)
        else:
            self.image_now = self.image
        self.move_image()
        window.blit(self.image_now, (self.x, self.y)) 

class Snake (Human):
    def __init__(self,x,y,width,height,image_list,step):
        super().__init__(x,y,width,height,image_list,step)

    def move(self,window):  
        self.move_image()
        window.blit(self.image_now, (self.x, self.y)) 

class Slime (Human):
    def __init__(self,x,y,width,height,image_list,step):
        super().__init__(x,y,width,height,image_list,step)

    def move(self,window):  
        self.move_image()
        window.blit(self.image_now, (self.x, self.y)) 

class Gun (Human):
    def __init__(self,x,y,width,height,image_list,step):
        super().__init__(x,y,width,height,image_list,step)

    def move(self,window):  
        self.move_image()
        window.blit(self.image_now, (self.x, self.y))
        
class Wall(pygame.Rect):
    def __init__(self,x,y,width,height,color):
        super().__init__(x,y,width,height)
        self.color = color

def creat_wall(new_map):
    x,y = 0,0
    x1,y2 = 0,0
    width, height = 12,12
    for line in new_map:
        for elem in line:
            if elem == "1":
                wall_list.append(Wall(x,y,width,height,WHITE))
            x += width
        x = 0
        y += height
    for line in new_map:
        for elem in line:
            if elem == "2":
                wall_list.append(Wall(x1,y2,width,height,BLUE))
            x1 += width
        x1 = 0
        y2 += height

creat_wall(maps["LVL1"]["map"])