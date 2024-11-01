import customtkinter as ctk
from utils import send_data

class ParametrosTab(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=568, height=317, fg_color=["#152759","#064E3B"],corner_radius=0)
        self.grid_propagate(False)

        param_row1 = ctk.CTkFrame(self, border_width=1, fg_color="#ffffff",corner_radius=0)
        param_row1.grid(row=0, column=0, pady=8,padx=(12,12))
        # Volume total
        self.volume_total = 1.0
        volume_label = ctk.CTkLabel(param_row1,text="Volume total", font=("Poppins", 30,"bold"), width=538, text_color=["#152759","#064E3B"])
        volume_label.grid(row=0,pady=(12,0))

        self.volume_value_label = ctk.CTkLabel(param_row1, text=f"{self.volume_total:.2f} Litro(s)", font=("Poppins", 28, "bold"), width=190,height=55, text_color="#ffffff", bg_color=["#152759","#064E3B"])
        self.volume_value_label.grid(row=1,pady=(20,32))

        buttom_width=86
        buttom_height=72
        buttom_frame = ctk.CTkFrame(param_row1, fg_color="#ffffff")
        buttom_frame.grid(row=2, pady=(0,20))
        increase_button = ctk.CTkButton(buttom_frame, text="+0.1L", width=buttom_width, height=buttom_height, command=lambda: self.controlar_volume(0.1), fg_color="#D9D9D9",text_color="black", font=("Poppins", 20,"bold"), border_color=["#152759","#064E3B"], border_width=2)
        increase_button.grid(row=0, column=0, padx=(0,10))    
        decrease_button = ctk.CTkButton(buttom_frame, text="+0.5L", width=buttom_width, height=buttom_height, command=lambda: self.controlar_volume(0.5), fg_color="#D9D9D9",text_color="black", font=("Poppins", 20,"bold"), border_color=["#152759","#064E3B"], border_width=2)
        decrease_button.grid(row=0, column=1,padx=32)
        increase_button = ctk.CTkButton(buttom_frame, text="-0.1L", width=buttom_width, height=buttom_height, command=lambda: self.controlar_volume(0.1,False), fg_color="#D9D9D9",text_color="black", font=("Poppins", 20,"bold"), border_color=["#152759","#064E3B"], border_width=2)
        increase_button.grid(row=0, column=2)    
        decrease_button = ctk.CTkButton(buttom_frame, text="-0.5L", width=buttom_width, height=buttom_height, command=lambda: self.controlar_volume(0.5,False), fg_color="#D9D9D9",text_color="black", font=("Poppins", 20,"bold"), border_color=["#152759","#064E3B"], border_width=2)
        decrease_button.grid(row=0, column=3,padx=(32,0))

        send_data_button = ctk.CTkButton(self, text="Enviar dados", font=("Poppins", 16, "bold"), width=150, height=40, fg_color="#468C2D",corner_radius=16, command=send_data)
        send_data_button.grid(row=2,sticky="e",padx=(12,16),pady=(2,0))


    def controlar_volume(self, offset, add=True):
        if add:
            result = min(5, round(self.volume_total + offset,2))
        else:
            result = max(0.5, round(self.volume_total - offset,2))
        self.volume_total = result
        self.volume_value_label.configure(text=f"{self.volume_total:.2f} Litro(s)")

