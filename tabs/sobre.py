import customtkinter as ctk
from utils import mostrar_dados_dispositivo, add_scrollable_frame

class SobreTab(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=568, height=317, fg_color=["#152759","#064E3B"])
        ctk.set_default_color_theme("blue-dpa.json")
        self.grid_propagate(False)

        # Adiciona o frame scrollável
        scrollable_frame = add_scrollable_frame(self, width=548, height=317)
        device_name = ctk.CTkLabel(scrollable_frame, text="Nome do dispositivo: ", font=("Poppins", 16,"bold"))
        device_name_label = ctk.CTkLabel(scrollable_frame, text="", font=("Poppins", 16))
        device_name.grid(row=0, column=0, pady=10)
        device_name_label.grid(row=0, column=1, pady=10)


        os = ctk.CTkLabel(scrollable_frame, text="Sistema operacional:", font=("Poppins", 16,"bold"))
        os_label = ctk.CTkLabel(scrollable_frame, text="", font=("Poppins", 16))
        os.grid(row=1, column=0, pady=10)
        os_label.grid(row=1, column=1, pady=10)

        # Versão do sistema operacional
        os_version = ctk.CTkLabel(scrollable_frame, text="Versão do SO:", font=("Poppins", 16, "bold"))
        os_version_label = ctk.CTkLabel(scrollable_frame, text="", font=("Poppins", 16))
        os_version.grid(row=2, column=0, pady=10)
        os_version_label.grid(row=2, column=1, pady=10)

        # Versão do Python
        python_version = ctk.CTkLabel(scrollable_frame, text="Versão do Python:", font=("Poppins", 16, "bold"))
        python_version_label = ctk.CTkLabel(scrollable_frame, text="", font=("Poppins", 16))
        python_version.grid(row=3, column=0, pady=10)
        python_version_label.grid(row=3, column=1, pady=10)

        # Arquitetura do sistema
        architecture = ctk.CTkLabel(scrollable_frame, text="Arquitetura:", font=("Poppins", 16, "bold"))
        architecture_label = ctk.CTkLabel(scrollable_frame, text="", font=("Poppins", 16))
        architecture.grid(row=4, column=0, pady=10)
        architecture_label.grid(row=4, column=1, pady=10)

        # Endereço IP
        ip_address = ctk.CTkLabel(scrollable_frame, text="Endereço IP:", font=("Poppins", 16, "bold"))
        ip_address_label = ctk.CTkLabel(scrollable_frame, text="", font=("Poppins", 16))
        ip_address.grid(row=5, column=0, pady=10)
        ip_address_label.grid(row=5, column=1, pady=10)



        # Nome do processador
        processor = ctk.CTkLabel(scrollable_frame, text="Processador:", font=("Poppins", 16, "bold"))
        processor_label = ctk.CTkLabel(scrollable_frame, text="", font=("Poppins", 16))
        processor.grid(row=7, column=0, pady=10)
        processor_label.grid(row=7, column=1, pady=10)

        # Memória RAM
        ram = ctk.CTkLabel(scrollable_frame, text="Memória RAM:", font=("Poppins", 16, "bold"))
        ram_label = ctk.CTkLabel(scrollable_frame, text="", font=("Poppins", 16))
        ram.grid(row=8, column=0, pady=10)
        ram_label.grid(row=8, column=1, pady=10)


        # Uptime
        uptime = ctk.CTkLabel(scrollable_frame, text="Tempo de atividade:", font=("Poppins", 16, "bold"))
        uptime_label = ctk.CTkLabel(scrollable_frame, text="", font=("Poppins", 16))
        uptime.grid(row=12, column=0, pady=10)
        uptime_label.grid(row=12, column=1, pady=10)

        # Uso de CPU
        cpu = ctk.CTkLabel(scrollable_frame, text="Uso de CPU:", font=("Poppins", 16, "bold"))
        cpu_label = ctk.CTkLabel(scrollable_frame, text="", font=("Poppins", 16))
        cpu.grid(row=13, column=0, pady=10)
        cpu_label.grid(row=13, column=1, pady=10)

        # Uso de Memória
        memory = ctk.CTkLabel(scrollable_frame, text="Uso de Memória:", font=("Poppins", 16, "bold"))
        memory_label = ctk.CTkLabel(scrollable_frame, text="", font=("Poppins", 16))
        memory.grid(row=14, column=0, pady=10)
        memory_label.grid(row=14, column=1, pady=10)

        # Uso de Disco
        disk = ctk.CTkLabel(scrollable_frame, text="Uso de Disco:", font=("Poppins", 16, "bold"))
        disk_label = ctk.CTkLabel(scrollable_frame, text="", font=("Poppins", 16))
        disk.grid(row=15, column=0, pady=10)
        disk_label.grid(row=15, column=1, pady=10)

        mostrar_dados_dispositivo(scrollable_frame)
