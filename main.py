import os

print('=+' * 20)
print('Sejam Bem vindo(a)!')
print('Coleta seletiva Pessoa Fisica!')

def menu (): 
    print ('\nEscolha uma opção de 1 a 7 \n') 
    print ('   |1| - Cadastrar cliente') # opção de cadastro para cliente com a função adicionar_cadastro
    print ('   |2| - Remover cliente') # remove cliente cadastrado com função remover_cadastro
    print ('   |3| - Listar cliente') # lista clientes cadastrado na lista
    print ('   |4| - Cadastrar coleta')#cadastra coleta
    print ('   |5| - Listar coleta') #lista coletas cadastrada
    print ('   |6| - Excluir coleta')# ecluir coleta cadastrada
    print ('   |7| - Sair\n') # fecha o aplicativo
    opt = input('Digite a opçao desejada: ').strip() # entrada de dados
    print('=+' * 20)
    return opt # retorna menu opçes
    
def adicionar_cliente():#adicionar cadastro cliente
    lcliente=[]
    cliente = str(input('Digite o nome do cliente: ')).strip()
    cliente=cliente.upper()
    lcliente.append(cliente) # adiciona cliente na lista
    f = open("cliente.txt", "a", encoding='utf-8') #w apaga a pode escrever
    
    f.write((cliente))
    f.close()

    if cliente in lcliente:
        print('Cadastro realizado com sucesso !', cliente, ' ',) #, end='|'
        # lcliente = cliente  implmentação quantidade clientes 
        # cliente=cliente + 1
    else:
                      
        print('Cliente com cadastrado') 
    #pass 

def remover_cliente():
    lcliente=[]
    # contatoEncontrado = False
    if(os.path.isfile('cliente.txt') == True):
        cliente = str(input('Digite o nome do cliente: ')).strip()
        cliente=cliente.upper() # retorna string para maiuscula
        
    with  open("cliente.txt", "r")as arquivo: #w apaga a pode escrever
        linhas = arquivo.readlines()

    with  open("cliente.txt", "w")as arquivo: # utlizado para escrever no arquivo
        for contato in linhas:
            lcliente.append(contato) # add contato
            lcliente = lcliente[0].split()
            if lcliente != cliente:
                print('Cliente Excluido')
                #arquivo.write(cliente)
            else:
                print('Cliente OK')
     
      
def listar_clientes():
    #lcliente=[] 
    f = open("cliente.txt", "r", encoding='utf-8') # não exibe lista de clientes
    clientes = f.readlines()
    for cliente in clientes:
        print(cliente , end='| \n')
    f.close()
    
def adicionar_coleta():
    lcliente=[]
    cliente = str(input("Digite o nome do cliente: "))
    cliente=cliente.upper()
    lcliente.append(cliente) # adiciona cliente na lista
    f = open("cliente.txt", "a", encoding='utf-8') #w apaga a pode escrever
    f.write((cliente))
    f.close()
           
    f = open("coleta.txt", "a", encoding='utf-8') #  retirei a e col w não exibe lista de clientes
    
    print ('Escolha a opção de tipo coleta:') 
    print ('   |1ª| - Papel') 
    print ('   |2ª| - Vidro') 
    print ('   |3ª| - Metal') 
    print ('   |4ª| - Orgânico')
    
    tcoleta=[]
    print ('Digite sua opção: 1 a 4')
    print()
    coleta = str(input('Digite o tipo de coleta: '))
    coleta=coleta.upper()
    tcoleta.append(coleta)
    f.close()   
    
    if coleta == '1':
        coleta = 'Papel' # intenção adicionar texto
        tcoleta.append(coleta) # falta inclementar 
        print('Opção de coleta registrada: ', coleta)
    
    elif coleta == '2':
        coleta ='Vidro' # intenção adicionar texto
        tcoleta.append(coleta)
        print('Opção de solicitação: registrada! ', coleta)
    
    elif coleta == '3':
        coleta='Metal' # intenção adicionar texto
        tcoleta.append(coleta)
        print('Opção de solicitação: registrada! ', coleta)
    
    elif coleta == '4':
        coleta='Metal' # intenção adicionar texto
        tcoleta.append(coleta)
        print('Opção de solicitação: registrada! ', coleta)
            
    else:
             
        print('Opção de solicitação: não registrada! ') 
    #pass 
    
    f = open("horacoleta.txt", "a", encoding='utf-8') # não exibe lista de clientes
    print ('Escolha o horário de atendimento!') 
    print ('   |1ª| - diurno') 
    print ('   |2ª| - Vespertino') 
    print ('   |3ª| - Noite') 
    
   
    pcoleta=[]  
    coleta = str(input("Digite o horário da coleta: "))
    coleta=coleta.upper()
    pcoleta.append(coleta)
    #f.write((pcoleta))
    # coleta = []
    if coleta == '1':
        coleta = 'Diurno' # intenção adicionar texto
        pcoleta.append(coleta)
        print('Horário registrado: ', coleta)
    
    elif coleta == '2':
        coleta ='Vespertino' # intenção adicionar texto
        pcoleta.append(coleta)
        print('Horário registrado: ', coleta)

    elif coleta == '3':
        coleta ='Noturno' # intenção adicionar texto
        pcoleta.append(coleta)
        print('Horário registrado:', coleta)
    else:
        print('Horário não registrado: ')

    f.close()

def listar_coleta():
    f = open("cliente.txt", "r", encoding='utf-8')
    for x in f:
        print('Cliente cadastrado:', x)
    
    f.close()
    f = open("coleta.txt", "r", encoding='utf-8')
    for x in f:
        print('Tipo de coleta cadastrada: ', x)
    
    f.close()
    f = open("horacoleta.txt", "r", encoding='utf-8')
    for x in f:
        print('Horário de coleta cadastrada: ', x)
 
    f.close()

    
def remover_coleta():
    lcliente=[]

    if(os.path.isfile('coleta.txt') == True):
            cliente = str(input('Digite o nome do cliente: '))
            cliente=cliente.upper()
            
            with  open("coleta.txt", "r")as arquivo: #w apaga a pode escrever
                linhas = arquivo.readlines()
            with  open("coleta.txt", "w")as arquivo:
             
                for arquivo in linhas:
                    lcliente.append(cliente)
                    lcliente = lcliente[0].split(';')
                    if lcliente != arquivo: #
                        print('Cliente Excluido')
                            
                    else:
                        print('Solicitação não executada')
            
        
opcao = menu() 
while opcao != '7': #ensera o aplicativo
    if opcao == '1': #adiciona cliente
        adicionar_cliente() 

    elif opcao == '2':  #remove cadastro cliente mas esta escrevendo também 
        remover_cliente() 
        
    elif opcao == '3': 
      
        listar_clientes() # exibe lista d e clientes cadastrado
        
        
    elif opcao == '4': # cadastra coleta
        adicionar_coleta()

    elif opcao == '5': # lista soicitações de coleta
        listar_coleta()
                        
    elif opcao == '6': # exclui coleta
        #cliente=input('Digite nome do cliente')
        #if cliente== cliente:
            remover_coleta()
    else:
        print('Cliente não encontradp')
               
    opcao = menu() 


