import os
class Node:
    def __init__(self, value, isFim=False):
        self.value = value
        self.children = []
        self.isFim = isFim

def print_tree(node, level=0):
    print(' ' * 4 * level + '->', node.value)
    for child in node.children:
        print_tree(child, level + 1)

def create_tree():
    # node inicial
    root = Node("Na cela")

    # Primeiro nivel
    pedir_lanche = Node("Pedir um lanche")
    chamar_guarda = Node("Chamar o guarda")
    root.children.extend([pedir_lanche, chamar_guarda])

    # Segundo nivel
    usar_cerrote = Node("Você encontrou um cerrote no seu lanche!")
    usar_bomba = Node("Você encontrou uma bomba no seu lanche!")
    usar_furadeira = Node("Você encontrou uma furadeira no seu lanche!")
    pedir_banheiro = Node("Pedir para ir no banheiro")
    tentar_nocautear = Node("Tentar nocautear o guarda")
    pedir_lanche.children.extend([usar_cerrote, usar_bomba, usar_furadeira])
    chamar_guarda.children.extend([pedir_banheiro, tentar_nocautear])

    # Terceiro nivel
    corredor_direita = Node("Ir ao corredor da direita!")
    corredor_esquerda = Node("Ir ao corredor da esquerda!")
    correr_corredor = Node("Correr no corredor?")
    ficar_banheiro = Node("Ficar no banheiro?")
    AlertouGuardas = Node("A sua furadeira fez muito barulho e alertou os guardas! Eles tiraram seus lanches.", isFim=True)
    finalBomba = Node("A bomba explodiu na sua cela e você morreu.", isFim=True)
    usar_bomba.children.append(finalBomba)
    usar_furadeira. children.append(AlertouGuardas)
    usar_cerrote.children.extend([corredor_direita, corredor_esquerda])
    pedir_banheiro.children.extend([correr_corredor, ficar_banheiro])

    # Quarto nivel
    escritorio_preso1 = Node("Escritório dos policiais, você é preso.", isFim=True)
    entrar_campo_tiro = Node("Entrar no campo de tiro?")
    entrar_garagem = Node("Entrar na garagem?")
    pular_janela = Node("Pular da janela?")
    esconder_lixeira = Node("Se esconder na lixeira?")
    correr_corredor.children.append(corredor_esquerda)
    corredor_direita.children.append(escritorio_preso1)
    corredor_esquerda.children.extend([entrar_campo_tiro, entrar_garagem])
    ficar_banheiro.children.extend([pular_janela, esconder_lixeira])

    # Quinto nivel
    levar_tiro = Node("Você leva um tiro!", isFim=True)
    roubar_viatura = Node("Roubar uma viatura?")
    roubar_helicoptero = Node("Roubar um helicóptero?")
    cair_predio = Node("Você cai do prédio e morre.", isFim=True)
    LixaoFim = Node("Você é isolado em um lixão no oceano.", isFim=True)
    entrar_campo_tiro.children.append(levar_tiro)
    entrar_garagem.children.extend([roubar_viatura, roubar_helicoptero])
    pular_janela.children.append(cair_predio)
    esconder_lixeira.children.append(LixaoFim)

    # Sexto nivel
    FinalEscapar = Node("Você escapou!!!!", isFim=True)
    FinalSemGasosa = Node("Você está sem gasolina, e não sabe dirigir um helicóptero.", isFim=True)
    roubar_helicoptero.children.append(FinalSemGasosa)
    roubar_viatura.children.append(FinalEscapar)

    # Additional branch for "Tentar nocautear o guarda"
    levar_soco = Node("Você leva um soco.", isFim=True)
    tentar_nocautear.children.append(levar_soco)

    return root

def EscolherCaminho(node, root):
    if node.isFim or not node.children:
        print(f"Você encontrou um final!: {node.value}")
        restart = input("Quer reiniciar? (sim/não): ").strip().lower()
        if restart == 'sim':
            EscolherCaminho(root, root)
        else:
            print("Finalizando...")
        return

    if len(node.children) == 1:
        print(f"Caminho atual: {node.value}")
        EscolherCaminho(node.children[0], root)
        os.system('cls')
    else:
        os.system('cls')
        print(f"Caminho atual: {node.value}")
        for i, child in enumerate(node.children):
            print(f"{i + 1}. {child.value}")

        choice = int(input("Escolha um número: ")) - 1
        if 0 <= choice < len(node.children):
            EscolherCaminho(node.children[choice], root)
        else:
            print("Escolha inválida. Tente novamente.")
            EscolherCaminho(node, root)

if __name__ == "__main__":
    tree = create_tree()
    EscolherCaminho(tree, tree)