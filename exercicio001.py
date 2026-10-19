import computador
print("INICIANDO\n")
marca = input("Marca do computador: ")
memoria = input("Marca de memoria: ")
preco = input("Valor do produto: R$")
pc = computador.Computador(marca, memoria, float(preco))
pc.biblioteca_componentes()
pc.salva_persistente()
pc.exibir_conteudo()