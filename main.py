import random, math, pygame, sys
from pygame import mixer

global player_x_velocity, score_value, number_of_enemies
global player_x, bullet_x, bullet_y, bullet_state
global count,lvl
lvl = 0
TITLE = 'El jueguito de los marciano locos por José Conde '
GAME_OVER = 'GAME OVER LOSER'
YOU_WIN = 'YOU WIN'

count = 0

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600

ENEMY_X_VELOCITY = 4
ENEMY_Y_VELOCITY = 40
PLAYER_VELOCITY = 5

Tamaño_del_enemigo_x = 64
Tamaño_del_enemigo_y = 64

BULLET_READY_STATUS = 0
BULLET_FIRE_STATUS = 1

BACKGROUND_SOUND = "sonidito.wav"
LASER_SOUND = "laser.wav"
EXPLOSION_SOUND = "explosion.wav"
WIN_SOUND = 'win.wav'
GAME_OVER_SOUND = 'gameover.wav'

BACKGROUND_IMG = 'background.png'
ICON_IMG = 'agonias.png'
HERO_IMG = 'hero.png'
#F3 lista con diferentes png de enemigos que seran calleados depues con random choice
ENEMY_IMG = ["enemy.png", "enemy1.png", "enemy2.png", "enemy3.png"]
BULLET_IMG = 'bullet.png'

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

