class Pessoa:
#Criando o método construtor
def__init__(self,nome,hobby,endereço):
# estamos criando os atributos da classe utilizndo o método construtor. Nesse caso precisamos passar os parâmetros que serão usados como valores dos atributos.
self.nome = nome
self.hobby = hobby
self.endereco = enderenco

# Criando os métodos normais
def exibirDados(self):
    print(f"Olá {self.nome} seu hobby é {self.hobby} e seu endereço é {self.endereco}")

    #CRIANDO OS OBJETOS
    pessoal = Pessoa("Geraldo","Corredor","Rua 10 Cohab")
    pessoa.exibirDados()# chamando o método da classe

    pessoal = Pessoas("Karia", "Artes Marciais","Av 12 Renascenca")
    print(pessoal2.nome)