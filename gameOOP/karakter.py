from abc import ABC, abstractmethod  # <-- Tambahkan baris ini di paling atas

class Karakter(ABC):
    def __init__(self, nama, hp, attack_power):
        self._nama = nama            
        self._hp = hp                
        self._attack_power = attack_power

    @property
    def nama(self):
        return self._nama

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, nilai):
        self._hp = max(0, nilai)     

    def status(self):
        return f"{self._nama} [HP: {self._hp}]"

    # Abstract Method (Wajib di-override oleh class turunan)
    @abstractmethod
    def serang(self, target):
        pass