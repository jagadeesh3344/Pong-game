import pygame,sys

def animate_cpu():
    global cpu_speed
    cpu.y += cpu_speed

    if ball.centery == cpu.centery:
        cpu_speed = 0
    elif ball.centery < cpu.centery:
        cpu_speed = -6
    elif ball.centery > cpu.centery:
        cpu_speed = 6

    if cpu.top <= 0:
        cpu.top = 0
    if cpu.bottom >= screen_height:
        cpu.bottom = screen_height

##init game
pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pong Game!")
clock = pygame.time.Clock()

ball = pygame.Rect(0,0,30,30)
ball.center = (screen_width/2, screen_height/2)

cpu = pygame.Rect(0,0,20,100)
cpu.centery = screen_height/2


cpu_speed = 6

while True:
    #Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    animate_cpu()
        
    #Clear the screen
    screen.fill('black')

    #Draw the score
    
    
    #Draw the game objects
    pygame.draw.aaline(screen,'white',(screen_width/2, 0), (screen_width/2, screen_height))
    pygame.draw.ellipse(screen,'white',ball)
    pygame.draw.rect(screen,'white',cpu)
    
    #Update the display
    pygame.display.update()
    clock.tick(60)

