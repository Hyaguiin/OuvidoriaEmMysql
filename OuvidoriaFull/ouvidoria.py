from CONEXAO import Conexao

class Ouvidoria:
  def __init__(self):
    self.titulo= ''
    self.tipo= ''
    self.descricao= ''

class Ouvidoria:
  def __init__(self):
    self.ocorrencias=[]
    self.conexao = Conexao()

  def listar_ocorrencia(self, tipo_lista):
    pass
  
  def adicionar_ocorrencia(self, titulo, tipo, descricao):
    tipos_cadastraveis = ['elogio', 'reclamacao', 'sugestao']

    if tipo in tipos_cadastraveis:
      self.ocorrencias.append(
        Ouvidoria(titulo, tipo, descricao)
      )
      return len(self.ocorrencias)
    if int(tipo)-1 < len(tipos_cadastraveis):
      numero_index = int(tipo)-1
      self.ocorrencias.append(
        Ouvidoria(titulo, tipos_cadastraveis[numero_index], descricao)
      )


  def remover_reclamacao(self, codigo):
    pass
    
  def pesquisar_ocorrencia(self, index):
    pass
      