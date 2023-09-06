import subprocess
import RPi.GPIO as GPIO
import time
import mysql.connector
from mysql.connector import Error

senha = "111111"
id_senha = 0

def conectar():
    try :
        global con
        con = mysql.connector.connect(host='localhost', database = 'mysql', user = 'root', password = '197328')
    except Error as erro:
        print("Erro de conexao")

try:
    conectar()
    consulta_sql = 'select * from password_access'
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    senha = linhas[len(linhas)-1][1]
    id_senha = linhas[len(linhas)-1][0]
    cursor.close()
except Error as e:
    print("Erro ao acessar tabela ", e)
finally:
    if (con.is_connected()):
        con.close()
        cursor.close()
        print("Conexao encerrada")

print(senha)
print(id_senha)

# Definição dos pinos de coluna e linha
coluna1 = 13
coluna2 = 6
coluna3 = 26
coluna4 = 19
linha1 = 5

# Pino de controle da tranca
tranca = 18

# Definição dos pinos de controle do motor
StepPins = [23, 24, 25, 18]

#Buzzer Pins
buzzer = 7 

# Define simple sequence
StepCount = 4
Seq = []
Seq = [i for i in range(0, StepCount)]
Seq[0] = [1,0,0,0]
Seq[1] = [0,1,0,0]
Seq[2] = [0,0,1,0]
Seq[3] = [0,0,0,1]

# Configuração dos pinos como saída
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(coluna1, GPIO.OUT)
GPIO.setup(coluna2, GPIO.OUT)
GPIO.setup(coluna3, GPIO.OUT)
GPIO.setup(coluna4, GPIO.OUT)
GPIO.setup(tranca, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)

# Set all pins as output
for pin in StepPins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, False)

# Define some settings
WaitTime = 0.005

# Configuração da linha como entrada
GPIO.setup(linha1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Matriz de teclado
teclado = [[1, 2, 3, 4],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]

# Variável para armazenar a senha digitada
senha_digitada = ""

def take_photo():
    subprocess.call("./pic_command.sh")

def ativar_tranca():
    GPIO.output(tranca, GPIO.HIGH)
    print("Tranca ativada")
    time.sleep(1)
    GPIO.output(tranca, GPIO.LOW)

GPIO.output(tranca, GPIO.LOW)

def acionar_motor(nb):
        StepCounter = 0
        if nb<0: sign=-1
        else: sign=1
        nb=sign*nb*2 #times 2 because half-step
        print("nbsteps {} and sign {}".format(nb,sign))
        for i in range(nb):
                for pin in range(4):
                        xpin = StepPins[pin]
                        if Seq[StepCounter][pin]!=0:
                                GPIO.output(xpin, True)
                        else:
                                GPIO.output(xpin, False)
                StepCounter += sign
        # If we reach the end of the sequence
        # start again
                if (StepCounter==StepCount):
                        StepCounter = 0
                if (StepCounter<0):
                        StepCounter = StepCount-1
                # Wait before moving on
                time.sleep(WaitTime)

nbStepsPerRev=512

def ativar_buzzer():
    for i in range(3):
        GPIO.output(buzzer, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(buzzer, GPIO.LOW)
        time.sleep(0.5)
        
# Loop infinito para leitura do teclado
while True:
    for coluna in range(4):
        # Define coluna atual como saída e as outras como entrada
        if coluna == 0:
            GPIO.output(coluna1, False)
            GPIO.output(coluna2, True)
            GPIO.output(coluna3, True)
            GPIO.output(coluna4, True)
        elif coluna == 1:
            GPIO.output(coluna1, True)
            GPIO.output(coluna2, False)
            GPIO.output(coluna3, True)
            GPIO.output(coluna4, True)
        elif coluna == 2:
            GPIO.output(coluna1, True)
            GPIO.output(coluna2, True)
            GPIO.output(coluna3, False)
            GPIO.output(coluna4, True)
        elif coluna == 3:
            GPIO.output(coluna1, True)
            GPIO.output(coluna2, True)
            GPIO.output(coluna3, True)
            GPIO.output(coluna4, False)

        # Verifica se a linha está ativa
        if GPIO.input(linha1) == False:
            tecla_pressionada = teclado[0][coluna]
            senha_digitada += str(tecla_pressionada)
            print("Tecla pressionada:", tecla_pressionada)
            time.sleep(0.2)
            if len(senha_digitada) == 6:
                if senha_digitada == senha:
                    print("Senha correta")
                    take_photo()
                    ativar_tranca()
                    acionar_motor(nbStepsPerRev)
                    time.sleep(0.2);
                    acionar_motor(-nbStepsPerRev)
                    
                    try:
                        conectar()
                        atualiza_foto = """UPDATE password_access 
                        SET fotos_tentativas = '/home/lock/Desktop/Camera/cam_pic.jpg', ultimo_acesso = now()
                        WHERE id = """ + str(id_senha)
                        cursor = con.cursor()
                        cursor.execute(atualiza_foto)
                        con.commit()
                    except Error as e:
                        print("Erro de conexao att")
                    finally:
                        if (con.is_connected()):
                            con.close()
                            cursor.close()
                            print("Conexao encerrada att")

                else:
                    print("Senha incorreta")
                    ativar_buzzer()
                senha_digitada = ""

# Limpeza dos pinos
GPIO.cleanup()