def aumentar(preco = 0, taxa = 0, formato = False):
    novo_preco = preco + (preco * taxa / 100)
    return novo_preco if formato is False else moeda(novo_preco)

def diminuir(preco = 0, taxa = 0, formato = False):
    novo_preco = preco - (preco * taxa / 100)
    return novo_preco if formato is False else moeda(novo_preco)

def dobro(preco = 0, formato = False):
    novo_preco = preco * 2
    return novo_preco if formato is False else moeda(novo_preco)

def metade(preco = 0, formato = False):
    novo_preco = preco / 2
    return novo_preco if formato is False else moeda(novo_preco)

def moeda(preco = 0, moeda='R$'):
    return f"{moeda}{preco:.2f}".replace('.', ',')