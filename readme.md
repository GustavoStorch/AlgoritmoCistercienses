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

Como Executar o Projeto
Para executar o projeto, é necessário iniciar tanto o backend (API) quanto o frontend. Utilize dois terminais separados para isso.

Pré-requisitos
Python 3.12

Node.js 18.12.0 e npm

Passo 1: Clonar o Repositório
bash
Copiar
Editar
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Passo 2: Configurar e Iniciar o Backend (API)
Navegue até o diretório da API:

bash
Copiar
Editar
cd API
Crie e ative um ambiente virtual:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Inicie a aplicação Flask:

bash
Copiar
Editar
python main.py
A API estará disponível em http://localhost:5000.

Passo 3: Configurar e Iniciar o Frontend
Abra um novo terminal e navegue até o diretório do frontend:

bash
Copiar
Editar
cd FrontEnd
Instale as dependências:

bash
Copiar
Editar
npm install
Inicie a aplicação React:

bash
Copiar
Editar
npm start
A aplicação estará disponível em http://localhost:3000.