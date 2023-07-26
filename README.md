<h1 align="center">Analise de personalidades com base no Big Five</h1>
<h3 align="center">Aplicação desenvolvida para o Trabalho de conclusão de curso (TCC) do curso de Bacharelado em Ciência da Computação da Universidade Estadual Paulista "Júlio de Mesquita Filho" (UNESP), campus de Presidente Prudente</h3>
<h1 align="center">
  <img src="https://github.com/DayaToledo/TCC-api/assets/55140068/89ec19dc-f4d4-409e-8736-54068454d5da"/>
</h1>


&nbsp;&nbsp;
<p align="center">
  <img alt="License" src="https://img.shields.io/github/license/dayaToledo/TCC-api?style=for-the-badge"/>&nbsp;&nbsp;
  <img alt="Count languages" src="https://img.shields.io/github/languages/count/DayaToledo/TCC-api?style=for-the-badge"/>&nbsp;&nbsp;
  <img alt="Top language" src="https://img.shields.io/github/languages/top/DayaToledo/TCC-api?style=for-the-badge"/>&nbsp;&nbsp;
  <img alt="Repo size" src="https://img.shields.io/github/repo-size/DayaToledo/TCC-api?style=for-the-badge"/>&nbsp;&nbsp;
</p>


&nbsp;&nbsp;
## 🔍 Sobre

A aplicação tem como objetivo principal tornar possível a predição da personalidade de candidatos a vagas de emprego, utilizando o método Big Five como base para o questionário. Isso auxiliará os recrutadores na análise dos candidatos e facilitará a seleção dos melhores perfis, reduzindo o esforço humano nesse processo.

O método Big Five define cinco grandes fatores que compoem a personalidade de uma pessoa: *Openness to Experience*  (Abertura à Experiência), *Conscientiousness* (Conscienciosidade), *Extraversion* (Extroversão), *Agreeableness* (Agradabilidade) e *Neuroticism* (Neuroticismo). Estes cinco fatores são calculados com base em respostas fornecidas pelos candidatos à um questionário. Neste caso, um individuo tem porcentagens de cada um dos cinco fatores. 

Baseado na pontuação da pessoa para cada um dos cinco fatores, pode ser definido uma personalidade unificada para ela, que diz qual a maior tendência da personalidade. Sendo assim, um individuo possui um pouco de cada um dos cinco fatores em sua personalidade, mas o conjunto deles faz com que ele tenha uma tendencia maior para uma personalidade especifica, unificada. Dentre as possibilidades de personalidade unificada temos: _responsible_ (responsável), _lively_	(animado), _dependable_	(confiável), _extraverted_	(extrovertido) e _serious_ (sério).

<p align="center">  
  <img width="90%" style="border-radius: 5px" alt="Fluxograma Big Five e personalidade unificada" src="https://github.com/DayaToledo/TCC-api/assets/55140068/643ce2cc-2891-44ae-9299-76ef61a6aa8b">
</p>

<p align="center">  
  <img width="80%" style="border-radius: 5px" alt="Exemplo da personalidade de uma pessoa" src="https://github.com/DayaToledo/TCC-api/assets/55140068/5b0d89f9-1d6a-48ea-bbe8-c5289856770d)">
</p>

Esta aplicação utiliza técnicas de _machine learning_ para implementar um modelo preditivo treinado de forma supervisionada, classificando a personalidade das pessoas em duas categorias: *dependable* (confiável) e *responsible* (responsável).

Para desenvolver esse modelo, foram testados diversos algoritmos de treinamento do _Sklearn_, sendo o _LogisticRegression_ o que obteve melhor desempenho, alcançando uma acurácia final de 40%. Visando melhorar ainda mais a acurácia, foi feito um ajuste na base de dados para que o modelo predissesse apenas essas duas personalidades específicas, resultando em uma acurácia final de 61%.

<p align="center">  
  <img width="100%" style="border-radius: 5px" alt="Fluxo de desenvolvimento do modelo de predição" src="https://github.com/DayaToledo/TCC-api/assets/55140068/2421d210-5bc7-409f-9de8-03efc7a89404">
</p>
<p align="center">  
  <img width="50%" style="border-radius: 5px" alt="Resultado da acurácia dos algoritmos testados" src="https://github.com/DayaToledo/TCC-api/assets/55140068/65fd087c-16aa-4384-be7c-4b94b30d1bc7">
</p>

Além disso, foi implementada uma API com FastAPI que utiliza esse modelo preditivo criado para prever a personalidade de uma pessoa, oferecendo um endpoint que simplifica a utilização do sistema, tratando automaticamente os dados de entrada antes de utilizá-los no modelo.

<p align="center">  
  <img width="100%" style="border-radius: 5px" alt="Fluxo de desenvolvimento da API final com endpoint" src="https://github.com/DayaToledo/TCC-api/assets/55140068/a6aabdae-b772-4893-ae2b-98497e656677">
</p>

Ao final do desenvolvimento foram obtidos:

- um modelo preditivo capaz de prever a tendência da personalidade de uma pessoa para *dependable* (confiável) ou *responsible* (responsável)
- um endpoint que recebe as 50 respostas pro método Big Five e retorna a predição da personalidade do candidato

