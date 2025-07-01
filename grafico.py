import serial
import matplotlib.pyplot as plt

# Configura a porta e velocidade da serial
porta = 'COM3'  # Altere para a porta correta (ex: /dev/ttyUSB0 no Linux/Mac)
baudrate = 9600
ser = serial.Serial(porta, baudrate, timeout=1)

# Armazena os dados recebidos
angulos = []
intensidades = []

print("Coletando dados...")

# Loop de leitura (10 ciclos, com 12 medidas por ciclo = 120 leituras)
while len(angulos) < 120:
    try:
        linha = ser.readline().decode('utf-8').strip()
        if ',' in linha:
            partes = linha.split(',')
            angulo = int(partes[0])
            intensidade = int(partes[1])
            angulos.append(angulo)
            intensidades.append(intensidade)
            print(f"Ângulo: {angulo}, Intensidade: {intensidade}")
    except Exception as e:
        print("Erro:", e)

ser.close()

# Plotagem
plt.figure(figsize=(10,5))
plt.plot(angulos, intensidades, 'o-', label='Intensidade de luz')
plt.xlabel('Ângulo (°)')
plt.ylabel('Intensidade (ADC)')
plt.title('Distribuição de Intensidade por Ângulo')
plt.grid(True)
plt.legend()
plt.show()
