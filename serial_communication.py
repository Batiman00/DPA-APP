import serial

class SerialCommunication:
    def __init__(self, porta_serial, baudrate=115200):
        """
        Inicializa a comunicação serial e configura a porta e taxa de transmissão.

        Args:
            porta_serial (str): Porta serial para comunicação.
            baudrate (int): Taxa de transmissão.
        """
        self.porta_serial = porta_serial
        self.baudrate = baudrate
        self.is_connected = False
        self.ser = None

    def connect(self):
        """
        Estabelece a conexão com a porta serial, se não estiver conectada.
        """
        if not self.is_connected:
            try:
                self.ser = serial.Serial(self.porta_serial, self.baudrate, timeout=1)
                self.is_connected = True
                print(f"Conexão estabelecida com {self.porta_serial}.")
            except serial.SerialException as e:
                print(f"Erro ao conectar na porta serial: {e}")
                self.is_connected = False

    def disconnect(self):
        """
        Desconecta da porta serial.
        """
        if self.is_connected:
            self.ser.close()
            self.is_connected = False
            print(f"Desconectado da porta serial {self.porta_serial}.")

    def enviar_dados(self, volume_infundido, tempo, volume_drenado):
        """
        Envia os dados pela porta serial apenas se a conexão estiver ativa.
        
        Args:
            volume_infundido (int): Valor do volume infundido em ml.
            tempo (int): Valor do tempo em segundos.
            volume_drenado (int): Valor do volume drenado em ml.
        """
        if self.is_connected:
            try:
                dados = f"({volume_infundido},{tempo},{volume_drenado})"
                self.ser.write(dados.encode())  # Envia os dados pela porta serial
                print(f"Dados enviados: {dados}")
            except Exception as e:
                print(f"Erro ao enviar dados: {e}")
                self.is_connected = False
                self.disconnect()

    def receber_dados(self):
        """
        Lê os dados pela porta serial, se a conexão estiver ativa.

        Returns:
            tuple: Uma tupla contendo volume_infundido, volume_total, tempo_faltante, ou None se não houver dados.
        """
        if self.is_connected:
            try:
                if self.ser.in_waiting > 0:
                    linha = self.ser.readline().decode().strip()
                    if linha.startswith("(") and linha.endswith(")"):
                        volume_infundido, volume_total, tempo_faltante = map(int, linha[1:-1].split(","))
                        return volume_infundido, volume_total, tempo_faltante
            except serial.SerialException as e:
                print(f"Erro ao ler dados da porta serial: {e}")
                self.is_connected = False
                self.disconnect()
        return None

    def is_connected(self):
        return self.is_connected
