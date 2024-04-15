2. Crie uma classe que modele uma aluno
(a) Atributos: nome, numero de matrıcula e curso
(b) Metodos: mostrar curso e alterar curso 

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
