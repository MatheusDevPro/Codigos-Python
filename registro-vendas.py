def mostrar_vendas():
    vendas = []
    while True:
        try:
            venda = float(input("Digite o valor da venda (ou -1 para encerrar): "))
            if venda == -1:
                break
            vendas.append(venda)
        except ValueError:
            print("insira um valor válido.")
    return vendas

def calcular_media(vendas):
    if len(vendas) > 0:
        return sum(vendas) / len(vendas)
    return None

def encontrar_maior_venda(vendas):
    if vendas:
        return max(vendas)
    return None

def exibir_resultados(vendas):
    maior_venda = encontrar_maior_venda(vendas)
    media_vendas = calcular_media(vendas)

    if maior_venda is not None:
        print(f"A maior venda é: R${maior_venda:.2f}")
    else:
        print("Nenhuma venda registrada.")

    if media_vendas is not None:
        print(f"A média das vendas é: R${media_vendas:.2f}")
    else:
        print("Nenhuma venda mostrada para calcular a média.")

def main():
    vendas = mostrar_vendas()
    exibir_resultados(vendas)

if __name__ == "__main__":
    main()