from Ouvi3def import Conexao

ouvidoria = Conexao()

menu = ''''\033[32m'
 =========================================================
            BEM VINDO(A) AO SISTEMA DE OUVIDORIA!
1) Listar Ocorrências
2) Adicionar Ocorrências
3) Remover Ocorrências
4) Procurar Ocorrências por Código
5) Sair do programa
 ========================================================= '\033[32m'''

opcoes_tipos = '''
1) Elogios
2) Reclamações
3) Sugestões
4) Todas'''

op_registro ='''
1) Elogios
2) Reclamações
3) Sugestões'''


oco = int
while oco != 5:
    ouvidoria.tempo()
    print(menu)
    oco = int(input('digite qual voce deseja \n-->'))
    if oco ==1:
        print(op_registro)
        lista_ocorrencia = ouvidoria.listar_ocorrencia()
        for item in lista_ocorrencia:
             print(item)


    elif oco == 2:
        print(op_registro)
        print()
        tipos = int(input('Qual tipo você deseja selecionar? \n -->'))
        if tipos == 1:
            ouvidoria.registrar_ocorrencia_elogio()
        elif tipos == 2:
                ouvidoria.registrar_ocorrencia_reclamacao()
        elif tipos == 3:
                ouvidoria.registrar_ocorrencia_sugestao()

    elif oco == 3:
        delet = int(input('qual o Código da ocorrência? \n-->'))
        ouvidoria.deletar_ocorrencia(delet)

    elif oco ==4:
        pesq = int(input('Qual o código da Ocorrência que você deseja pesquisar? \n--->'))
        ouvidoria.pesquisar_ocorrencia(pesq)

    elif oco ==5:
        print('Você escolheu sair do sistema, volte sempre!')
        ouvidoria.close_conexao()

