import multiprocessing
import string
import random
import time
from zeep import Client

import socket #usado para coordinacion y acuerdo

cuentaActiva=""
token = ""
############################## COORDINACION Y ACUERDO ###############################
### Se conecta con el banco B y envia el token
def     conexionAcuerdoSend(_mensaje):
    clientA = socket.socket()
    clientA.connect(('192.168.1.7',8000)) 
    print ("Enviando peticion...")    
    clientA.send(_mensaje.encode()) #envio de mensaje
    print ("Accedeiendo a la cuenta...")
    clientA.close()
  
    

### Espera mensajes del Banco C
def conexionAcuerdoRecv():     
    server = socket.socket()
    server.bind(('192.168.1.4',8000))
    server.listen()
        
    while True:        
        
        conexion, adrr = server.accept()
        
        print ("Nueva conexion establecida")
        print (adrr)
        
        mensaje = conexion.recv(1024).decode()              
        #print (mensaje)
        #desifra el token para obtener la cuenta
        cuenta = mensaje[8:15]
        msgTrue =mensaje[15:]
        print("Cuenta: " + cuenta)        
        print("CuentaActiva: " + cuentaActiva)        
        print("Token: " + token)
        print("TokenB: " + mensaje[0:15])
        print("MSGTrue: " + msgTrue)                                 
        #si la cuenta esta siendo usada en este banco

        if (msgTrue == 'True' and cuenta == cuentaActiva):
            time.sleep(2)
            print ("Cuenta usada en estos momentos...")
            client = socket.socket()
            client.connect(('192.168.1.7',8000))     
            #print ("msgTrue, Enviando mensaje...")
            client.send(token.encode()) #envia la cuenta             
            client.close()  
            #si la cuenta tiene permiso para acceder
            #      if (mensaje == token and cuenta == ''):
            
        print("Entrando por segunda vez al Banco A:")
        print("Este es el mensaje: "+mensaje)
        print("Este es token: "+token)
        print("Esta es la cuenta: "+cuenta)
        print("Este es la cuenta:  "+cuentaActiva)   
        if (mensaje == token and cuenta == cuentaActiva):
            print ('Hecho!!!')
            break   
            
        if (cuenta == cuentaActiva and token != mensaje[0:15]): #la cuenta esta siendo usada actualmente en este Banco
            #como esta en la seccion critica, tenemos que esperar a que termine su proceso
            time.sleep(2)
            client = socket.socket()
            client.connect(('192.168.1.7',8000))     
            #print ("Un usuario esta tratando de acceder a la cuenta...")
            tokenTrue = mensaje + 'True'
            client.send(tokenTrue.encode()) #envia la cuenta            
            #print ("cuenta==cuentaActiva") 
            client.close()  
             
        if(cuenta != cuentaActiva or cuentaActiva == ""): #la cuenta no es usada en este Banco
            time.sleep(2)
            client = socket.socket()
            client.connect(('192.168.1.7',8000))     
            #print ("pasando token...")
            client.send(mensaje.encode()) #envia la cuenta    
            
            client.close()
                                      
        
        conexion.close()
	   
        
#####################################################################################

########################## ESTABLECE CONEXION CON UN BANCO ##########################
def conexion(n_cuenta):
    remoteBank = None
    #Obtiene el banco al cual pertenece la cuenta
    banco = n_cuenta[0:1]
    
    if (banco == "A"):
        remoteBank =Client('http://192.168.1.4:1515/WS/Bank_A?wsdl')
    elif (banco == "B"):
        remoteBank =Client('http://192.168.1.7:1520/WS/Bank_B?wsdl')
    elif (banco == "C"):
        remoteBank =Client('http://192.168.1.8:1525/WS/Bank_C?wsdl')    

    return remoteBank    

#####################################################################################

