import tkinter as tk
import customtkinter as ctk
import socket
import time
import psutil
import platform
import traceback
from datetime import datetime
import screen_brightness_control as sbc

# Função para exibir a caixa de erro
def show_error(message):
    tk.messagebox.showerror("Erro", message)

# Função que pode gerar um erro (exemplo)
def send_data():
    try:
        result = 10 / 0
    except Exception as e:
        error_message = f"Ocorreu um erro: {str(e)}\n\nDetalhes: {traceback.format_exc()}"
        show_error(error_message)

# Função para obter o nome do dispositivo
def get_device_name():
    return socket.gethostname()

# Função para obter o sistema operacional e versão
def get_os_info():
    os_name = platform.system()
    os_version = platform.version()
    return f"{os_name} {os_version}"

# Função para obter a versão do Python
def get_python_version():
    return platform.python_version()

# Função para obter o endereço IP
def get_ip_address():
    try:
        ip = socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        ip = "Não disponível"
    return ip

# Função para obter o tempo de atividade do dispositivo
def get_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_str = time.strftime('%H:%M:%S', time.gmtime(uptime_seconds))
    return uptime_str

# Função para obter o uso de CPU
def get_cpu_usage():
    return f"{psutil.cpu_percent()}%"


def get_disk_usage():
    return psutil.disk_usage('/').percent

# Função para obter o uso de memória
def get_memory_info():
    memory = psutil.virtual_memory()
    return f"{memory.percent}%"

# Função para obter informações de espaço em disco
def get_disk_info():
    disk = psutil.disk_usage('/')
    return f"{disk.percent}% usado de {disk.total // (2**30)}GB"

def get_memory_usage():
    return psutil.virtual_memory().percent

# Função para obter a quantidade de RAM
def get_ram_info():
    ram = psutil.virtual_memory()
    return f"{ram.total / (1024 ** 3):.2f} GB"

# Função para ajustar o formato de hora manualmente
def ajustar_hora(hora_entry, ajustar_hora_status):
    nova_hora = hora_entry.get()  # Pega o valor inserido pelo usuário
    try:
        datetime.strptime(nova_hora, '%H:%M')  # Verifica se o formato é HH:MM
        os.system(f'sudo date +%T -s "{nova_hora}:00"')  # Ajusta a hora no Raspberry Pi
        ajustar_hora_status.configure(text="Hora ajustada com sucesso", text_color="green")
    except ValueError:
        ajustar_hora_status.configure(text="Formato inválido. Use HH:MM", text_color="red")

def ajustar_brilho(valor):
    global brilho_valor
    brilho_valor = int(valor)
    try:
        sbc.set_brightness(brilho_valor)
    except Exception as e:
        print(f"Erro ao ajustar o brilho: {e}")

def mostrar_dados_dispositivo(scrollable_frame):
    """
    Exibe informações sobre o dispositivo na seção 'Sobre' em um frame rolável.

    Parâmetros:
    scrollable_frame (tk.Frame): O frame rolável onde as informações do dispositivo serão exibidas.
    """
    # Obtém informações do dispositivo
    device_name = socket.gethostname()
    os_name = platform.system() 
    os_version = platform.release()
    python_version = platform.python_version()
    architecture = platform.architecture()[0]
    ip_address = get_ip_address()
    uptime = get_uptime()
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    processor = platform.processor()
    ram = get_ram_info()

    
    # Dicionário de informações para exibir
    dados_dispositivo = {
        "Nome do dispositivo": device_name,
        "Sistema operacional": os_name,
        "Versão do SO": os_version,
        "Versão do Python": python_version,
        "Arquitetura": architecture,
        "Endereço IP": ip_address,
        "Processador": processor,
        "Memória RAM": ram,
        "Tempo de atividade": uptime,
        "Uso de CPU": cpu_usage,
        "Uso de Memória": memory_usage,
        "Uso de Disco": disk_usage,
    }

    # Limpa o conteúdo existente do frame
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    # Adiciona as informações como labels no frame
    for i, (chave, valor) in enumerate(dados_dispositivo.items()):
        label_chave = ctk.CTkLabel(scrollable_frame, text=f"{chave}: ", font=('Poppins', 16, 'bold'), width=230, anchor='w', text_color=["white","white"])
        label_chave.grid(row=i, column=0, padx=10, pady=8, sticky='w')

        label_valor = ctk.CTkLabel(scrollable_frame, text=valor, font=('Poppins', 16),width=284, wraplength=284,anchor='w', text_color=["white","white"])
        label_valor.grid(row=i, column=1, padx=10, pady=8, sticky='w')

def add_scrollable_frame(parent_frame, width, height):
    canvas = tk.Canvas(parent_frame, width=width, height=height, borderwidth=0)
    scrollbar = ctk.CTkScrollbar(parent_frame, orientation="vertical", command=canvas.yview)
    scrollable_frame = ctk.CTkFrame(canvas, width=width, fg_color=["#152759","#064E3B"])
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.grid(row=0, column=0)
    scrollbar.grid(row=0, column=1, sticky="ns")
    return scrollable_frame



