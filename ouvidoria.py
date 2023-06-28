from CONEXAO import Conexao

class Ouvidoria:
  def __init__(self):
    self.ocorrencias= []
    self.conexao = Conexao()

  def listar_ocorrencia(self, tipo_lista):
    tipos_cadastraveis = ['elogio', 'reclamacao', 'sugestao']
    lista_ocorrencias=[]
    mensagem=''
    if tipo_lista in tipos_cadastraveis:
      lista_ocorrencias = self.conexao.get_ocorrencia(tipos_cadastraveis.index(tipo_lista))
    elif int(tipo_lista) <= 3:
      lista_ocorrencias = self.conexao.get_ocorrencia( int(tipo_lista)-1 )
    else:
      lista_ocorrencias = self.conexao.get_ocorrencia(4)
    
    divisa='-'*20

    for linha in lista_ocorrencias:
      tipo = tipos_cadastraveis[linha[2]-1]
      mensagem+= f"{divisa}\nId: {linha[0]}\nTitulo: {linha[1]}\nTipo: {tipo}\nDescricao: {linha[3]}\n{divisa}\n"

    return mensagem
  
  def adicionar_ocorrencia(self, titulo, tipo, descricao):
    tipos_cadastraveis = ['elogio', 'reclamacao', 'sugestao']

    if int(tipo)-1 < len(tipos_cadastraveis):
      userId = self.conexao.post_ocorrencia(titulo, int(tipo), descricao)
      return userId

  def remover_ocorrencia(self, id):
    return self.conexao.delete_ocorrencia(id)
    
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

  def close_conexao(self):
    self.conexao.close_conexao()
      