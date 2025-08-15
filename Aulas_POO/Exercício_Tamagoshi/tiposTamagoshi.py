# tipos.py
from base import Tamagoshi

class TamagoshiFeliz(Tamagoshi):
    def falar(self):
        print(f"{self.nome} diz: Yay! Eu adoro brincar com você! 🌈✨")


class TamagoshiFominha(Tamagoshi):
    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 10

    def falar(self):
        print(f"{self.nome} diz: Tô com fome de novo... me dá comida!! 🍔🥺")


class TamagoshiZangado(Tamagoshi):
    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 5
        self.fome += 5

    def vida(self):
        super().vida()
        if self.fome > 70 or self.tedio > 70:
            self.saude -= 10

    def falar(self):
        print(f"{self.nome} diz: Grrr... você me irritou de novo! 😤")
