from CONEXAO import Conexao

class Ouvidoria:
  def __init__(self):
    self.titulo= ''
    self.tipo= ''
    self.descricao= ''

class Ouvidoria:
  def __init__(self):
    self.ocorrencias= []
    self.conexao = Conexao()

  def listar_ocorrencia(self, tipo_lista):
    tipos_cadastraveis = ['elogio', 'reclamacao', 'sugestao', 'todas']
    lista_ocorrencias=[]
    mensagem=''
    if tipo_lista in tipos_cadastraveis:
      lista_ocorrencias = self.conexao.get_ocorrencia(tipo_lista)
    elif int(tipo_lista) < 4:
      lista_ocorrencias = self.conexao.get_ocorrencia( tipos_cadastraveis[int(tipo_lista)] )
    
    divisa='-'*20

    for linha in lista_ocorrencias:
      mensagem+= f"{divisa}\nId: {linha[0]}\nTitulo: {linha[1]}\nTipo: {linha[2]}\nDescricao: {linha[3]}\n{divisa}\n"

    return mensagem
  
  def adicionar_ocorrencia(self, titulo, tipo, descricao):
    tipos_cadastraveis = ['elogio', 'reclamacao', 'sugestao']

    if tipo in tipos_cadastraveis:
      userId = self.conexao.post_ocorrencia(titulo, tipo, descricao)
      return userId
    elif int(tipo)-1 < len(tipos_cadastraveis):
      userId = self.conexao.post_ocorrencia(titulo, tipos_cadastraveis[int(tipo)], descricao)
      return userId

  def remover_ocorrencia(self, codigo):
    pass
    
  def pesquisar_ocorrencia(self, index):
    pass

  def close_conexao(self):
    self.conexao.close_conexao()
      