from CONEXAO import Conexao

class Ouvidoria:
  def __init__(self):
    self.ocorrencias= []
    self.conexao = Conexao()


  # Nesse metodo esse pega o dado que é o tipo da lista,
  # # e envia os dados para a classe conexao
  # e retorna uma lista de tuplas, mostrando todos os dados
  # que estão com o tipo escolhido e retorna uma mensagem
  # com todas os dados da tabela no banco de dados
  def listar_ocorrencia(self, tipo_lista):
    tipos_cadastraveis = ['elogio', 'reclamacao', 'sugestao']
    self.lista_ocorrencias = []
    mensagem = ''

    if tipo_lista in tipos_cadastraveis:
      lista_ocorrencias = self.conexao.get_ocorrencia(tipos_cadastraveis.index(tipo_lista) + 1)
    elif 1 <= int(tipo_lista) <= 3:
      lista_ocorrencias = self.conexao.get_ocorrencia(int(tipo_lista))
    else:
      lista_ocorrencias = self.conexao.get_ocorrencia(int(tipo_lista))

    divisa = '-' * 20

    for linha in lista_ocorrencias:
      tipo = tipos_cadastraveis[int(linha[2]) - 1]
      mensagem += f"{divisa}\nId: {linha[0]}\nTítulo: {linha[1]}\nTipo: {tipo}\nDescrição: {linha[3]}\n{divisa}\n"

    return mensagem

    divisa='-'*20

    for linha in lista_ocorrencias:
      tipo = tipos_cadastraveis[linha[2]-1]
      mensagem+= f"{divisa}\nId: {linha[0]}\nTitulo: {linha[1]}\nTipo: {tipo}\nDescricao: {linha[3]}\n{divisa}\n"

    return mensagem
  
  # Pega os dados do parametro (que é fornecido pelo main.py),
  # entao enviar os dados para para cadastrar no banco de dados
  def adicionar_ocorrencia(self, titulo, tipo, descricao):
    tipos_cadastraveis = ['elogio', 'reclamacao', 'sugestao']

    if int(tipo)-1 < len(tipos_cadastraveis):
      userId = self.conexao.post_ocorrencia(titulo, int(tipo), descricao)
      print()
      print(f'Ocorência Registrada com sucesso! Código: {userId}')


  # Envia os dados recebidos e executa a funcao para excluir uma linha na tabela
  def remover_ocorrencia(self, id):
    self.listar_ocorrencia(4)
    return self.conexao.delete_ocorrencia(id)
    
  # Aqui ele pesquisa tendo o id, e monta a mensagem para enviar a mensagem no main.py
  def pesquisar_ocorrencia(self, index):
    tipos_cadastraveis = ['elogio', 'reclamacao', 'sugestao']

    lista_ocorrencia = self.conexao.search_ocorrencia(index)
    mensagem = ''
    divisao = '-'*20
    for ele in lista_ocorrencia:
      mensagem+= divisao
      mensagem+= f'Id: {ele[0]}'
      mensagem+= f'\nTitulo: {ele[1]}'
      mensagem+= f'\nTipo: {tipos_cadastraveis[ele[2]-1]}'
      mensagem+= f'\nDescrição: {ele[3]}\n'
      mensagem+= divisao
    return mensagem

  # Fecha a conexao
  def close_conexao(self):
    self.conexao.close_conexao()
      