############################### FUNCION PRINCIPAL ###############################
if __name__ == "__main__":                

    bancoA =Client('http://192.168.1.4:1515/WS/Bank_A?wsdl')

    print("\t\t############ BANCO A ############\n")
    #--------------MENU--------------
    
    while True:
        ### Ejecuta un nuevo proceso para recivir mensajes coordinacion y verificacion
        #thread = Thread(target=conexionAcuerdoRecv, args=())
        #thread.daemon = True        
        #thread.start()             
        cuentaActiva = ""
        token = ""

       
        #process = multiprocessing.Process(target=conexionAcuerdoRecv, args=())
        #process.start()
        #print (process.name)
        print("1.Crear Cuenta")
        print("2.Realizar una Transaccion")

        op = int(input())    

        if (op == 1): #Crear cuenta
            
            print("\nIngrese su nombre completo: ")        
            str = input()        
            bancoA.service.crearCuenta(str)                    
            #process.terminate()
            #process.join()
            #process.close()
            
            print("Creando numero de cuenta...")
            print("Numero de cuenta generada:...")

        elif (op == 2): #Ingresar al sistema            
            print("\nIngrese su numero de cuenta")            
            cuentaActiva = input()   
            #verifica si se esta usando o no la cuenta
            #print (process.name)
            if (cuentaActiva != None):
                #process.terminate()
                #process.join()
                #process.close() 
                #Generar numero aleatorio para usar junto a la cuenta como token                                
                token = '' .join(random.choice(string.ascii_letters + string.digits) for _ in range(8)) + cuentaActiva                
                print ("Token: " + token)
                #conexionAcuerdoSend(token)           
            
            #para cargar datos nuevos
            #process = multiprocessing.Process(target=conexionAcuerdoRecv, args=())
            #process.start()
            #process.join() #espera a que termine el proceso del hilo 
            

            print ("Se accedio correctamente...")            
            #print (process.name)
            #process.close()

            #enciendo otra ves el hilo
            #process = multiprocessing.Process(target=conexionAcuerdoRecv, args=())
            #process.start()
            #print (process.name)

            remoteBank = conexion(cuentaActiva) #Conexion remota con el banco A, B O C             
            menu_trans = True

            #en caso de que se ingrese una cuenta inexistente, no entra al menu trans
            if (remoteBank == None):
                menu_trans = True
            
            #time.sleep(1)
            while menu_trans:
                print("\tMENU DE TRANSACCIONES")
                print("\t---------------------")
                #-----------------MENU DE TRANSACCIONES------------------
                print("\t1.Deposito")			
                print("\t2.Retiro")
                print("\t3.Transferencia")
                print("\t4.Detalle")
                print("\t5.Salir")  
                op_trans = int(input())

                if op_trans == 1: #Deposito
                    print("\tMonto: ");	
                    remoteBank.service.deposito(cuentaActiva, input())
                elif op_trans == 2: #Retiro
                    print("\tMonto: ");	
                    remoteBank.service.retiro(cuentaActiva, input())
                elif op_trans == 3: #Transferencia
                    print("\tNumero de cuenta: ");
                    cuentaTrans=input()
                    remoteTrans = conexion(cuentaTrans)
                    if remoteTrans.service.activo(cuentaTrans) :
                            print("\tMonto: ");
                            monto=input()
                            remoteBank.service.retiro(cuentaActiva, monto)
                            remoteTrans.service.deposito(cuentaTrans,monto)
                    else :
                            print("espere que termine la transaccion pendiente")	
                elif op_trans == 4: #Detalle
                    print(remoteBank.service.detalle(cuentaActiva))
                elif op_trans == 5: #Salir                    
                    #print (process.name)                                                                                
                    #process.terminate()
                    #process.join()
                    #process.close()                    
                    menu_trans = False 
                    print ("Saliendo de la cuenta...")       
        elif op == 3:
            bancoA.service.listaUsuarios() 
            #process.terminate() 
            #process.join()
            #process.close()               
        

#####################################################################################