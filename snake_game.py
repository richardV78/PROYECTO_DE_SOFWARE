import pygame, sys, time, random
# se importa una libreria de pyton para en su mayoria juegos
pygame.init() 

play_surface = pygame.display.set_mode((500, 500)) 
fps = pygame.time.Clock()

def food():
    random_pos = random.randint(0,49)*10
    food_pos = [random_pos, random_pos]
    return food_pos

def main():

    snake_pos = [100, 50]
    snake_body = [[100,50],[90,50],[80,50]]
    change = "RIGHT"
    run = True
    food_pos = food()
    score = 0

    while run: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change = "RIGHT"
                if event.key == pygame.K_LEFT:
                    change = "LEFT"
                if event.key == pygame.K_UP:
                    change = "UP"
                if event.key == pygame.K_DOWN:
                    change = "DOWN"
            
        if change == "RIGHT":
            snake_pos[0] += 10
        if change == "LEFT":
            snake_pos[0] -= 10
        if change == "UP":
            snake_pos[1] -= 10
        if change == "DOWN":
            snake_pos[1] += 10

        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            food_pos = food()
            scpre += 1 
            print(score)
        else: 
            snake_body.pop()


        play_surface.fill((0,0,0))
        
        for pos in snake_body:
            pygame.draw.rect(play_surface,(200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(play_surface,(169,6,6), pygame.Rect(food_pos[0], pos[1], 10, 10))
        
        pygame.display.flip()
        fps.tick(10)


main()
pygame.quit()
