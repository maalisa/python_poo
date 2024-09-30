class Pessoa:
    #Atributos - são as características da classe
    nome = "Fulano"
    Idade = 25
    Altura = 1.60

    #métodos - são os comportamentos da classe
    def falar (self,texto):# self é o parâmetro obrigatório do python que informa que o método pertence á própria classe que foi criada.
        print(f"Tenho algo pra te falar:{texto}")

    # CRIANDO OBJETOS
    pessoal = Pessoas () # dessa forma estamos criando um objeto do tipo de pessoa

    print(pessoal.nome, pessoal.idade)
    pessoal.falar("Bom dia, hoje é segunda-feira")