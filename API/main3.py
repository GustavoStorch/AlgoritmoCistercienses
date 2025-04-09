import cv2
import numpy as np
import os
import argparse

# Caminho da pasta com os símbolos
DIRETORIO_SIMBOLOS = r'C:\Estudos\Algoritmos Avançados - Martim\AlgoritmoCistercienses\API\static\symbols\output'

def carregar_simbolos(tamanho=(128, 128)):
    simbolos = {}
    for valor in [1,2,3,4,5,6,7,8,9,
                  10,20,30,40,50,60,70,80,90,
                  100,200,300,400,500,600,700,800,900,
                  1000,2000,3000,4000,5000,6000,7000,8000,9000]:
        caminho = os.path.join(DIRETORIO_SIMBOLOS, f"{valor}.png")
        if os.path.exists(caminho):
            img = carregar_e_processar_imagem(caminho, tamanho)
            simbolos[valor] = img
    return simbolos

def carregar_e_processar_imagem(caminho_imagem, tamanho=(128, 128)):
    img = cv2.imread(caminho_imagem, cv2.IMREAD_UNCHANGED)

    if img is None:
        raise FileNotFoundError(f"Imagem não encontrada: {caminho_imagem}")

    # Se tiver canal alpha, substitui fundo transparente por branco
    if img.shape[-1] == 4:
        alpha_channel = img[:, :, 3]
        rgb_channels = img[:, :, :3]
        white_background = np.ones_like(rgb_channels, dtype=np.uint8) * 255
        alpha_factor = alpha_channel[:, :, np.newaxis] / 255.0
        img_rgb = rgb_channels * alpha_factor + white_background * (1 - alpha_factor)
        img = img_rgb.astype(np.uint8)

    # Converte para cinza
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Binariza (preto e branco)
    _, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Redimensiona
    img_resized = cv2.resize(img_bin, tamanho, interpolation=cv2.INTER_NEAREST)
    
    return img_resized

def combinar_simbolos(simbolos, tamanho=(128, 128)):
    composicoes = {}
    valores = list(simbolos.keys())

    for i in range(len(valores)):
        for j in range(i + 1, len(valores)):
            val1, val2 = valores[i], valores[j]
            soma_valor = val1 + val2

            if soma_valor in simbolos:
                continue  # já temos imagem pronta

            img1 = simbolos[val1]
            img2 = simbolos[val2]

            # Combinação visual com OR bit a bit (funde os traços)
            combinada = cv2.bitwise_or(img1, img2)

            composicoes[soma_valor] = combinada

    return composicoes

def reconhecer_numero(caminho_imagem, tamanho=(128, 128)):
    imagem_input = carregar_e_processar_imagem(caminho_imagem, tamanho)
    simbolos = carregar_simbolos(tamanho)

    # Verificação exata
    for valor, simbolo_img in simbolos.items():
        if np.array_equal(imagem_input, simbolo_img):
            print(f"Imagem corresponde exatamente ao número: {valor}")
            return valor

    # Verificação por composição (duas imagens)
    composicoes = combinar_simbolos(simbolos, tamanho)

    for valor_combinado, img_combinada in composicoes.items():
        if np.array_equal(imagem_input, img_combinada):
            print(f"Imagem corresponde à combinação de símbolos que formam o número: {valor_combinado}")
            return valor_combinado

    print("Nenhum símbolo ou combinação corresponde exatamente.")
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reconhece número cisterciense de uma imagem.")
    parser.add_argument("imagem", help="Caminho da imagem a ser analisada")

    args = parser.parse_args()
    reconhecer_numero(args.imagem)
