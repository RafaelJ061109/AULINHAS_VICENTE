📚 RESUMO UNIFICADO DOS DOIS MATERIAIS

(Classes + Encapsulamento)

🧠 Parte 1 — Classes e Objetos (Material anterior)

O primeiro material apresentou os fundamentos da Programação Orientada a Objetos (POO).

📌 O que é uma classe

Uma classe é um molde para criar objetos.

Exemplo:

class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

Ela define:

características (atributos)
comportamentos (métodos)
📌 O que é um objeto

Um objeto é uma instância da classe.

Exemplo:

produto = Produto("Arroz", 10, 5.0)

Agora temos um produto com:

nome
quantidade
preço
📌 Métodos

São funções dentro da classe.

Exemplo:

def adicionar(self, qtd):
    self.quantidade += qtd

Permitem modificar o comportamento do objeto.

📌 Uso em sistema real

Foi desenvolvido um sistema simples de estoque, permitindo:

adicionar produtos
remover produtos
listar estoque
🧠 Parte 2 — Encapsulamento (Capítulo 3)

Agora o foco foi proteger os dados dos objetos.

📌 Problema do acesso direto

Antes:

produto.quantidade = -50

Isso gera:

❌ dados inválidos
❌ erros futuros
❌ inconsistência

📌 O que é Encapsulamento

Encapsulamento significa:

👉 proteger dados e controlar acesso a eles

Em vez de alterar diretamente:

produto.quantidade -= 5

Usamos:

produto.remover(5)
📌 Níveis de acesso em Python

Existem 3 níveis:

🔹 Público
self.nome

Pode ser acessado livremente.

🔹 Protegido
self._quantidade

É apenas uma convenção.

🔹 Privado
self.__preco

Usa:

👉 name mangling

Internamente vira:

_Produto__preco

Isso dificulta acesso indevido.

📌 Controle com métodos

Agora os dados são acessados assim:

def obter_quantidade(self):
    return self.__quantidade

E alterados assim:

def remover(self, qtd):
    self.__quantidade -= qtd
📌 Validação de dados

Podemos impedir erros:

def remover(self, qtd):
    if qtd <= self.__quantidade:
        self.__quantidade -= qtd
    else:
        print("Quantidade insuficiente")

Agora:

❌ quantidade negativa não acontece

📌 Classe Produto final (Refatorada)
class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.__quantidade = quantidade
        self.__preco = preco

    def adicionar(self, qtd):
        if qtd > 0:
            self.__quantidade += qtd

    def remover(self, qtd):
        if 0 < qtd <= self.__quantidade:
            self.__quantidade -= qtd

    def atualizar_preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco

    def obter_quantidade(self):
        return self.__quantidade

    def obter_preco(self):
        return self.__preco
💻 TUTORIAIS PRÁTICOS DE PROGRAMAÇÃO

(Seção prática separada)

🧪 Tutorial 1 — Criar uma Classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

Criando objeto:

p1 = Pessoa("Ana", 20)
print(p1.nome)
🧪 Tutorial 2 — Criar um Sistema de Estoque
estoque = []

nome = input("Nome do produto: ")
quantidade = int(input("Quantidade: "))
preco = float(input("Preço: "))

produto = Produto(nome, quantidade, preco)

estoque.append(produto)
🧪 Tutorial 3 — Listar estoque usando for
for produto in estoque:
    print(
        produto.nome,
        produto.obter_quantidade(),
        produto.obter_preco()
    )
🧪 Tutorial 4 — Validação com if
idade = int(input("Idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
🔁 GUIA — FUNÇÕES E ESTRUTURAS DE REPETIÇÃO
📌 Funções em Python

Função é um bloco reutilizável.

Criar função
def saudacao():
    print("Olá!")

Executar:

saudacao()
Função com parâmetros
def soma(a, b):
    print(a + b)
Função com retorno
def soma(a, b):
    return a + b
🔁 Estrutura for

Usada quando sabemos quantas repetições.

for i in range(5):
    print(i)

Saída:

0
1
2
3
4
🔁 for in com lista
nomes = ["Ana", "Carlos", "João"]

for nome in nomes:
    print(nome)
🔁 Estrutura while

Repete enquanto condição for verdadeira.

contador = 0

while contador < 5:
    print(contador)
    contador += 1
🔁 break

Interrompe loop.

while True:
    numero = int(input("Digite 0 para sair: "))

    if numero == 0:
        break
🔁 continue

Pula repetição.

for i in range(5):

    if i == 2:
        continue

    print(i)
📊 TABELA — TRATAMENTO DE DADOS EM PYTHON

(com utilidades reais, erros e aplicações práticas)

Comando	O que faz	Exemplo	Quando usar	Possível erro	Utilidade prática real
.strip()	Remove espaços	" João ".strip()	Limpar entrada do usuário	Não funciona em números	Limpar nome em cadastro
.replace()	Substitui texto	"123-456".replace("-", "")	Padronizar dados	Substituir algo errado	Remover hífens de CPF em cadastro
.lower()	Minúsculo	"Ana".lower()	Comparações	Confundir com .upper()	Validar login independente de maiúsculas
.upper()	Maiúsculo	"ana".upper()	Padronização	Pode alterar nomes	Gerar códigos padronizados
.capitalize()	Primeira maiúscula	"joão".capitalize()	Formatar nomes	Não corrige nomes compostos	Ajustar nome em cadastro
.title()	Cada palavra maiúscula	"joao silva".title()	Formatar nomes completos	Pode alterar "da", "de"	Cadastro de clientes
.split()	Divide texto	"1,2,3".split(",")	Ler dados separados	Separador errado	Ler lista de produtos digitados
.join()	Junta textos	" ".join(lista)	Criar frases	Lista com número gera erro	Montar endereço completo
.isdigit()	Verifica número	"123".isdigit()	Validar entrada numérica	Retorna False para negativos	Validar idade
.startswith()	Verifica início	"admin123".startswith("admin")	Validar prefixos	Prefixo incorreto	Verificar login administrativo
.endswith()	Verifica fim	"file.txt".endswith(".txt")	Verificar extensão	Extensão incorreta	Upload de arquivos
.replace(" ", "")	Remove espaços internos	"123 456".replace(" ", "")	Limpar números	Pode remover espaços válidos	Limpar telefone
📌 EXEMPLO REAL — Cadastro usando .replace()

Situação:

Usuário digita CPF:

cpf = input("Digite o CPF: ")

Entrada:

123.456.789-00

Tratamento:

cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")

Resultado:

12345678900

Utilidade:

✔ Armazenar CPF padronizado
✔ Evitar erros de comparação
✔ Facilitar busca no banco

📌 EXEMPLO REAL — Cadastro com .strip()
nome = input("Nome: ").strip()

Entrada:

"   João   "

Resultado:

"João"

Evita erro:

"João" ≠ " João "
📌 POSSÍVEIS ERROS COMUNS
❌ Usar .strip() em número
numero = 123
numero.strip()

Erro:

AttributeError

Solução:

Converter:

numero = str(numero).strip()
🎯 CONCLUSÃO GERAL

Após unir os dois materiais, os principais aprendizados foram:

✔ criação de classes
✔ uso de objetos
✔ encapsulamento
✔ controle de acesso
✔ validação de dados
✔ uso de funções
✔ estruturas for e while
✔ tratamento de dados
✔ criação de sistemas mais seguros
