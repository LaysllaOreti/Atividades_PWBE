# persistencia.py
import json

def salvar_bichinho(tamagoshi, caminho):
    dados = {
        'nome': tamagoshi.nome,
        'fome': tamagoshi.fome,
        'saude': tamagoshi.saude,
        'idade': tamagoshi.idade,
        'tedio': tamagoshi.tedio,
        'xp': tamagoshi.xp,
        'nivel': tamagoshi.nivel
    }
    with open(caminho, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def carregar_bichinho(cls, caminho):
    with open(caminho, 'r') as arquivo:
        dados = json.load(arquivo)
        return cls(
            nome=dados['nome'],
            fome=dados['fome'],
            saude=dados['saude'],
            idade=dados['idade'],
            tedio=dados['tedio'],
            xp=dados['xp'],
            nivel=dados['nivel']
        )
