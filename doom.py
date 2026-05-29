import pygame
import math

# Inicializar pygame
pygame.init()

# Pantalla
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Doom")

clock = pygame.time.Clock()

# Jugador
player_x = 400
player_y = 300
player_angle = 0
player_speed = 3

# Colores
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)

# Mapa
MAP = [
    "########",
    "#......#",
    "#......#",
    "#..#...#",
    "#......#",
    "#......#",
    "########"
]

TILE = 64

# Convertir paredes
walls = []

for y, row in enumerate(MAP):
    for x, char in enumerate(row):
        if char == "#":
            walls.append(pygame.Rect(x * TILE, y * TILE, TILE, TILE))

# Función para raycasting
def draw_3d():
    rays = 120
    fov = math.pi / 3

    for ray in range(rays):

        angle = player_angle - fov / 2 + fov * ray / rays

        for depth in range(1, 800):

            target_x = player_x + math.cos(angle) * depth
            target_y = player_y + math.sin(angle) * depth

            rect = pygame.Rect(target_x, target_y, 2, 2)

            hit = False

            for wall in walls:
                if wall.colliderect(rect):

                    corrected_depth = depth * math.cos(player_angle - angle)

                    if corrected_depth < 1:
                        corrected_depth = 1

                    wall_height = 30000 / corrected_depth

                    color = 255 / (1 + corrected_depth * corrected_depth * 0.0001)

                    pygame.draw.rect(
                        screen,
                        (color, color, color),
                        (
                            ray * (WIDTH / rays),
                            HEIGHT / 2 - wall_height / 2,
                            (WIDTH / rays) + 1,
                            wall_height
                        )
                    )

                    hit = True
                    break

            if hit:
                break

# Loop principal
running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Movimiento
    if keys[pygame.K_w]:
        player_x += math.cos(player_angle) * player_speed
        player_y += math.sin(player_angle) * player_speed

    if keys[pygame.K_s]:
        player_x -= math.cos(player_angle) * player_speed
        player_y -= math.sin(player_angle) * player_speed

    # Rotación
    if keys[pygame.K_LEFT]:
        player_angle -= 0.05

    if keys[pygame.K_RIGHT]:
        player_angle += 0.05

    # Fondo
    screen.fill(BLACK)

    pygame.draw.rect(screen, (30, 30, 30), (0, 0, WIDTH, HEIGHT // 2))
    pygame.draw.rect(screen, (70, 70, 70), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    # Dibujar mundo
    draw_3d()

    pygame.display.flip()

pygame.quit()