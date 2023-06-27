# Grupo: Natália, Karle, Luiz Neto, Gigliarly e Hyago
import time 
from ouvidoria import Ouvid
from Ouvi3def import Conexao
ouvidoria = Conexao()
condicao = True
for c in range(3):
  print('.')
  time.sleep(0.2)
  print('\033[1;31m')
menu = """.......................................................
Bem vindo ao menu da Ouvidoria!   
1) Para listar reclamações
2) Para adicionar reclamações
3) Para remover reclamações
4) Para pesquisar reclamações
5) Para sair do programa
......................................................."""
print('\033[1;31m')

tipos_ocorrencia = """
Tipos para cadastro:
1) Elogio
2) Reclamacao
3) Sugestao
4) Todas
"""
tipos_normais = """1) Elogio
2) Reclamacao
3) Sugestao
4) Todas
"""
while condicao:
  print(menu)
  escolha = input('-> ')
  
  if escolha == '1':
    print('Qual vai ser o tipo da lista?')
    if not ouvidoria.tipo:
      print("Lista vazia")
      continue
    tipo = input(f'{tipos_normais}->')
    resultado = ouvidoria.listar_ocorrencia(tipo)
    print(resultado)
  
  for c in range(3):
    print('.')
    time.sleep(0.2)
  
  
  if escolha == '2':
    print(tipos_ocorrencia)
    tipo = input('Nome do tipo da ocorrência: ')
    titulo = input('Titulo: ')
    descricao = input('Descricao: ')
    posicao = ouvidoria.adicionar_reclamacao(titulo, tipo.lower(), descricao)
    print(posicao)
  
  for c in range(3):
    print('.')
    time.sleep(0.2)
  
  if escolha == '3':
    index = int(input('Index: '))
    ouvidoria.remover_reclamacao(index)
  
  for c in range(2):
    print('.')
    time.sleep(0.2)
  
  if escolha == '4':
    numero_pesquisa = input('Numero de pesquisa: ')
    pesquisa = ouvidoria.pesquisar_ocorrencia(numero_pesquisa)
    if pesquisa:
      print(f"""-----------------
Titulo: {pesquisa[0]};
Tipo: {pesquisa[1]};
Descricao: {pesquisa[2]}
-----------------""")
    
  if escolha == '5':
    condicao = False
    print('\nVocê escolheu sair do sistema. Para fazer de novo, por gentileza reinicie o programa!')
    ouvidoria.close_conexao()
    for c in range(2):
      print('.')
      time.sleep(0.2)

