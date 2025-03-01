from function import *

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("MAZE")

clock = pygame.time.Clock()

hero = Hero(
    10,
    59,
    size_hero[0],
    size_hero[1],
    hero_image_list,
    3,
    3
)

snake = Snake(
    50,
    400,
    size_snake[0],
    size_snake[1],
    snake_image_list,
    5
)

slime = Slime(
    350,
    375,
    size_slime[0],
    size_slime[1],
    slime_image_list,
    4,
    "horizontal",
    radius= 155
)

slime1 = Slime(
    360,
    320,
    size_slime[0],
    size_slime[1],
    slime_image_list,
    8,
    "horizontal",
    radius= 145
)

gun = Gun(
    937,
    170,
    size_gun[0],
    size_gun[1],
    gun_image_list,
    0
)
gun1 = Gun(
    710,
    170,
    size_gun[0],
    size_gun[1],
    gun_image_list,
    0
)

fireball = Fireball(
    gun.x,
    gun.y - 5,
    size_fireball[0],
    size_fireball[1],
    fireball_image_list,
    3,
    "horizontal"
)

game = True
while game:
    events = pygame.event.get()
    window.fill(BLACK)
    #x,y = 0,0

    #for i in range(85):
     #   pygame.draw.line(window,WHITE, (0,y), (size_window[0], y))
      #  pygame.draw.line(window,WHITE, (x,0), (x, size_window[1]))
     #   x+=15
      #  y+=15

    hero.move(window)
    snake.move(window)
    slime.guardion(window)
    slime1.guardion(window)
    gun.move(window,fireball)
    gun1.move(window,fireball)
      
    for wall in wall_list:
        pygame.draw.rect(window,wall.color,wall)

    for event in events:
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hero.walk["up"] = True
            if event.key == pygame.K_s:
                hero.walk["down"] = True
            if event.key == pygame.K_a:
                hero.walk["left"] = True
            if event.key == pygame.K_d:
                hero.walk["right"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                hero.walk["up"] = False
            if event.key == pygame.K_s:
                hero.walk["down"] = False
            if event.key == pygame.K_a:
                hero.walk["left"] = False
            if event.key == pygame.K_d:
                hero.walk["right"] = False


    clock.tick(FPS)
    pygame.display.flip()