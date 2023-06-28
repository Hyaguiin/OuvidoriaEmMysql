from CONEXAO import Conexao

class Ouvidoria:
  def __init__(self):
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

    print(lista_ocorrencias)
    for linha in lista_ocorrencias:
      tipo = tipos_cadastraveis[linha[2]-1]
      mensagem+= f"{divisa}\nId: {linha[0]}\nTitulo: {linha[1]}\nTipo: {tipo}\nDescricao: {linha[3]}\n{divisa}\n"

    return mensagem
  
  def adicionar_ocorrencia(self, titulo, tipo, descricao):
    tipos_cadastraveis = ['elogio', 'reclamacao', 'sugestao']

    if tipo in tipos_cadastraveis:
      userId = self.conexao.post_ocorrencia(titulo, tipos_cadastraveis.index(tipo), descricao)
      return userId
    elif int(tipo)-1 <= len(tipos_cadastraveis):
      userId = self.conexao.post_ocorrencia(titulo, int(tipo), descricao)
      return userId

  def remover_ocorrencia(self, codigo):
    pass
    
  def pesquisar_ocorrencia(self, index):
    pass

  def close_conexao(self):
    self.conexao.close_conexao()
      