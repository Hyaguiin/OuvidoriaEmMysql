# Grupo: Natália, Karle, Luiz Neto, Gigliarly e Hyago
import time 
from ouvidoria import Ouvidoria
from CONEXAO import Conexao

conexao = Conexao()
ouvidoria = Ouvidoria()
condicao = True

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
2) reclamacao
3) Sugestao
4) Todas
"""
tipos_normais = """1) Elogio
2) reclamacao
3) Sugestao
4) Todas
"""
while condicao:
  print(menu)
  escolha = input('-> ')

  for c in range(3):
    print('.')
    time.sleep(0.2)
  
  if escolha == '1':
    print('Qual vai ser o tipo da lista?')
    
    tipo = input(f'{tipos_normais}->')
    resultado = ouvidoria.listar_ocorrencia(tipo)

    print(resultado)
    input('Aperte ENTER, pra continuar!!')
  
  if escolha == '2':
    print(tipos_ocorrencia)
    tipo = input('Tipo: ')
    titulo = input('Titulo: ')
    descricao = input('Descricao: ')
    posicao = ouvidoria.adicionar_ocorrencia(titulo, tipo.lower(), descricao)
    print(posicao)
  
  if escolha == '3':
    index = int(input('Index: '))
    ouvidoria.remover_ocorrencia(index)
  
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

