# Detector de Línguas
Detecção de línguas a partir de frase de entrada, classificando a língua segundo seu [código](https://www.alchemysoftware.com/livedocs/ezscript/Topics/Catalyst/Language.htm).

Para esta aplicação foi utilizada a biblioteca [langid](https://github.com/saffsd/langid.py), que classifica frases de entrada em uma de 97 línguas.

## Resultados Obtidos

A classificação de línguas teve um resultado satisfatório, diferenciando corretamente ou, quando errado, em línguas que se assemelham com a esperada.

|Frase|Língua Esperada|Língua Obtida|
|-----|------|------|
|The sun is shining brightly in the sky|en|en|
|El cielo está despejado y azul.|es|es|
|Le soleil brille dans le ciel|fr|fr|
|Die Sonne scheint hell am Himmel.|de|de|
|Il sole splende nel cielo.|it|it|
|太陽が空に輝いています。|ja|ja|
|太阳照耀着天空。|zh|zh|
|Солнце ярко светит на небе.|ru|bg|
|الشمس تشرق في السماء بوضوح.|ar|ar|
|सूरज आसमान में चमक रहा है।|hi|hi|

Da tabela de exemplos, apenas a frase em Russo (ru) obteve um resultado diferente do esperado, sendo classificada como Búlgaro (bg), que se assemelha a Russo.


## Como usar

### Preparar ambiente

Utilizando Python 3.11
1. Criar um ambiente virtual: `python -m venv venv`
2. Ativar o ambiente virtual: `venv\Scripts\activate.bat` (No Windows)
3. Instalar as bibliotecas: `pip install -r requirements.txt`

### Rodar o programa
1. Ativar o ambiente virtual: `venv\Scripts\activate.bat` (Caso não esteja)
2. Executar o arquivo [main](main.py): `python main.py`
3. Digitar uma frase ou `0` para parar a aplicação
