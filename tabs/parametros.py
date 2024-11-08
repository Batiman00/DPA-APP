import customtkinter as ctk
from widgets import add_plus_minus_buttom
from utils import enviar_dados_serial

class ParametrosTab(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=584, height=317, fg_color="#152759",corner_radius=0)
        self.grid_propagate(False)

        param_row1 = ctk.CTkFrame(self, border_width=1, fg_color="#152759")
        param_row1.grid(row=0, column=0, pady=8,padx=(12,12))
        param_row2 = ctk.CTkFrame(self,border_width=1,fg_color="#152759")
        param_row2.grid(row=1, column=0, padx=(12,12),pady=8) 
        param_row3 = ctk.CTkFrame(self,border_width=1,fg_color="#152759")
        param_row3.grid(row=2, column=0, padx=(12,12),pady=8)
        # Volume total
        self.volume_total = 1.0
        volume_label = ctk.CTkLabel(param_row1,text="Volume total", font=("Poppins", 16,"bold"), width=210, height=56)
        volume_label.grid(row=0, column=0,padx=(4, 0),pady=1)

        self.volume_value_label = ctk.CTkLabel(param_row1, text=f"{self.volume_total:.2f} Litro(s)", font=("Poppins", 18, "bold"), width=190,height=56, text_color="#152759", bg_color="white")
        self.volume_value_label.grid(row=0, column=1,pady=1)

        self.volume_button = add_plus_minus_buttom(param_row1,self.aumentar_volume,self.diminuir_volume,2)
        self.volume_button.grid(row=0,column=2,pady=2, padx=2)

        # Tempo
        self.hour = 1
        self.minutes = 0
        time_label = ctk.CTkLabel(param_row2, text="Tempo", font=("Poppins", 16, "bold"), width=210, height=56)
        time_label.grid(row=1, column=0,padx=(4, 0), pady=1)

        self.time_value_label = ctk.CTkLabel(param_row2, text=f"{self.hour}h e {self.minutes} min", font=("Poppins", 18, "bold"),width=190,height=56, text_color="#152759", bg_color="white")
        self.time_value_label.grid(row=1, column=1)

        time_button = add_plus_minus_buttom(param_row2, self.aumentar_tempo, self.diminuir_tempo,2)
        time_button.grid(row=1, column=2, pady=2,padx=2)

         # Residual
        self.residual = 0
        residual_label = ctk.CTkLabel(param_row3, text="Residual", font=("Poppins", 16, "bold"), width=210, height=56)
        residual_label.grid(row=1, column=0,padx=(4, 0), pady=1)

        self.residual_value_label = ctk.CTkLabel(param_row3, text=f"{self.residual} mL", font=("Poppins", 18, "bold"),width=190,height=56, text_color="#152759", bg_color="white")
        self.residual_value_label.grid(row=1, column=1)

        residual_button = add_plus_minus_buttom(param_row3, self.aumentar_residual, self.diminuir_residual,2)
        residual_button.grid(row=1, column=2, pady=2,padx=2)

        send_data_button = ctk.CTkButton(self, text="Enviar dados", font=("Poppins", 16, "bold"), width=150, height=45, fg_color="#468C2D",corner_radius=16, command=self.enviar_dados_button_click)
        send_data_button.grid(row=3, column=0,sticky="e",padx=(0,16),pady=(40,0))

    def aumentar_volume(self):
        if self.volume_total < 10:
            self.volume_total += 0.25
            self.volume_value_label.configure(text=f"{self.volume_total:.2f} Litro(s)")

    def diminuir_volume(self):
        if self.volume_total > 0.5:
            self.volume_total -= 0.25
            self.volume_value_label.configure(text=f"{self.volume_total:.2f} Litro(s)")

    def aumentar_tempo(self):
        if self.hour < 10:
            if self.minutes == 30:
                self.hour += 1
                self.minutes = 0
            else:
                self.minutes  += 30
            self.time_value_label.configure(text=f"{self.hour}h e {self.minutes} min")
        
    def diminuir_tempo(self):
        if self.hour >= 1:
            if self.minutes == 30:
                self.minutes = 0
            else:
                self.hour -= 1
                self.minutes = 30
            self.time_value_label.configure(text=f"{self.hour}h e {self.minutes} min")

    def aumentar_residual(self):
        if self.residual < self.volume_total*1000:
            self.residual += 100
            self.residual_value_label.configure(text=f"{self.residual} mL")

    def diminuir_residual(self):
        if self.residual > 0:
            self.residual -= 100
            self.residual_value_label.configure(text=f"{self.residual} mL")

    def enviar_dados_button_click(self):
        time = self.hour + self.minutes == 30 if 0.5 else 0
        enviar_dados_serial(self.volume_total, time, self.residual)