from math import sqrt
import pygame
import imageio
import random

# create the main surface (or window)
WIDTH, HEIGHT = 1008, 608
BORDER = 10
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# colors
BG = (0, 0, 0)
BLUE = (69, 133, 136)
BLACK = (40, 40, 40)
RED = (157, 0, 6)

# configuration
ITERS = 1000
FPS = 10
NODE_RADIUS = 8
NODE_MIN_WIDTH = 10
NODE_MIN_HEIGHT = 10
NODE_MAX_WIDTH = WIDTH - 10
NODE_MAX_HEIGHT = HEIGHT - 10


def Fruch_Reig(g, fuerza=0.3,ITERS=ITERS):
    """
    Visualización basada en el algoritmo de Fruchterman-Reingold.
    """
    run = True
    clock = pygame.time.Clock()
    frames=[]

    init_nodes(g)

    area = (NODE_MAX_WIDTH - NODE_MIN_WIDTH) * (NODE_MAX_HEIGHT - NODE_MIN_HEIGHT)
    k = sqrt(area / len(g.obtener_nodos())) * fuerza
    t = min(WIDTH, HEIGHT) / 4  # temperatura inicial

    i = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if i > ITERS:
            continue


        WIN.fill(BG)
        update_nodes(g, t, k)
        draw_edges(g)
        draw_nodes(g)
        pygame.display.update()
        image_data = pygame.surfarray.array3d(WIN)
        image_data = image_data.transpose([1, 0, 2])
        frames.append(image_data)

        t *= 0.95  # enfriar temperatura
        i += 1
        imageio.mimsave("grafo_animado.mp4", frames, fps=FPS)
    pygame.quit()
    return


def init_nodes(g):
    """
    Inicializa los nodos del grafo g en posiciones aleatorias.
    """
    for node in g.obtener_nodos():
        x = random.randrange(NODE_MIN_WIDTH, NODE_MAX_WIDTH)
        y = random.randrange(NODE_MIN_HEIGHT, NODE_MAX_HEIGHT)
        node.attrs['coords'] = [x, y]
        node.attrs['color_fill'] = (
            random.randint(150, 255),
            random.randint(150, 255),
            random.randint(150, 255)
        )
        node.attrs['color_border'] = (
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1)
        )
    return


def update_nodes(g, t, k):
    """
    Aplica el algoritmo de Fruchterman-Reingold para actualizar las posiciones.
    """
    # Inicializar desplazamiento
    for v in g.obtener_nodos():
        v.attrs['disp'] = [0.0, 0.0]

    # Fuerzas de repulsión
    for v in g.obtener_nodos():
        for u in g.obtener_nodos():
            if v == u:
                continue
            dx = v.attrs['coords'][0] - u.attrs['coords'][0]
            dy = v.attrs['coords'][1] - u.attrs['coords'][1]
            dist = sqrt(dx**2 + dy**2) or 0.01
            fr = (k * k) / dist
            v.attrs['disp'][0] += (dx / dist) * fr
            v.attrs['disp'][1] += (dy / dist) * fr

    # Fuerzas de atracción
    for e in g.obtener_aristas():
        u, v = e.obtener_nodos()
        dx = v.attrs['coords'][0] - u.attrs['coords'][0]
        dy = v.attrs['coords'][1] - u.attrs['coords'][1]
        dist = sqrt(dx**2 + dy**2) or 0.01
        fa = (dist**2) / k
        disp_x = (dx / dist) * fa
        disp_y = (dy / dist) * fa
        v.attrs['disp'][0] -= disp_x
        v.attrs['disp'][1] -= disp_y
        u.attrs['disp'][0] += disp_x
        u.attrs['disp'][1] += disp_y

    # Actualizar posiciones con desplazamiento limitado
    for v in g.obtener_nodos():
        dx, dy = v.attrs['disp']
        disp_len = sqrt(dx**2 + dy**2) or 0.01
        limited_dx = (dx / disp_len) * min(disp_len, t)
        limited_dy = (dy / disp_len) * min(disp_len, t)
        v.attrs['coords'][0] += limited_dx
        v.attrs['coords'][1] += limited_dy

        # Limitar dentro del marco
        v.attrs['coords'][0] = min(NODE_MAX_WIDTH, max(NODE_MIN_WIDTH, v.attrs['coords'][0]))
        v.attrs['coords'][1] = min(NODE_MAX_HEIGHT, max(NODE_MIN_HEIGHT, v.attrs['coords'][1]))
    return


def draw_nodes(g):
    """
    Dibuja los nodos del grafo g.
    """
    for node in g.obtener_nodos():
        color_fill = node.attrs.get('color_fill', BLUE)
        color_border = node.attrs.get('color_border', RED)
        pygame.draw.circle(WIN, color_fill, node.attrs['coords'], NODE_RADIUS - 2, 0)
        pygame.draw.circle(WIN, color_border, node.attrs['coords'], NODE_RADIUS, 2)
    return


def draw_edges(g):
    """
    Dibuja las aristas del grafo g.
    """
    for edge in g.obtener_aristas():
        u, v = edge.obtener_nodos()
        u_pos = u.attrs['coords']
        v_pos = v.attrs['coords']
        pygame.draw.line(WIN, (255, 255, 255), u_pos, v_pos, 1)
    return