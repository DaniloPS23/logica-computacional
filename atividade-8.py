
1. Crie uma classe que modele uma pessoa

(a) Atributos: nome, idade e endereço

(b) Metodos: mostrar endereço e alterar endereço


class Pessoa:

  def __init__(self,nome, idade, endereco):
   self.nome= nome
   self.idade= idade
   self.endereco= endereco

  def mudar_endereco(self,novo_endereco):
   self.endereco= novo_endereco

  def retornar_endereco(self):
    print(self.endereco)

  def deletar_endereco(self):
    self.endereco=None

idade=int(input('insira sua idade: '))
nome=str(input('insira seu nome: '))
endereco_inicial=str(input('insira seu endereco: '))

pessoa1=Pessoa(nome, idade, endereco_inicial)

print(pessoa1.nome)
print(pessoa1.endereco)
print(pessoa1.idade)

pessoa1.deletar_endereco()

pessoa1.mudar_endereco('rua 2')

pessoa1.retornar_endereco()


2. Crie uma classe que modele uma aluno

(a) Atributos: nome, numero de matrıcula e curso

(b) Metodos: mostrar curso e alterar curso ´


class Aluno:
  def __init__(self,nome, numero_de_matricula, curso ):
   self.nome= nome
   self.numero_de_matricula= numero_de_matricula
   self.curso= curso
  def mudar_curso(self, novo_curso):
    self.curso= novo_curso
  def retornar_curso(self):
   print(self.curso)
  def deletar_curso(self):
   self.curso=None

nome=str(input('insira um nome: '))
numero_de_matricula=int(input('insira o numero de sua matricula: '))
curso=str(input('insira o curso que esta fazendo: '))

aluno1=Aluno(nome, numero_de_matricula, curso)

print(aluno1.nome)
print(aluno1.numero_de_matricula)
print(aluno1.curso)


aluno1.deletar_curso()

aluno1.mudar_curso('banco de dados')

aluno1.retornar_curso()

3. Crie uma classe representando os alunos de um determinado curso. A classe deve conter os atributos matr´ıcula do aluno, nome, nota da primeira prova, nota da segunda prova e nota da terceira prova. Crie metodos para acessar o nome e a media do aluno. ´

(a) Permita ao usuario entrar com os dados de 5 alunos. ´

(b) Encontre o aluno com maior media geral. ´

(c) Encontre o aluno com menor media geral ´

(d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para
aprovac¸ao.  


class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3
    
    def esta_aprovado(self):
        return self.calcular_media() >= 6

# (a) Permitindo ao usuário entrar com os dados de 5 alunos
alunos = []
for i in range(5):
    matricula = input("Matrícula do aluno {}: ".format(i+1))
    nome = input("Nome do aluno {}: ".format(i+1))
    nota1 = float(input("Nota da primeira prova do aluno {}: ".format(i+1)))
    nota2 = float(input("Nota da segunda prova do aluno {}: ".format(i+1)))
    nota3 = float(input("Nota da terceira prova do aluno {}: ".format(i+1)))
    aluno = Aluno(matricula, nome, nota1, nota2, nota3)
    alunos.append(aluno)

# (b) Encontrando o aluno com maior média geral
melhor_aluno = max(alunos, key=lambda aluno: aluno.calcular_media())
print("O aluno com maior média geral é:", melhor_aluno.nome, "com média", melhor_aluno.calcular_media())

# (c) Encontrando o aluno com menor média geral
pior_aluno = min(alunos, key=lambda aluno: aluno.calcular_media())
print("O aluno com menor média geral é:", pior_aluno.nome, "com média", pior_aluno.calcular_media())

# (d) Verificando se cada aluno foi aprovado ou reprovado
for aluno in alunos:
    if aluno.esta_aprovado():
        print(aluno.nome, "foi aprovado.")
    else:
        print(aluno.nome, "foi reprovado.")
