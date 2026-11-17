import random
from karakter import Karakter

class Hero(Karakter):
    def __init__(self, nama, hp, attack_power, class_hero):
        super().__init__(nama, hp, attack_power)
        self.class_hero = class_hero

    # Override method serang (Polymorphism)
    def serang(self, target):
        damage = self._attack_power + random.randint(2, 8)
        print(f"🗡️ {self._nama} ({self.class_hero}) menebas {target.nama} sebesar {damage} damage!")
        target.hp -= damage

    def skill_khusus(self, target):
        damage = self._attack_power * 2
        print(f"🔥 {self._nama} mengeluarkan SKILL ULTIMATE ke {target.nama} sebesar {damage} damage!")
        target.hp -= damage