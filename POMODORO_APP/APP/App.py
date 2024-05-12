import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage

class PomodoroTimer:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x350")
        self.root.title("POMODORO APP - MAT")
        # Modifiquei o caminho da imagem do ícone para algo mais genérico
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file="Timer.png"))

        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=("Ubuntu", 16))
        self.s.configure("TButton", font=("Ubuntu", 16))  # Corrigi o estilo do botão aqui

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=10, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        # Corrigi o nome das variáveis dos labels
        self.timer_label = ttk.Label(self.tab1, text="25:00", font=("Ubuntu", 58))
        self.timer_label.pack(pady=50)

        self.descanso_label = ttk.Label(self.tab2, text="05:00", font=("Ubuntu", 58))
        self.descanso_label.pack(pady=50)
        
        self.pausa_label = ttk.Label(self.tab3, text="15:00", font=("Ubuntu", 58))
        self.pausa_label.pack(pady=50)

        self.tabs.add(self.tab1, text="TIMER")
        self.tabs.add(self.tab2, text="DESCANSO")
        self.tabs.add(self.tab3, text="PAUSA")

        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=20)

        self.start_button = ttk.Button(self.grid_layout, text="Iniciar", command=self.start_timer_thread)
        self.start_button.grid(row=0, column=0)

        self.skip_button = ttk.Button(self.grid_layout, text="Proximo", command=self.skip_clock)
        self.skip_button.grid(row=0, column=1)

        self.reset_button = ttk.Button(self.grid_layout, text="Resetar", command=self.reset_clock)
        self.reset_button.grid(row=0, column=2)

        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text="Contagem: 0", font=("Ubuntu", 16))
        self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.pomodoro = 0
        self.skipped = False
        self.stopped = False

        self.root.mainloop()

    def start_timer_thread(self):
        t = threading.Thread(target=self.start_timer)
        t.start()

    def start_timer(self):
        self.stopped = False
        self.skipped = False

        timer_id = self.tabs.index(self.tabs.select()) + 1

        if timer_id == 1:
            full_seconds = 60 * 25
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")  # Corrigi o nome do label aqui
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            
            if not self.stopped or self.skipped:
                self.pomodoro += 1
                self.pomodoro_counter_label.config(text=f"Pomodoros: {self.pomodoro}")  # Corrigi o nome da variável aqui
                if self.pomodoro % 4 == 0:
                    self.tabs.select(2)
                else:
                    self.tabs.select(1)
                    self.start_timer()

        elif timer_id == 2:
            full_seconds = 60 * 5
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.descanso_label.config(text=f"{minutes:02d}:{seconds:02d}")  # Corrigi o nome do label aqui
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()
        
        elif timer_id == 3:
            full_seconds = 60 * 15
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.pausa_label.config(text=f"{minutes:02d}:{seconds:02d}")  # Corrigi o nome do label aqui
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()
        else:
            print("ID de Timer Inválido")
                        

    def reset_clock(self):
        pass

    def skip_clock(self):
        pass

PomodoroTimer()
