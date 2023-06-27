class Ouvidoria:
  def __init__(self):
    self.titulo = []
    self.tipo = []
    self.descricao= []
  
  def adicionar_reclamacao(self, titulo, tipo, descricao):
    tipos_cadastraveis = ['elogio', 'reclamacao', 'sugestao']
    self.titulo.append(titulo)
    self.descricao.append(descricao)
    if tipo in tipos_cadastraveis:
      self.tipo.append(tipo)
      return len(self.tipo) 
    if int(tipo)-1 <= len(tipos_cadastraveis):
      numero_index = int(tipo)-1
      if numero_index <= len(tipos_cadastraveis):
        self.tipo.append(tipos_cadastraveis[numero_index])
    print('Uma reclamação foi adicionada')
    return len(self.titulo)

  def remover_reclamacao(self, codigo):
    if 1 <= codigo <= len(self.titulo):
      self.titulo.pop(codigo - 1)
      self.tipo.pop(codigo - 1)
      self.descricao.pop(codigo - 1)
      print('\nSua reclamação foi removida\n')
      return True
    else:
      return False

  def listar_ocorrencia(self, tipo_lista):
    mensagem = ""
    resultado=[]
    lista=[]
    tipos_cadastraveis = ['elogio', 'reclamacao', 'sugestao']
    if tipo_lista == 'todas' or int(tipo_lista)==4:
      for i in range(len(self.tipo)):
        lista.append(self.titulo[i])
        lista.append(self.tipo[i])
        lista.append(self.descricao[i])
        resultado.append(lista)
      for item in resultado:
        mensagem+= f"\nTitulo: {item[0]}\nTipo: {item[1]}\nDescricao: {item[2]}\n"
      return mensagem

    elif tipo_lista in tipos_cadastraveis:
      for i in range(len(self.titulo)):
        if tipo_lista == self.tipo[i]:
          lista.append( self.titulo[i] )
          lista.append( self.tipo[i] )
          lista.append( self.descricao[i] )
          resultado.append( lista )
      for item in resultado:
        mensagem+= f"\nTitulo: {item[0]}\nTipo: {item[1]}\nDescricao: {item[2]}\n"
      return mensagem

    elif 0<int(tipo_lista)<5:
      for i in range(len(self.titulo)):
        if self.tipo[i] == tipos_cadastraveis[int(tipo_lista)-1]:
          lista.append(self.titulo[i])
          lista.append(self.descricao[i])
          resultado.append(lista)
          
      for item in resultado:
        mensagem+=f"\nTitulo: {item[0]}\nDescricao: {item[1]}\n"
      return mensagem
    
  def pesquisar_ocorrencia(self, index):
    indexes = []
    for i in range(1, len(self.tipo)+1):
      indexes.append(f'{i}')
    if index in indexes:
      resultado = [
        self.titulo[ int(index)-1 ],
        self.tipo[ int(index)-1 ],
        self.descricao[ int(index)-1 ]
      ]
      return resultado
    else:
      print('Não existem problemas cadastrados')
      return False
      