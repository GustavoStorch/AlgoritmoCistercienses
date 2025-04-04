import cv2
import numpy as np
import os

# Definição do diretório de símbolos
DIRETORIO_SIMBOLOS = r'C:\Estudos\Algoritmos Avançados - Martim\AlgoritmoCistercienses\API\static\symbols\output'

def carregar_imagem(numero):
    """Carrega a imagem correspondente ao número informado."""
    caminho = os.path.join(DIRETORIO_SIMBOLOS, f'{numero}.png')
    if os.path.exists(caminho):
        return cv2.imread(caminho, cv2.IMREAD_UNCHANGED)  # Mantém transparência
    else:
        print(f'Imagem {numero}.png não encontrada!')
        return None

def criar_canvas():
    """Cria um canvas quadrado para a montagem do número cisterciense."""
    tamanho = 200  # Ajuste conforme necessário
    return np.zeros((tamanho, tamanho, 4), dtype=np.uint8)  # Fundo transparente

def sobrepor_imagem(base, img):
    """Sobrepõe a imagem no centro do canvas mantendo a transparência."""
    h, w = img.shape[:2]
    H, W = base.shape[:2]
    
    # Calcular posição central
    y_offset = (H - h) // 2
    x_offset = (W - w) // 2

    for y in range(h):
        for x in range(w):
            if y + y_offset < base.shape[0] and x + x_offset < base.shape[1]:
                alpha = img[y, x, 3] / 255.0  # Normaliza o canal alfa
                if alpha > 0:  # Apenas pixels visíveis são aplicados
                    for c in range(3):  # Canal R, G, B
                        base[y + y_offset, x + x_offset, c] = (
                            alpha * img[y, x, c] + (1 - alpha) * base[y + y_offset, x + x_offset, c]
                        )
                    base[y + y_offset, x + x_offset, 3] = max(base[y + y_offset, x + x_offset, 3], img[y, x, 3])

def gerar_numero_cisterciense(numero):
    """Quebra o número em partes e combina as imagens corretamente sobrepostas."""
    partes = {
        "unidades": (numero % 10),
        "dezenas": (numero // 10 % 10) * 10,
        "centenas": (numero // 100 % 10) * 100,
        "milhares": (numero // 1000 % 10) * 1000
    }

    canvas = criar_canvas()

    for valor in partes.values():
        if valor > 0:
            img = carregar_imagem(valor)
            if img is not None:
                sobrepor_imagem(canvas, img)

    cv2.imwrite('numero_gerado.png', canvas)
    print("Número gerado com sucesso! Salvo como numero_gerado.png")

# Entrada do usuário
numero = int(input("Digite um número entre 1 e 9999: "))
gerar_numero_cisterciense(numero)
