import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time


class Interface:
    def __init__(self, program):
        self.__connected_program = program
        self.__connected_program.connect_interface(self)
        self.root = tk.Tk()
        self.fig, self.ax = plt.subplots()
        self.frame = tk.Frame(self.root)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.File = tk.Button(text="File", command=self.__connected_program.file)
        self.Animate = tk.Button(text="Animate", command=self.__connected_program.main)
        self.About = tk.Button(text="About", command=self.about)
        self.Exit = tk.Button(text="Exit", command=Program.exit)

        self.frame.pack()
        self.canvas.get_tk_widget().pack()
        self.File.pack()
        self.Animate.pack()
        self.About.pack()
        self.Exit.pack()

    def about(self):
        self.root = tk.Toplevel(self.root)
        self.root.geometry('100x100')
        self.root.information = tk.Label(self.root, text="\nПИЭ-21\nМилованов Д. А.\n")
        self.root.information.pack()

    def animate(self, array: list):
        if array:
            plt.cla()
            plt.bar(range(len(array)), array)
            plt.draw()
            time.sleep(0.3)
            self.root.update()

    def main(self):
        self.root.mainloop()

#
#
#


class Program:
    def __init__(self):
        self.__file_path = "Путь отсутствует."
        self.__array = []
        self.__connected_interface = None

    def connect_interface(self, interface: Interface):
        self.__connected_interface = interface

    def main(self):
        if self.__array:
            s = self.__array
            for i in range(len(s)-1):
                for j in range(len(s)-1):
                    if s[j] > s[j+1]:
                        s[j], s[j+1] = s[j+1], s[j]
                        self.__array = s
                        self.__connected_interface.animate(s)

    def file(self):
        # файл должен содержать числа разделённые пробелом
        self.__file_path = filedialog.askopenfilename()
        self.__array = list(map(int, open(self.__file_path, 'r').readline().split()))
        plt.cla()
        plt.bar(range(len(self.__array)), self.__array)
        plt.draw()

    @staticmethod
    def exit():
        quit()

    def get_array(self):
        return self.__array


p = Program()
a = Interface(p)
a.main()
