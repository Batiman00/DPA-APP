import sys
sys.dont_write_bytecode = True
import customtkinter as ctk
from tabs.parametros import ParametrosTab
from tabs.configuracoes import ConfiguracoesTab
from tabs.sobre import SobreTab
from tabs.monitoramento import MonitoramentoTab
import time
from PIL import Image

# Configuração inicial da janela
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue-dpa.json")

param_light_icon = ctk.CTkImage(light_image=Image.open('images/param_light.png'))
param_icon = ctk.CTkImage(light_image=Image.open('images/param.png'))
setting_light_icon = ctk.CTkImage(light_image=Image.open('images/settings_light.png'))
setting_icon = ctk.CTkImage(light_image=Image.open('images/settings.png'))
info_light_icon = ctk.CTkImage(light_image=Image.open('images/info_light.png'))
info_icon = ctk.CTkImage(light_image=Image.open('images/info.png'))

def atualizar_hora():
    hora_atual = time.strftime('%H:%M')
    hora_label.configure(text=hora_atual)
    root.after(1000, atualizar_hora) 

def mostrar_frame(frame, aba):
    frame.tkraise()
    if aba == "parametros":
        parametros_button.configure(fg_color=["#152759","#064E3B"], image=(param_light_icon),text_color="white",background_corner_colors=[["#9EC9E0","#34D399"], '#152759','#152759', ["#9EC9E0","#34D399"]])  # Aba selecionada
        monitoramento_button.configure(fg_color=["#9EC9E0","#34D399"],image=info_icon, text_color=["#282828","#000000"])  # Aba não selecionada
        configuracoes_button.configure(fg_color=["#9EC9E0","#34D399"],image=setting_icon, text_color=["#282828","#000000"])  # Aba não selecionada
        sobre_button.configure(fg_color=["#9EC9E0","#34D399"],image=info_icon, text_color=["#282828","#000000"])  # Aba não selecionada
    elif aba == "monitoramento":
        parametros_button.configure(fg_color=["#9EC9E0","#34D399"], image=param_icon,text_color=["#282828","#000000"])
        monitoramento_button.configure(fg_color=["#152759","#064E3B"],image=info_icon, text_color="white")  # Aba não selecionada
        configuracoes_button.configure(fg_color=["#9EC9E0","#34D399"],image=setting_light_icon, text_color=["#282828","#000000"])
        sobre_button.configure(fg_color=["#9EC9E0","#34D399"],image=info_icon, text_color=["#282828","#000000"])
    elif aba == "configuracoes":
        parametros_button.configure(fg_color=["#9EC9E0","#34D399"], image=param_icon,text_color=["#282828","#000000"])
        monitoramento_button.configure(fg_color=["#9EC9E0","#34D399"],image=info_icon, text_color=["#282828","#000000"])  # Aba não selecionada
        configuracoes_button.configure(fg_color=["#152759","#064E3B"],image=setting_light_icon, text_color="white")
        sobre_button.configure(fg_color=["#9EC9E0","#34D399"],image=info_icon, text_color=["#282828","#000000"])
    elif aba == "sobre":
        parametros_button.configure(fg_color=["#9EC9E0","#34D399"],image=param_icon, text_color=["#282828","#000000"])
        monitoramento_button.configure(fg_color=["#9EC9E0","#34D399"],image=info_icon, text_color=["#282828","#000000"])  # Aba não selecionada
        configuracoes_button.configure(fg_color=["#9EC9E0","#34D399"],image=setting_icon, text_color=["#282828","#000000"])
        sobre_button.configure(fg_color=["#152759","#064E3B"],image=info_light_icon, text_color="white")

# Criação da janela principal
root = ctk.CTk()
root.title("PERITONE.AI")
root.geometry("800x400")
root.iconbitmap("./images/icon.ico")
root.wm_attributes("-fullscreen",True)

# Título principal e hora
title_frame = ctk.CTkFrame(root)
title_frame.grid(row=0, column=0, columnspan=3, pady=10, padx=10, sticky="ew")

