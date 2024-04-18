class Cliente:

    def __init__(self,nome, ano_de_nascimento, sexo, limite_de_crédito, endereço):
        self.nome = nome
        self.ano_de_nascimento = ano_de_nascimento
        self.sexo = sexo
        self.limite_de_crédito = limite_de_crédito
        self.endereço = endereço

    def imprimir_valores(self):
        print("Nome:"), self.nome
        print("Ano de nascimento:"), self.ano_de_nascimento
        print("Sexo:"), self.sexo
        print("Limite de crédito:", self.limite_de_crédito)
        print("Endereço:", self.endereço)

cliente1 = Cliente("Anderson", 1992, "Masculino", 5000, "Rua Guarani")

cliente1.imprimir_valores()