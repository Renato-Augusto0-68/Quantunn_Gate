
class Personagem:
    def __init__(self):
        self.vida = 100
        self.item = []

    def dano(self, i=1):
        self.vida -= 20 * i
        if self.vida < 0:
            self.vida = 0

    def recuperar(self, i=1):
        self.vida += 20 * i
        if self.vida > 100:
            self.vida = 100

    def guardar_items(self, item):
        self.item.append(item)

    def mostrar_items(self, item=None):
        if item:
            return item if item in self.item else "Nada"
        return ", ".join(self.item) if self.item else "Nada"
