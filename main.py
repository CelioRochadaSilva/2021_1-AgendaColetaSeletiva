#inicio

cliente=0 
coleta=0
tcoleta=0
pcoleta=0
#lcoleta=0
#salvar_diario=0 

ldiario=[cliente,tcoleta,pcoleta]
print('=+' * 20)
print('Sejam Bem vindo(a)!')
print('Coleta seletiva Pessoa Fisica!')

def menu (): 
    print ('Escolha uma opção de 1 a 7 \n') 
    print ('   1 - Cadastrar cliente') # opção de cadastro para cliente com a função adicionar_cadastro
    print ('   2 - Remover cliente') # remove cliente cadastrado com função remover_cadastro
    print ('   3 - Listar cliente') # lista clientes cadastrado na lista
    print ('   4 - Cadastrar coleta')
    print ('   5 - Listar coleta')
    print ('   6 - Excluir coleta')
    print ('   7 - Sair\n') # fecha o aplicativo
    opt = input('Digite a opçao desejada: utf8') # entrada de dados
    print('=+' * 20)
    return opt 
def adicionar_cliente():
    lcliente=[]
    cliente = str(input("Digite o nome do cliente:"))
    cliente=cliente.upper()
    lcliente.append(cliente) # adiciona cliente na lista
    f = open("cliente.txt", "a") #w apaga a pode escrever
    # print(f.read())
    # print(f.readline())
    # print(f.readline())
    f.write((cliente))
    f.close()

    if cliente in lcliente:
        print('Cadastro realizado', cliente)
    else:
                      
        print('Cliente com cadastrado') 
    pass 

def remover_cliente():
    lcliente=[]
    cliente=str(input("Digite o nome do cliente:"))
    cliente=cliente.upper()
    f = open("cliente.txt", "w") #w apaga a pode escrever
    # print(f.read())
    #print(cliente.readline())
    # print(f.readline())
    f.write((cliente))
    f.close()
    
    if cliente in lcliente:
        print('Cliente Removido',cliente)
    else:
        print('Esse cliente não está cadastrado') 
    pass 

def listar_clientes():
    #lcliente=[] 
    f = open("cliente.txt", "r") # não exibe lista de clientes
   
    #print(f.readlines())
    clientes = f.readlines()
    for cliente in clientes:
        print(cliente)
    f.close()
    # for contato in clientes:
    #     clientes.append(contato)
    #     lista = lista[0].split(';')
    # if (lista[0] == listar_clientes):
   
    
def adicionar_coleta():
    tcoleta=[]
    f = open("coleta.txt", "a") # não exibe lista de clientes
    
    print ('Escolha a opção de tipo coleta:') 
    print ('   1 - Papel') 
    print ('   2 - Vidro') 
    print ('   3 - Metal') 
    print ('   4 - Orgânico')

    coleta = str(input("Digite o tipo de coleta:"))
    coleta=coleta.upper()
    tcoleta.append(coleta)
    #print(f.readline())
    #clientes = f.readlines()
    f.write((coleta))
    f.close()   
    
    if coleta == '1':
        coleta='Papel' # intenção adicionar texto
        tcoleta.append(coleta) # falta inclementar 
        #print('Opção de solicitação registrada', tcoleta)
    
    elif coleta == '2':
        coleta='Vidro' # intenção adicionar texto
        tcoleta.append(coleta)
        print('Opção de solicitação de coleta registrada')
    
    elif coleta == '3':
        coleta='Metal' # intenção adicionar texto
        tcoleta.append(coleta)
        print('Opção de solicitação de coleta registrada')
    
    elif coleta == '4':
        coleta='Metal' # intenção adicionar texto
        tcoleta.append(coleta)
        print('Atualização registrada')
            
    else:
             
        print('atualização de coleta não registrada') 
    pass 
    
    print ('Escolha o horário de atendimento!') 
    print ('   1 - diurno') 
    print ('   2 - Vespertino') 
    print ('   3 - Noite') 
    
    f = open("coleta.txt", "a") # não exibe lista de clientes

    pcoleta=[]  
    pcoleta = str(input("Digite o horário da coleta:"))
    pcoleta=pcoleta.upper()
    tcoleta.append(pcoleta)
    f.write((pcoleta))
    
    if pcoleta == '1':
        pcoleta='Diurno' # intenção adicionar texto
        tcoleta.append(pcoleta) # error
        print('Orário registrada')
    
    if pcoleta == '2':
        pcoleta='Vespertino' # intenção adicionar texto
        tcoleta.append(pcoleta)
        print('Orário registrada')

    if pcoleta == '3':
        pcoleta='Noturno' # intenção adicionar texto
        tcoleta.append(pcoleta)
        print('Orário registrada')
    

def listar_coleta():
    print('Coleta cadastrado para: ',cliente, '\no tipo de coleta e hprario são: ') #exibi cliente solicitou coleta , tipo e horário
     


def remover_coleta():
    pass

#def atualizar_coleta():
 
def hora_coleta():

    print('Orário registrada', pcoleta) #esse
    pass 

def verificar_situacao():
    lcliente=[]
    cliente = str(input("Digite as novas informações sobre o cliente: "))
    cliente=cliente.upper()
    lcliente.append(cliente) # adiciona cliente na lista
    if cliente in lcliente:
        lcliente.remove(cliente)
        print('Alteração realizada com sucesso')
    else:
        print('Cadastro não alterado') 
    pass 
     
   
def le_diario ():
    ldiario=[]
    print(ldiario) 
    pass  


opcao = menu() 
while opcao != '7': #ensera o aplicativo
    if opcao == '1': #adiciona cliente
        adicionar_cliente() 
    elif opcao == '2':  #remove cadastro cliente
        remover_cliente() 
        
    elif opcao == '3': # exiber informações cliente, coleta e horario coleta
        listar_clientes()
        # print('clientes cadastrado:',lcliente)
        
    elif opcao == '4': # cadastra coleta
        adicionar_coleta()

    elif opcao == '5': # lista soicitações de coleta
        
        listar_coleta()
        
    if opcao == '6': # exclui coleta
        remover_coleta()
    
           
    opcao = menu() 

