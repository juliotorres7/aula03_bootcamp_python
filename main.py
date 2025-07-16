### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# quantidade = -10
# preco = 20

# if quantidade>0 and preco>0:
#     print("Valores aceitos")
# else:
#     print("Valores recusados")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# temperatura = 45

# if temperatura<10:
#     print("Baixa")
# elif temperatura>=10 and temperatura<25:
#     print("Normal")
# else:
#     print("Alta")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}


# erro = log.get("level")

# print(erro)

# for i in log.values():
#     if i == "ERROR":
#         print(f"o elemento {i} está com erro")


### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# idade_usuario = 30
# email_usuario = "julio.torresoutlook.com"

# if idade_usuario <= 18 and idade_usuario>=65:
#     print("Idade invalida")
# elif  "@" not in email_usuario or "." not in email_usuario:
#     print("e-mail invalido")
# else:
#     print("Dados de usuarios valido")

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# transacao = {'valor': 12000, 'hora': 20}

# if transacao['valor']>10000 or (transacao["hora"]<9 and transacao["hora"]>20):
#     print("transacao suspeita")
# else:
#     print("transacao ok")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# texto = "Eu vejo um futuro brilhante, eu vejo um futuro de paz, eu vejo um futuro de esperança"

# texto_revisado = texto.lower()

# texto_split = texto_revisado.split(" ")

# contar_palavras = {}

# for palavra in texto_split:
#     if palavra in contar_palavras:
#         contar_palavras[palavra] += 1
#     else:
#         contar_palavras[palavra] = 1

# print(contar_palavras)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# lista_numeros = [10,20,30,40,5, 15,0, 10]
# lista_normalizada = []

# minimo = min(lista_numeros)
# maximo = max(lista_numeros)

# for numero in lista_numeros:
#     lista_normalizada.append(( numero - minimo) / (maximo - minimo))

# print(lista_normalizada)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# for dicionario, d  in enumerate(usuarios):
#     for key, value in d.items():
#         if value == "":
#             print(f"dicionario index {dicionario} tem elemento vazio")
    

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# lista_numeros = [1,5,8,9,12]

# numeros_pare = []

# for i in lista_numeros:
#     if i % 2 == 0:
#         numeros_pare.append(i)

# print(numeros_pare)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# total_por_categori = {}

# for i in vendas:
#     categoria = i["categoria"]
#     total_venda = i["valor"]
#     if categoria in total_por_categori:
#         total_por_categori[categoria] += total_venda
#     else:
#         total_por_categori[categoria] = total_venda

# print(total_por_categori)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# dados = []
# entrada = ""

# while entrada != "sair":
#     entrada = input("entre um palavra ")

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# lista_de_numero = [4]
# entrada = 0


# while entrada not in lista_de_numero:
#     entrada = int(input("Entre um numero até acertar "))

numero = int(input("Digite um número entre 1 e 10: "))
while numero < 1 or numero > 10:
    print("Número fora do intervalo!")
    numero = int(input("Por favor, digite um número entre 1 e 10: "))

print("Número válido!")

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.