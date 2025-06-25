from math import sqrt
import pygame
import random
import imageio
import QuadTree as qtr

# Configuración de ventana
WIDTH, HEIGHT = 1024, 720
BORDER = 10
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Colores
BG = (0, 0, 0)
BLUE = (69, 133, 136)
BLACK = (40, 40, 40)
RED = (157, 0, 6)

# Parámetros de simulación
ITERS = 1000
FPS = 10
NODE_RADIUS = 8
NODE_MIN_WIDTH = 10
NODE_MIN_HEIGHT = 10
NODE_MAX_WIDTH = WIDTH - 10
NODE_MAX_HEIGHT = HEIGHT - 10
THETA = 1000  # parámetro de aproximación de Barnes-Hut

def compute_repulsion_force(p, q, k, theta):
    f = [0.0, 0.0]
    v = [p.attrs['coords'][0] - q.center[0], p.attrs['coords'][1] - q.center[1]]
    dist = sqrt(v[0]**2 + v[1]**2) or 0.01
    d = sqrt(q.width * q.height)

    if dist == 0:
        return [0.0, 0.0]

    if (d / dist < theta) or not q.divided:
        fr = (k * k) / dist
        f[0] = (v[0] / dist) * fr * q.mass
        f[1] = (v[1] / dist) * fr * q.mass
        return f
    else:
        for child in [q.NW, q.NE, q.SW, q.SE]:
            child_force = compute_repulsion_force(p, child, k, theta)
            f[0] += child_force[0]
            f[1] += child_force[1]
        return f


def BarnesHut(g, fuerza=.2, ITERS=ITERS):
    run = True
    clock = pygame.time.Clock()
    frames = []

    init_nodes(g)

    area = (NODE_MAX_WIDTH - NODE_MIN_WIDTH) * (NODE_MAX_HEIGHT - NODE_MIN_HEIGHT)
    k = sqrt(area / len(g.obtener_nodos()))*fuerza
    t = min(WIDTH, HEIGHT) / 10

    i = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if i > ITERS:
            run = False
            continue

        WIN.fill(BG)
        update_nodes(g, t, k)
        draw_edges(g)
        draw_nodes(g)
        pygame.display.update()
        image_data = pygame.surfarray.array3d(WIN)
        image_data = image_data.transpose([1, 0, 2])
        frames.append(image_data)

        t *= 0.95
        i += 1

        imageio.mimsave("grafo_animado.mp4", frames, fps=FPS)
    pygame.quit()
    return

def init_nodes(g):
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


def update_nodes(g, t, k):
    # Construir QuadTree
    qt = qtr.QuadTree(0, 0, WIDTH, HEIGHT)
    for n in g.obtener_nodos():
        qt.insert(n)

    # Fuerza de repulsión
    for v in g.obtener_nodos():
        v.attrs['disp'] = compute_repulsion_force(v, qt, k, THETA)

    # Fuerza de atracción
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

    # Actualizar posiciones
    for v in g.obtener_nodos():
        dx, dy = v.attrs['disp']
        disp_len = sqrt(dx**2 + dy**2) or 0.01
        limited_dx = (dx / disp_len) * min(disp_len, t)
        limited_dy = (dy / disp_len) * min(disp_len, t)
        v.attrs['coords'][0] += limited_dx
        v.attrs['coords'][1] += limited_dy

        # Limitar al marco
        v.attrs['coords'][0] = min(NODE_MAX_WIDTH, max(NODE_MIN_WIDTH, v.attrs['coords'][0]))
        v.attrs['coords'][1] = min(NODE_MAX_HEIGHT, max(NODE_MIN_HEIGHT, v.attrs['coords'][1]))


def draw_nodes(g):
    for node in g.obtener_nodos():
        color_fill = node.attrs.get('color_fill', BLUE)
        color_border = node.attrs.get('color_border', RED)
        pygame.draw.circle(WIN, color_fill, node.attrs['coords'], NODE_RADIUS - 2, 0)
        pygame.draw.circle(WIN, color_border, node.attrs['coords'], NODE_RADIUS, 2)


def draw_edges(g):
    for edge in g.obtener_aristas():
        u, v = edge.obtener_nodos()
        u_pos = u.attrs['coords']
        v_pos = v.attrs['coords']
        pygame.draw.line(WIN, (255, 255, 255), u_pos, v_pos, 1)