from pathlib import Path
import os
import json
class Computador:
    def __init__(self, marca, memoria, valor):
        self.marca = marca
        self.memoria = memoria
        self.valor = valor
    def salva_persistente(self):
        with open("Dados_computador.json", "w", encoding="utf-8") as arquivo:
            json.dump(self.dados_comp,arquivo, indent=4, ensure_ascii=False)
    def biblioteca_componentes(self):
        leitura = []
        if os.path.exists("Dados_computador.json"):
            with open("Dados_computador.json", "r", encoding="utf-8") as arquivo:
                leitura = json.load(arquivo)
        self.dados_comp = {"marca": self.marca, "memoria": self.memoria, "preco": self.valor}
        leitura.append(self.dados_comp)
        self.dados_comp = leitura
    def exibir_conteudo(self):
        with open("Dados_computador.json", "r", encoding="utf-8") as arquivo:
            leitura = json.load(arquivo)
            for dados in leitura:
                print(f"Marca: {dados["marca"]}\nTipo: {dados["memoria"]}\npreco: R${dados["preco"]:.2f}\n\n")