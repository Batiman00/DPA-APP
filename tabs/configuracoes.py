import customtkinter as ctk
from utils import ajustar_brilho

class ConfiguracoesTab(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=568, height=317, fg_color=["#152759","#064E3B"],corner_radius=0)
        self.grid_propagate(False)

        brilho_label = ctk.CTkLabel(self, text="Brilho da tela", font=("Poppins", 16, "bold"),width=100, text_color="white")
        brilho_label.grid(row=0, column=0, padx=20, pady=30)

        self.brilho_slider = ctk.CTkSlider(self, from_=0, to=100, number_of_steps=100,width=400 ,command=self.ajustar_brilho,progress_color=["#9EC9E0","#34D399"])
        self.brilho_slider.set(50)
        self.brilho_slider.grid(row=0, column=1, padx=20,pady=10)

        self.color_mode = ctk.CTkLabel(self, text="Modos", font=("Poppins", 16, "bold"),width=100)
        self.color_mode.grid(row=1, column=0, padx=20, pady=30)

        colors = ["AZUL", "VERDE"]
        self.options = ctk.CTkOptionMenu(self, values=colors, command=self.change_colors)
        self.options.grid(row=1, column=1, padx=20,pady=10)

    def ajustar_brilho(self, valor):
        ajustar_brilho(valor)

    def change_colors(self, choice):  
        print(choice)
        if choice == "AZUL":
            ctk.set_appearance_mode("light") 
        elif choice == "VERDE":
            ctk.set_appearance_mode("dark")