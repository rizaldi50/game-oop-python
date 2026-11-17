import random
from karakter import Karakter

class Monster(Karakter):
    def __init__(self, nama, hp, attack_power, jenis):
        super().__init__(nama, hp, attack_power)
        self.jenis = jenis

    # Override method serang (Polymorphism)
    def serang(self, target):
        damage = self._attack_power + random.randint(1, 5)
        print(f"💥 Monster {self._nama} ({self.jenis}) mencakar {target.nama} sebesar {damage} damage!")
        target.hp -= damage