title_label = ctk.CTkLabel(title_frame, text="PERITONE.AI", font=("Poppins", 28, "bold", "italic"),text_color=["#282828","#000000"])
title_label.grid(row=0, column=0, padx=(35, 0))

hora_label = ctk.CTkLabel(title_frame, text="", font=("Poppins", 16, "bold"), anchor="s",text_color=["#282828","#000000"])
hora_label.grid(row=0, column=1, padx=(500, 0),sticky="e")
atualizar_hora()

# Frame para as abas (simulação de tabview vertical)
tab_frame = ctk.CTkFrame(root, width=150, height=300)
tab_frame.grid(row=1, column=0, sticky="wsen")

# Parâmetros - Frame principal
param_frame = ParametrosTab(root)
param_frame.grid(row=1, column=1)

# Monitoramento - Frame
monitoramento_frame = MonitoramentoTab(root)
monitoramento_frame.grid(row=1, column=1)

# Configurações - Frame
config_frame = ConfiguracoesTab(root)
config_frame.grid(row=1, column=1)

# Sobre - Frame
sobre_frame = SobreTab(root)
sobre_frame.grid(row=1, column=1)

# Botões que simulam as abas
parametros_button = ctk.CTkButton(tab_frame,anchor='w', text="Parâmetros", width=180, height=40, font=("Poppins", 16, "bold"),
                                  command=lambda: mostrar_frame(param_frame, "parametros"), 
                                  fg_color=["#152759","#064E3B"], text_color="black",background_corner_colors=[["#9EC9E0","#34D399"], ["#152759","#064E3B"],["#152759","#064E3B"], ["#9EC9E0","#34D399"]], border_width=2)  # Inicialmente selecionado
parametros_button.grid(row=0, column=0, padx=(30, 0), sticky="w")

monitoramento_button = ctk.CTkButton(tab_frame,anchor='w', text="Monitoramento", width=180, height=40, font=("Poppins", 16, "bold"),
                                  command=lambda: mostrar_frame(monitoramento_frame, "monitoramento"), 
                                  fg_color=["#152759","#064E3B"], text_color="black",background_corner_colors=[["#9EC9E0","#34D399"], ["#152759","#064E3B"],["#152759","#064E3B"], ["#9EC9E0","#34D399"]], border_width=2)  # Inicialmente selecionado
monitoramento_button.grid(row=1, column=0, padx=(30, 0), sticky="w")

configuracoes_button = ctk.CTkButton(tab_frame,anchor='w', text="Configurações", width=180, height=40, font=("Poppins", 16, "bold"),
                                     command=lambda: mostrar_frame(config_frame, "configuracoes"), 
                                     fg_color=["#9EC9E0","#34D399"], text_color="white",background_corner_colors=[["#9EC9E0","#34D399"],["#152759","#064E3B"],["#152759","#064E3B"], ["#9EC9E0","#34D399"]],border_width=2)  # Não selecionada
configuracoes_button.grid(row=2, column=0, padx=(30, 0),)

sobre_button = ctk.CTkButton(tab_frame,anchor='w', text="Sobre", width=180, height=40, font=("Poppins", 16, "bold"),
                             command=lambda: mostrar_frame(sobre_frame, "sobre"), 
                             fg_color=["#9EC9E0","#34D399"], text_color="white",background_corner_colors=[["#9EC9E0","#34D399"], ["#152759","#064E3B"],["#152759","#064E3B"], ["#9EC9E0","#34D399"]],border_width=2)  # Não selecionada
sobre_button.grid(row=3, column=0, padx=(30, 0))

exit_button = ctk.CTkButton(tab_frame, text="SAIR", width=100, height=34,font=("Poppins", 16, "bold"), command=root.quit, corner_radius=16)
exit_button.grid(row=4, column=0, pady=(110,0))

mostrar_frame(param_frame, "parametros")

root.mainloop()
