from tamagoshi import Tamagoshi

class TamagoshiFeliz(Tamagoshi):
    def brincar(self, quantidade):
        super().brincar(quantidade)
        self.saude += 5
        if self.saude > 100:
            self.saude = 100


class TamagoshiFominha(Tamagoshi):
    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 10  


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