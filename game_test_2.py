import pygame
import random
import sys

pygame.init()

width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Игра с красными кругами")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


def draw_circle(x, y, radius):
    pygame.draw.circle(screen, RED, (x, y), radius)

hit_sound = pygame.mixer.Sound("hit_sound.wav")


radius = int(input("Введите радиус круга: "))
second_number = int(input("Введите частоту появления кругов (мс): "))

circles = []
clock = pygame.time.Clock()
last_circle_time = 0 
score = 0
total_attempts = 0
font = pygame.font.Font(None, 25)

while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if score >= 1:
                print('Счёт:',score, ',', 'Точность:',f"{accuracy:.2f}",'%')
                pygame.quit()
                sys.exit()
            else:
                pygame.quit()
                sys.exit()
            
        #Проверка нажатия на круг
        if event.type == pygame.MOUSEBUTTONDOWN:
            total_attempts += 1
            mouse_x, mouse_y = event.pos
            for circle in circles:
                if (mouse_x - circle['x'])**2 + (mouse_y - circle['y'])**2 <= (radius)**2:
                    circles.remove(circle)
                    score += 1  
                    hit_sound.play()
            break
            
    #Рисование кругов       
    current_time = pygame.time.get_ticks()
    if current_time - last_circle_time > second_number: 
        last_circle_time = current_time 

        #Проверка на проигрышь
        if len(circles) < 5:  
            x = random.randint(radius, width - radius)
            y = random.randint(radius, height - radius)
            circles.append({'x': x, 'y': y})
        else:
            if score >= 1:
                print('Счёт:',score, ',', 'Точность:',f"{accuracy:.2f}",'%')
                pygame.quit()
                sys.exit()
            else:
                print('Вы проиграли, больше 5 кругов на поле!')
                pygame.quit()
                sys.exit()

    
    for circle in circles:
        draw_circle(circle['x'], circle['y'], radius)

    #Точность
    if total_attempts > 0:
          accuracy = (score / total_attempts) * 100  
          accuracy_text = f"Accuracy: {accuracy:.2f}%"
    else:
          accuracy_text = "Accuracy: N/A"

    #Текст на экране
    score_text = font.render(f'Score: {score}', True, BLACK)
    accuracy_rendered = font.render(accuracy_text, True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(accuracy_rendered, (10, 30))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(30)
