# Bottle Counter CV

Sistema de contagem automática de garrafas em linhas de produção utilizando **Visão Computacional** e **Redes Neurais Convolucionais (CNN)**.

## Sobre o projeto

O Bottle Counter CV tem como objetivo automatizar o processo de contagem de garrafas em linhas de produção industrial por meio de técnicas de visão computacional e inteligência artificial.

A solução utiliza processamento digital de imagens e redes neurais convolucionais para identificar garrafas em imagens ou vídeos, possibilitando a contagem automática dos objetos detectados.

O projeto busca demonstrar a aplicação de técnicas de aprendizado profundo (*Deep Learning*) em cenários de automação industrial, reduzindo a necessidade de contagem manual e contribuindo para a eficiência dos processos produtivos.

## Tecnologias utilizadas

- **Python** – Linguagem de programação.
- **OpenCV** – Processamento e análise de imagens.
- **Redes Neurais Convolucionais (CNN)** – Detecção e reconhecimento de objetos.
- **Deep Learning** – Técnicas de aprendizado profundo.
- **NumPy** – Operações e manipulação de dados numéricos.

## Funcionalidades

- Detecção automática de garrafas.
- Processamento de vídeos.
- Contagem automática dos objetos identificados.
- Aplicação de modelos de redes neurais convolucionais.
- Análise visual dos resultados da detecção.

## Requisitos

- Dependências listadas em `requirements.txt`.

## Instalação e execução

### Linux (Ubuntu)

**1. Clone o repositório**

```bash
git clone https://github.com/SEU_USUARIO/bottle-counter-cv.git
cd bottle-counter-cv
```

**2. Crie um ambiente virtual**

```bash
python3 -m venv venv
```

**3. Ative o ambiente virtual**

```bash
source venv/bin/activate
```

**4. Atualize o pip**

```bash
python -m pip install --upgrade pip
```

**5. Instale as dependências**

```bash
pip install -r requirements.txt
```

**6. Execute o projeto**

```bash
python main.py
```

### Windows

**1. Clone o repositório**

```powershell
git clone https://github.com/SEU_USUARIO/bottle-counter-cv.git
cd bottle-counter-cv
```

**2. Crie um ambiente virtual**

```powershell
python -m venv venv
```

**3. Ative o ambiente virtual**

```powershell
.\venv\Scripts\Activate.ps1
```

Caso utilize o Prompt de Comando (CMD):

```cmd
venv\Scripts\activate.bat
```

**4. Atualize o pip**

```powershell
python -m pip install --upgrade pip
```

**5. Instale as dependências**

```powershell
pip install -r requirements.txt
```

**6. Execute o projeto**

```powershell
python main.py
```

## Contribuição

Contribuições são bem-vindas! Para colaborar:

1. Faça um fork do repositório.
2. Crie uma branch para sua funcionalidade (`git checkout -b feature/nova-funcionalidade`).
3. Faça commit das alterações (`git commit -m "feat: adiciona nova funcionalidade"`).
4. Envie as alterações (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

## Autor

Iago Rocha Oliveira(IagoRochaDev)
