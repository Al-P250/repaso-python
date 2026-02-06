from pprint import pprint


class Pokemon:
    def __init__(self, name, descripcion, movimientos, tipos, stats):
        self.name=name
        self.descripcion=descripcion
        self.movimientos=movimientos
        self.tipos=tipos
        self.stats=stats

    @property
    def atacar(self,ataque):
        for i in range(4):
            if self.movimientos[i]["move_name"]==ataque:
                danio=self.movimientos[i]["move_power"]*0.1
        return danio

    def mostrar(self):
        print(self.name)
        pprint(self.movimientos)
        pprint(self.stats)


    @property
    def estaVivo(self):

        return

    def __str__(self):
        return f"{self.name.capitalize()}\n Tipo(s) {self.tipos}."