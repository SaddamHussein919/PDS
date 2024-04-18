class Aluno:

    def __init__(self,nome, idade, sexo, RA, cpf, rg, nota1, nota2):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.RA = RA
        self.cpf = cpf
        self.rg = rg
        self.nota1 = nota1
        self.nota2 = nota2

    def imprimir_valores(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Sexo:", self.sexo)
        print("RA:", self.RA)
        print("Cpf:", self.cpf)
        print("Rg:", self.rg)
        print("Nota 1:", self.nota1)
        print("Nota 2:", self.nota2)

aluno1 = Aluno("David", 19, "Masculino", 11802385282, "117-790-852-83", "23 456 789-1", 40, 25)

aluno1.imprimir_valores()