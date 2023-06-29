# Grupo: Natália, Karle, Luiz Neto, Gigliarly, Hyago e Rafaela

# Esse arquivo será usado para mostrar as mensagens e pegar os dados que o cliente digitar

#opcional
import time

from ouvidoria import Ouvidoria

ouvidoria = Ouvidoria()
condicao = True

menu = """.......................................................
Bem vindo ao menu da Ouvidoria!   
1) Para listar ocorrencia
2) Para adicionar ocorrencia
3) Para remover ocorrencia
4) Para pesquisar ocorrencia
5) Para sair do programa
......................................................."""
print('\033[1;31m')

tipos_ocorrencia = """
Tipos para cadastro:
1) Elogio
2) reclamacao
3) Sugestao
"""
tipos_normais = """1) Elogio
2) reclamacao
3) Sugestao
4) Todas
"""

# Inicio do loop para mostrar os dados
while condicao:
  print(menu)
  escolha = input('-> ')

  for c in range(3):
    print('.')
    time.sleep(0.2)
  
  if escolha == '1':
    print('Qual vai ser o tipo da lista?')
    
    tipo = input(f'{tipos_normais}->')
    # aqui esse código pega o que o cliente digitou e
    # envia para o metodo listar_ocorrencia que está na classe ouvidoria
    resultado = ouvidoria.listar_ocorrencia(tipo)

    # Aqui ele retorna a mensagem montada pelo o metodo
    print(resultado)
    input('Aperte ENTER, pra continuar!!')
  
  if escolha == '2':
    print(tipos_ocorrencia)
    
    tipo = int(input('Tipo: '))
    titulo = input('Titulo: ')
    descricao = input('Descricao: ')
    # Pega os dados tipo, titulo, descricao e envia esses
    # dados para o metodo adicionar_ocorrencia da classe Ouvidoria
    posicao = ouvidoria.adicionar_ocorrencia(titulo, tipo, descricao)

  
  if escolha == '3':
    mensagem = ouvidoria.listar_ocorrencia(4)
    print(mensagem)
    index = int(input('Index: '))
    # Pega o dado index e envia esse
    # dados para o metodo remover_ocorrencia da classe Ouvidoria
    # Que devolver aqui o resultado (linha), uma confirmação que remover
    linha = ouvidoria.remover_ocorrencia(index)

    print(linha)
  
  if escolha == '4':
    numero_pesquisa = int(input('Numero de pesquisa: '))
    pesquisa = ouvidoria.pesquisar_ocorrencia(numero_pesquisa)

    # mesma coisa da parte de remover, porem esse retorna uma mensagem
    # que é uma mensagem montadada pela a classe Ouvidoria, dizendo o titulo
    # tipo, descricao, e o id
    print(pesquisa)
    
  if escolha == '5':
    condicao = False
    print('\nVocê escolheu sair do sistema. Para fazer de novo, por gentileza reinicie o programa!')
    
    # aqui ele Fecha a conexao com o banco de dados
    ouvidoria.close_conexao()