backgroud = pygame.image.load(BACKGROUND_IMG)
backgroud = pygame.transform.scale(backgroud, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.init()

mixer.music.load(BACKGROUND_SOUND)
mixer.music.play(-1)

pygame.display.set_caption(TITLE)
icon = pygame.image.load(ICON_IMG)
pygame.display.set_icon(icon)

player_img = pygame.image.load(HERO_IMG)
player_x = (SCREEN_WIDTH / 2) - (64 / 2)
player_y = SCREEN_HEIGHT - 120
player_y_velocity = 0
player_x_velocity = 0

number_of_enemies = 8
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_velocity = []
enemy_y_velocity = []

bullet_img = pygame.image.load(BULLET_IMG)
bullet_x = 0
bullet_y = SCREEN_HEIGHT - 120
bullet_y_velocity = 10
bullet_x_velocity = 0
bullet_state = BULLET_READY_STATUS

score_value = 0
score_font = pygame.font.Font('freesansbold.ttf', 30)
score_x = 10
score_y = 10


lvl_font = pygame.font.Font('freesansbold.ttf', 30)
lvl_x = 200
lvl_y = 10

message_font = pygame.font.Font('freesansbold.ttf', 40)
message_x = SCREEN_WIDTH // 2
message_y = SCREEN_HEIGHT // 2


# lista de imagenes  ENEMY_IMG


def create_enemies():
    global lvl
    global score_value, PLAYER_VELOCITY

    #F4 nuevos niveles con dificultad aumentada

    for i in range(number_of_enemies):
        if score_value == 0:
            enemy_img.append(pygame.image.load(random.choice(ENEMY_IMG)))
            enemy_x.append(random.randint(0, SCREEN_WIDTH - Tamaño_del_enemigo_x))
            enemy_y.append(random.randint(0, SCREEN_HEIGHT // 2))
 # F1 y F2 cambio aleatorio de velocidades en x y y
            enemy_x_velocity.append(random.randint(2, 5))
            enemy_y_velocity.append(random.randint(20, 40))
            lvl = 1
        elif score_value == 8:
            enemy_img.append(pygame.image.load(random.choice(ENEMY_IMG)))
            enemy_x.append(random.randint(0, SCREEN_WIDTH - Tamaño_del_enemigo_x))
            enemy_y.append(random.randint(0, SCREEN_HEIGHT // 2))
            enemy_x_velocity.append(random.randint(3, 6))
            enemy_y_velocity.append(random.randint(10, 20))
            lvl = 2
        elif score_value == 17:
            enemy_img.append(pygame.image.load(random.choice(ENEMY_IMG)))
            enemy_x.append(random.randint(0, SCREEN_WIDTH - Tamaño_del_enemigo_x))
            enemy_y.append(random.randint(0, SCREEN_HEIGHT // 2))
            enemy_x_velocity.append(random.randint(4, 7))
            enemy_y_velocity.append(random.randint(10, 20))
            lvl = 3
        elif score_value == 27:
# F6 los enemigos reducen si tamaño en aproximadamente 10% cada vez que cambia el nivel despues del nivel 3
            n = random.choice(ENEMY_IMG)
            m = pygame.transform.scale(pygame.image.load(n), (Tamaño_del_enemigo_x - 6, Tamaño_del_enemigo_y - 6))
            enemy_img.append(m)

            enemy_x.append(random.randint(0, SCREEN_WIDTH - (Tamaño_del_enemigo_x - 6)))
            enemy_y.append(random.randint(0, SCREEN_HEIGHT // 2))
            enemy_x_velocity.append(random.randint(5, 8))
            enemy_y_velocity.append(random.randint(10, 20))
            lvl = 4

        elif score_value == 38:

            n = random.choice(ENEMY_IMG)
            m = pygame.transform.scale(pygame.image.load(n), (Tamaño_del_enemigo_x - 12, Tamaño_del_enemigo_y - 12))
            enemy_img.append(m)

            enemy_x.append(random.randint(0, SCREEN_WIDTH - (Tamaño_del_enemigo_x - 12)))
            enemy_y.append(random.randint(0, SCREEN_HEIGHT // 2))
            enemy_x_velocity.append(random.randint(6, 9))
            enemy_y_velocity.append(random.randint(10, 20))
            lvl = 5
        elif score_value == 50:

            n = random.choice(ENEMY_IMG)
            m = pygame.transform.scale(pygame.image.load(n), (Tamaño_del_enemigo_x - 18, Tamaño_del_enemigo_y - 18))
            enemy_img.append(m)

            enemy_x.append(random.randint(0, SCREEN_WIDTH - (Tamaño_del_enemigo_x - 18)))
            enemy_y.append(random.randint(0, SCREEN_HEIGHT // 2))
            enemy_x_velocity.append(random.randint(7, 10))
            enemy_y_velocity.append(random.randint(10, 20))
            #F7 velocidad menor para el jugador
            PLAYER_VELOCITY = 4
            lvl =6
        elif score_value == 63:

            n = random.choice(ENEMY_IMG)
            m = pygame.transform.scale(pygame.image.load(n), (Tamaño_del_enemigo_x - 24, Tamaño_del_enemigo_y - 24))
            enemy_img.append(m)

            enemy_x.append(random.randint(0, SCREEN_WIDTH - (Tamaño_del_enemigo_x - 24)))
            enemy_y.append(random.randint(0, SCREEN_HEIGHT // 2))
            enemy_x_velocity.append(random.randint(7, 10))
            enemy_y_velocity.append(random.randint(10, 20))
            PLAYER_VELOCITY = 3
            lvl = 7

def change_level():
    global number_of_enemies,enemy_img,enemy_x,enemy_y,enemy_x_velocity,enemy_y_velocity

    enemy_img = []
    enemy_x = []
    enemy_y = []
    enemy_x_velocity = []
    enemy_y_velocity = []

    enemys = [0,9,10,11,12,13,14,15]

    number_of_enemies = enemys[count]
    create_enemies()
    spawn_enemy()



def spawn_enemy():
    gameOver = False
    global player_x_velocity, score_value, number_of_enemies
    global player_x, bullet_x, bullet_y, bullet_state
    for i in range(number_of_enemies):
        enemy_x[i] += enemy_x_velocity[i]

        # VERIFY GAME OVER
        if enemy_y[i] >= SCREEN_HEIGHT - 170:
            for j in range(number_of_enemies):
                enemy_y[j] = SCREEN_HEIGHT * 2

            if not gameOver:
                mixer.music.stop()
                mixer.Sound(GAME_OVER_SOUND).play()
            show_message(GAME_OVER)
            gameOver = True
            break

        if (enemy_x[i] >= SCREEN_WIDTH - 64):
            enemy_x_velocity[i] = enemy_x_velocity[i] * -1
            enemy_y[i] += enemy_y_velocity[i]
        if (enemy_x[i] <= 0):
            enemy_x_velocity[i] = enemy_x_velocity[i] * -1
            enemy_y[i] += enemy_y_velocity[i]

        collision = isCollision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            mixer.Sound(EXPLOSION_SOUND).play()
            bullet_y = SCREEN_HEIGHT - 120
            bullet_state = BULLET_READY_STATUS
            score_value += 1
            enemy_img.pop(i)
            enemy_x.pop(i)
            enemy_y.pop(i)
            number_of_enemies -= 1
            break

        show_enemy(enemy_img[i], enemy_x[i], enemy_y[i])


def show_player(player_img, player_x, player_y):
    screen.blit(player_img, (player_x, player_y))


def show_enemy(enemy_img, enemy_x, enemy_y):
    screen.blit(enemy_img, (enemy_x, enemy_y))


def show_bullet(bullet_img, bullet_x, bullet_y):
    global bullet_state
    bullet_state = BULLET_FIRE_STATUS
    screen.blit(bullet_img, (bullet_x - 16, bullet_y - 10))


def show_score(score_value, score_x, score_y):
    score_text = score_font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score_text, (score_x, score_y))

#F5 mostrar el nivel
def show_lvl(lvl, lvl_x, lvl_y):

    lvl_text = lvl_font.render("level : " + str(lvl), True, (255, 255, 255))
    screen.blit(lvl_text, (lvl_x, lvl_y))

def show_message(text):
    message_text = score_font.render(text, True, (255, 255, 255))
    text_rect = message_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    screen.blit(message_text, text_rect)


def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow((enemy_x + 64 / 2) - bullet_x, 2) + math.pow((enemy_y + 64 / 2) - bullet_y, 2))
    if distance < 30:
        return True
    else:
        return False


def main():
    running = True
    gameOver = False

    create_enemies()

    global player_x_velocity, score_value, number_of_enemies
    global player_x, bullet_x, bullet_y, bullet_state,count
    while running:
        screen.fill((0, 0, 0))
        screen.blit(backgroud, (0, 0))

        # detect events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("evento QUIT")
                pygame.quit()  # termina juego de pygame
                sys.exit(0)  # termina el programa

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_velocity = -PLAYER_VELOCITY
                if event.key == pygame.K_RIGHT:
                    player_x_velocity = PLAYER_VELOCITY
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    player_x_velocity = 0
                if event.key == pygame.K_SPACE:
                    if bullet_state is BULLET_READY_STATUS:
                        mixer.Sound(LASER_SOUND).play()
                        bullet_x = player_x + 64 / 2
                        show_bullet(bullet_img, bullet_x, bullet_y)

        # buller movement
        if bullet_state is BULLET_FIRE_STATUS:
            show_bullet(bullet_img, bullet_x, bullet_y)
            bullet_y -= bullet_y_velocity

        if bullet_y <= 0:
            bullet_y = SCREEN_HEIGHT - 120
            bullet_state = BULLET_READY_STATUS

        if number_of_enemies <= 0:
            count += 1
            if lvl == 7:
                show_message(YOU_WIN)
                if not gameOver:
                    mixer.music.stop()
                    mixer.Sound(WIN_SOUND).play()
                    gameOver = True
            else: change_level()



        # show enemies
        spawn_enemy()

        player_x += player_x_velocity

        if (player_x <= 0):
            player_x = 0
        if (player_x >= SCREEN_WIDTH - 64):
            player_x = SCREEN_WIDTH - 64

        show_player(player_img, player_x, player_y)
        show_score(score_value, score_x, score_y)
        show_lvl(lvl, lvl_x, lvl_y)

        # show_bullet(bullet_img, 200, 200)
        # show_enemy(enemy_img[0], enemy_x[0], enemy_y[0])

        # show_message(GAME_OVER, message_x, message_y)
        pygame.display.update()


main()
