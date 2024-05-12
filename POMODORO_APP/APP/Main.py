import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage

class PomodoroTimer:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x350")
        self.root.title("POMODORO APP - MAT")
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file="C:/Users/mateu/Desktop/APP_POMODOR/POMODORO_APP/APP/Timer.png"))


        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=("Ubuntu, 16"))
        self.s.configure("TButton.Tab", font=("Ubuntu, 16"))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=10, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        self.timer_label = ttk.Label(self.tab1, text ="25:00", font=("Ubunto", 58))
        self.timer_label.pack(pady=50)

        self.descanso_label = ttk.Label(self.tab2, text ="05:00", font=("Ubunto", 58))
        self.descanso_label.pack(pady=50)
        
        self.pausa_label = ttk.Label(self.tab3, text ="15:00", font=("Ubunto", 58))
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

        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text="Contagem: 0", font=("Ubunto", 16))
        self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.pomodoros = 0
        self.skipped = False
        self.stopped = False
        self.running = False

        self.root.mainloop()

    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True

    def start_timer(self):
        self.stopped = False
        self.skipped = False

        timer_id = self.tabs.index(self.tabs.select()) + 1

        if timer_id == 1:
            full_seconds = 60 * 25

            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.timer_label.config(text=f"{minutes: 02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            
            if not self.stopped or self.skipped:
                self.pomodoros += 1
                self.pomodoro_counter_label.config(text=f"Pomodoros: {self.pomodoros}")
                if self.pomodoros % 4 == 0:
                    self.tabs.select(2)
                else:
                    self.tabs.select(1)
                    self.start_timer()

        elif timer_id == 2:
            full_seconds = 60 * 5

            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.descanso_label.config(text=f"{minutes: 02d}:{seconds:02d}")
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
                self.pausa_label.config(text=f"{minutes: 02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()
        else:
            print("ID de Timer Invalido")
                        

    def reset_clock(self):
        self.stopped = True
        self.skipped = False
        self.pomodoros = 0
        self.timer_label.config(text="25:00")
        self.descanso_label.config(text="05:00")
        self.pausa_label.config(text="15:00")
        self.pomodoro_counter_label.config(text="Pomodores: 0")
        self.running = False

    def skip_clock(self):
        current_tab = self.tabs.index(self.tabs.select())
        if current_tab == 0:
            self.timer_label.config(text="25:00")
        elif current_tab == 1:
            self.descanso_label.config(text="05:00")
        elif current_tab == 2:
            self.pausa_label.config(text="15:00")

        self.stopped = True
        self.skipped = True


PomodoroTimer()

