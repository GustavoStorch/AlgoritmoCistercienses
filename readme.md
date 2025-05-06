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
- **Flask** – Para o frontend
- **REACT** – Para apresentação dos resultados

---

##  Estrutura do Projeto

```plaintext
├── API/                         # Backend em Flask
│   ├── SERVICES/                # Serviços de lógica de negócio
│   │   ├── cisterciense_service.py    # Lógica para geração de algarismos cistercienses
│   │   └── reconhecimento_service.py  # Lógica para reconhecimento de algarismos
│   ├── static/                  # Arquivos estáticos
│   │   ├── output/              # Imagens geradas
│   │   ├── Symbols/             # Símbolos utilizados
│   │   └── temp/                # Arquivos temporários
│   ├── main.py                  # Ponto de entrada da aplicação Flask
│   ├── treinar_modelo.py        # Script para treinamento do modelo de reconhecimento
│   └── requirements.txt         # Dependências do backend
├── FrontEnd/                    # Frontend em React
│   ├── public/                  # Arquivos públicos
│   │   └── index.html           # Página HTML principal
│   ├── src/                     # Código-fonte do React
│   │   ├── assets/              # Recursos estáticos (imagens, fontes, etc.)
│   │   │   └── catolica.png     # Imagem utilizada na aplicação
│   │   ├── components/          # Componentes React reutilizáveis
│   │   │   ├── Chat.js
│   │   │   ├── ImageMessage.js
│   │   │   ├── InputSection.js
│   │   │   ├── LoadingIndicator.js
│   │   │   └── Message.js
│   │   ├── services/            # Serviços para comunicação com o backend
│   │   │   └── api.js
│   │   ├── App.css              # Estilos globais da aplicação
│   │   ├── App.js               # Componente principal do React
│   │   └── index.js             # Ponto de entrada do React
└── README.md                    # Documentação do projeto

```

---

## Como Executar o Projeto

Para executar o projeto, é necessário iniciar tanto o backend (API) quanto o frontend. Utilize dois terminais separados para isso.

### Pré-requisitos

- **Python 3.12**
- **Node.js 18.12.0** e **npm**

---

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

```

---

### Passo 2: Configurar e Iniciar o Backend (API)

Navegue até o diretório da API:

```bash
cd API

```

Crie e ative um ambiente virtual:

```bash
#Linux/Mac
python -m venv venv
source venv/bin/active

#windows
python -m venv venv
venv/Scripts/active

```

Instale as dependências:

```bash
pip install -r requirements.txt

```

Inicie a aplicação Flask:

```bash
python main.py

```

A API estará disponível em: http://localhost:5000

---

### Passo 3: Configurar e Iniciar o FrontEnd

Abra um novo terminal e navegue até o diretório do frontend:

```bash
cd frontend

```

Instale as dependências:

```bash
npm install

```

Inicie a aplicação REACT:

```bash
npm start

```

A aplicação estará disponível em: http://localhost:3000

### Como utilizar o sistema

A utilização do sistema se da por meio de um simples chat. Caso queira saber como seria um número no formato Cisterciense, basta informar o número e enviar.

![image](https://github.com/user-attachments/assets/2da4a950-291c-4cf5-b0f5-44318c7055b2)

Também é possível informar uma imagem clicando no botão de clips, e então o sistema vai retornar o número correspondente a ele.

![image](https://github.com/user-attachments/assets/81f2fede-df0d-4104-9c7e-c9a20928ffc9)