<p align="center">  
  <img width="100%" style="border-radius: 5px" alt="Exemplificação do fluxo do funcionamento da aplicação final" src="https://github.com/DayaToledo/TCC-api/assets/55140068/d45c8895-31e0-4e57-a859-b1b177160c3e">
</p>

Essa aplicação é especialmente valiosa em processos seletivos com muitos candidatos e quando os recrutadores não têm informações prévias sobre a personalidade dos candidatos. Através da predição fornecida pela API, é possível reduzir significativamente o número de candidatos a serem avaliados manualmente, permitindo que os recrutadores se concentrem nos perfis mais compatíveis com as características desejadas para a vaga. Por exemplo, em um processo com mil candidatos em busca de profissionais responsáveis, a predição do modelo permitiria reduzir o número de candidatos, mantendo apenas aqueles com a personalidade requerida para a posição.

Abaixo temos uma exemplificação da utilização do endpoint da API por meio da documentação do Swagger:

<p align="center">  
  <img width="100%" style="border-radius: 5px" alt="Tela inicial do Swagger com endpoint da API" src="https://github.com/DayaToledo/TCC-api/assets/55140068/a257897e-8200-41e5-a184-f2f8d64fd61d">
</p>
<p align="center">  
  <img width="100%" style="border-radius: 5px" alt="Envio de uma requisição" src="https://github.com/DayaToledo/TCC-api/assets/55140068/22d8a76e-14d1-4a41-8702-89447228e289">
</p>
<p align="center">  
  <img width="100%" style="border-radius: 5px" alt="Resposta da requisição solicitada" src="https://github.com/DayaToledo/TCC-api/assets/55140068/3f256f55-a6eb-4657-aaf4-9bcb2aed2557">
</p>


&nbsp;
## ⚒ Tecnologias

Essa aplicação foi desenvolvida utilizando:
- [Pandas](https://pandas.pydata.org/) e [Numpy](https://numpy.org/) na manipulação dos conjuntos de dados em CSV
- [Seaborn](https://seaborn.pydata.org/) e [Matplotlib](https://matplotlib.org/) na elaboração e visualização de gráficos descritivos
- [Sklearn](https://scikit-learn.org/stable/) para criar, treinar e testar os modelos preditivos
- [Pickle](https://docs.python.org/3/library/pickle.html) para salvar e manipular o arquivo que contém o modelo final treinado
- [FastAPI](https://fastapi.tiangolo.com/) para criar a API com Python e o endpoint pra predizer dados
- [Swagger](https://swagger.io/tools/swagger-ui/) (incluido dentro do FastAPI) para a exibição de uma documentação do endpoint de fácil acesso
- [Pydantic](https://docs.pydantic.dev/latest/) para validar os dados recebidos pelo endpoint


&nbsp;
## :rocket: Como executar o projeto

### Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
- [Git](https://git-scm.com)
- [Python](https://www.python.org/) *(Nesse projeto foi usado a versão 3.10.7)*

Além disto é bom ter um editor para trabalhar com o código como o [VSCode](https://code.visualstudio.com/).

E também, neste projeto foi utilizado um ambiente Python para facilitar a manipulação das dependências, então segue algumas referências sobre o assunto:
- [Documentação da biblioteca Python VENV](https://docs.python.org/pt-br/3/library/venv.html)  
- [Tutorial de criação de ambientes virtuais](https://docs.python.org/pt-br/3/tutorial/venv.html#:~:text=Um%20diret%C3%B3rio%20de%20localiza%C3%A7%C3%A3o%20comum,Tamb%C3%A9m%20previne%20conflitos%20com%20.) 
<br>

### Instalando o projeto e suas dependências
1. Confira se você tem o Python instalado na sua máquina: `python --version`

2. Faça clone do repositório localmente na sua máquina: `git clone git@github.com:DayaToledo/TCC-api.git`

3. Acesse a pasta raiz do projeto (pasta onde tem o arquivo requirements.txt)

4. Crie um ambiente virtual Python para o projeto: `python -m venv tcc`

5. Ative o ambiente Python que acabou de criar: `source tcc/Scripts/activate`

6. Atualize o pip antes de instalar as dependências: `python -m pip install --upgrade pip`

7. Instale as dependências do projeto: `pip install -r requirements.txt`
<br>

### Para treinar um modelo

Para treinar o modelo de predição, rode o comando seguinte:

`python src/scripts/trainer.py LogisticRegression specific`

- `LogisticRegression` é o primeiro argumento, e indica qual algoritmo será usado no treinamento
- `specific` é o segundo argumento, e indica se será treinado com o conjunto de dados especifico (somente *dependable* e *responsible*) ou não 

<br>

### Para rodar e utilizar a API
1. Rode o comando pra executar a API: 
  <br>  `uvicorn --port 8080 src.api.main:app`
2. Acesse o endpoint pela documentação do Swagger oferecida pelo navagador: 
  <br>  `http://localhost:8080/docs#`



&nbsp;
## 📃 Licença
Esse repositório está licenciado pela **MIT LICENSE**. Para mais informações detalhadas, leia o arquivo [LICENSE](./LICENSE) contido nesse repositório


&nbsp;
## 👩‍💻 Autor
Feito por [Dayana Toledo](https://www.linkedin.com/in/toledodayana/). Entre em contato!
