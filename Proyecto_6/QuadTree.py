class QuadTree:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.divided = False
        self.nodos = []
        self.mass = 0
        self.center = [0, 0]
        self.NW = self.NE = self.SW = self.SE = None

    def insert(self, nodo):
        x, y = nodo.attrs['coords']
        if not (self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height):
            return False

        self.nodos.append(nodo)
        self.mass += 1
        self._update_center()

        if self.mass > 1 and not self.divided:
            self._subdivide()
            for n in self.nodos:
                self._insert_children(n)
            self.nodos = []
        return True

    def _update_center(self):
        if self.mass == 0:
            self.center = [0, 0]
        else:
            x_sum = sum(n.attrs['coords'][0] for n in self.nodos)
            y_sum = sum(n.attrs['coords'][1] for n in self.nodos)
            self.center = [x_sum / self.mass, y_sum / self.mass]

    def _subdivide(self):
        w, h = self.width / 2, self.height / 2
        self.NW = QuadTree(self.x, self.y, w, h)
        self.NE = QuadTree(self.x + w, self.y, w, h)
        self.SW = QuadTree(self.x, self.y + h, w, h)
        self.SE = QuadTree(self.x + w, self.y + h, w, h)
        self.divided = True

    def _insert_children(self, nodo):
        for child in [self.NW, self.NE, self.SW, self.SE]:
            if child.insert(nodo):
                break