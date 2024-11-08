import customtkinter as ctk

class MonitoramentoTab(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=584, height=317, fg_color=["#152759","#064E3B"],corner_radius=0)
        self.grid_propagate(False)

        self.progress_label = ctk.CTkLabel(self, text="Progresso", font=("Poppins", 16, "bold"),width=100, text_color="white")
        self.progress_label.grid(row=0, column=0, padx=20, pady=30)

        self.progress = ctk.CTkProgressBar(self,width=400, height=15,progress_color=["#9EC9E0","#34D399"])
        self.progress.set(0)
        self.progress.grid(row=0, column=1, padx=20,pady=10)

        self.time = ctk.CTkLabel(self, text="Tempo faltante", font=("Poppins", 16, "bold"),width=100)
        self.time.grid(row=1, column=0, padx=20, pady=30)

        self.time_label = ctk.CTkLabel(self, text="30 min", font=("Poppins", 20, "bold"))
        self.time_label.grid(row=1, column=1, padx=20,pady=10)