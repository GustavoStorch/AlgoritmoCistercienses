#  Conversor de Algarismos Cistercienses com Visão Computacional

Este projeto tem como objetivo traduzir números entre o sistema **arábico** (0–9999) e o sistema **cisterciense**, um antigo sistema de numeração utilizado por monges entre os séculos XII e XV. Utilizando técnicas de visão computacional (como o OpenCV), o projeto permite:

- Gerar imagens de números em algarismos cistercienses.
- Interpretar imagens de algarismos cistercienses e convertê-los para o formato arábico.
- Exibir, via frontend, as imagens, os números e as localizações dos algarismos reconhecidos.

---

##  Contexto Histórico

No século XII, um grupo de monges em mosteiros europeus desenvolveu um sistema visual de numeração que usava **um único símbolo gráfico** para representar valores de 1 a 9999. Esse sistema, conhecido como **numerais cistercienses**, consistia em uma linha vertical à qual eram anexados traços na parte superior, média e inferior, indicando unidades, dezenas, centenas e milhares.

Apesar de não serem utilizados em cálculos matemáticos, esses numerais foram uma alternativa aos números romanos, e serviram principalmente para fins bibliográficos e marcações de produção até caírem em desuso no século XV.

---

##  Funcionalidades

###  Conversão Bidirecional
- **Arábico ➜ Cisterciense**
  - Entrada: Número arábico (1 a 9999)
  - Saída: Imagem com a representação cisterciense correspondente

- **Cisterciense ➜ Arábico**
  - Entrada: Imagem de numeral cisterciense
  - Saída: Número arábico interpretado

###  Manipulação de Imagens
- Geração precisa de imagens sem distorções
- Leitura de imagens de algarismos cistercienses a partir de uma pasta no disco
- Apresentação visual no frontend com:
  - Imagem original
  - Número arábico correspondente
  - Localização gráfica dos componentes do número

---

##  Tecnologias Utilizadas

- **Python**
- **OpenCV** – Para processamento e geração de imagens
- **Flask** (ou outro framework web) – Para o frontend
- **HTML/CSS** – Para apresentação dos resultados

---

##  Estrutura do Projeto

```plaintext
├── images/                 # Pasta com imagens cistercienses para leitura
├── output/                 # Imagens geradas com algarismos cistercienses
├── static/                 # Arquivos estáticos (CSS, JS)
├── templates/              # Arquivos HTML do frontend
├── cistercian_utils.py     # Algoritmos de geração e interpretação
├── app.py                  # Backend com interface web
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
