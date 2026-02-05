class Pokemon:
    def __init__(self, name, descripcion, movimientos, tipos, stats):
        self.name=name
        self.descripcion=descripcion
        self.movimientos=movimientos
        self.tipos=tipos
        self.stats=stats

    def __str__(self):
        return f"{self.name}. Tipo(s) {self.tipos}."