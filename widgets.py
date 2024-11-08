import customtkinter as ctk

# Função para criar os botões de incremento e decremento
def add_plus_minus_buttom(parent, increment_func, decrement_func,frame_width,buttom_width=54,buttom_height=40):
    buttom_frame = ctk.CTkFrame(parent, width=frame_width, fg_color="#152759")
    increase_button = ctk.CTkButton(buttom_frame, text="+", width=buttom_width, height=buttom_height, command=increment_func, fg_color="#D9D9D9",text_color="black")
    increase_button.grid(row=0, column=0, padx=2)    
    decrease_button = ctk.CTkButton(buttom_frame, text="-", width=buttom_width, height=buttom_height, command=decrement_func, fg_color="#D9D9D9",text_color="black")
    decrease_button.grid(row=0, column=1,padx=2)
    return buttom_frame