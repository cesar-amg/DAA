from math import log, atan2, cos, sin
import pygame
import imageio
import random


WIDTH, HEIGHT   = 800, 608
BORDER          = 10
WIN             = pygame.display.set_mode((WIDTH, HEIGHT))

# Colores
BG              = (0, 0, 0)
BLUE            = (69, 133, 136)
BLACK           = (40, 40, 40)
RED             = (157, 0, 6)

# Configuración
ITERS           = 500
FPS             = 20
NODE_RADIUS     = 5
DIST_MIN        = (min(WIDTH, HEIGHT)) // 35
NODE_MIN_WIDTH  = 10
NODE_MIN_HEIGHT = 10
NODE_MAX_WIDTH  = WIDTH - 10
NODE_MAX_HEIGHT = HEIGHT - 10

# spring para 100
"""c1 = 1.65
c2 = 0.9
c3 = 0.4
c4 = 0.6"""

# spring para 500
c1 = 2
c2 = 0.5
c3 = 0.1
c4 = 0.4


def spring(g):
    """
    Muestra una animación del metodo de visualizacion spring de Eades.

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """

    run = True
    clock = pygame.time.Clock()
    frames = []

    init_nodes(g)
    draw_edges(g)
    draw_nodes(g)


    i = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if i > ITERS:
            continue

        WIN.fill(BG)
        update_nodes(g)
        draw_edges(g)
        draw_nodes(g)
        pygame.display.update()
        image_data = pygame.surfarray.array3d(WIN)
        image_data = image_data.transpose([1, 0, 2])
        frames.append(image_data)
        i += 1

        imageio.mimsave("grafo_animado.mp4", frames, fps=FPS)
    pygame.quit()
    return


def init_nodes(g):
    """
    Inicializa los nodos del grafo g en posiciones random

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """

    for node in g.obtener_nodos():
        x = random.randrange(NODE_MIN_WIDTH, NODE_MAX_WIDTH)
        y = random.randrange(NODE_MIN_HEIGHT, NODE_MAX_HEIGHT)
        node.attrs['coords'] = [x, y]
        node.attrs['color_fill'] = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        node.attrs['color_border'] = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    return

def update_nodes(g):
    """
    Aplica la fuerza a los nodos del grafo G para actualizar su poisicion

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """
    ################
    for node in g.obtener_nodos():
        x_attraction = 0
        y_attraction = 0
        x_node, y_node = node.attrs['coords']

        for other in node.vecinos:
            x_other, y_other = other.attrs['coords']
            d = ((x_node - x_other) ** 2 + (y_node - y_other)**2) ** 0.5

            # defining minimum distance
            if d < DIST_MIN:
                continue
            attraction = c1 * log(d / c2)
            angle = atan2(y_other - y_node, x_other - x_node)
            x_attraction += attraction * cos(angle)
            y_attraction += attraction * sin(angle)

        not_connected = (other for other in g.obtener_nodos()
                        if (other.valor not in node.vecinos and other != node))
        x_repulsion = 0
        y_repulsion = 0
        for other in not_connected:
            x_other, y_other = other.attrs['coords']
            d = ((x_node - x_other) ** 2 + (y_node - y_other)**2) ** 0.5
            if d == 0:
                continue
            repulsion = c3 / d ** 0.5
            angle = atan2(y_other - y_node, x_other - x_node)
            x_repulsion -= repulsion * cos(angle)
            y_repulsion -= repulsion * sin(angle)

        fx = x_attraction + x_repulsion
        fy = y_attraction + y_repulsion
        node.attrs['coords'][0] += c4 * fx
        node.attrs['coords'][1] += c4 * fy

        # Restrict for limits of window
        node.attrs['coords'][0] = max(node.attrs['coords'][0], NODE_MIN_WIDTH)
        node.attrs['coords'][1] = max(node.attrs['coords'][1], NODE_MIN_HEIGHT)
        node.attrs['coords'][0] = min(node.attrs['coords'][0], NODE_MAX_WIDTH)
        node.attrs['coords'][1] = min(node.attrs['coords'][1], NODE_MAX_HEIGHT)

    return


def draw_nodes(g):
    """
    Dibuja los nodos del grafo g

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """

    for node in g.obtener_nodos():
        color_fill = node.attrs.get('color_fill', BLUE)
        color_border = node.attrs.get('color_border', RED)
        pygame.draw.circle(WIN, color_fill, node.attrs['coords'], NODE_RADIUS - 3, 0)
        pygame.draw.circle(WIN, color_border, node.attrs['coords'], NODE_RADIUS, 3)

    return


def draw_edges(g):
    """
    Dibuja las aristas del grafo g

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """

    for edge in g.obtener_aristas():
        u, v = edge.obtener_nodos()
        u_pos = u.attrs['coords']
        v_pos = v.attrs['coords']

        pygame.draw.line(WIN, (255, 255, 255), u_pos, v_pos, 1)

    return
