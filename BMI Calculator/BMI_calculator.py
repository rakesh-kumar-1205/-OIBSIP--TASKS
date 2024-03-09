import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BMICalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")

        # Variables
        self.weight_var = tk.DoubleVar()
        self.height_var = tk.DoubleVar()
        self.bmi_var = tk.StringVar()
        self.user_data = []

        # GUI Elements
        self.label_weight = tk.Label(master, text="Weight (kg):")
        self.entry_weight = tk.Entry(master, textvariable=self.weight_var)

        self.label_height = tk.Label(master, text="Height (m):")
        self.entry_height = tk.Entry(master, textvariable=self.height_var)

        self.button_calculate = tk.Button(master, text="Calculate BMI", command=self.calculate_bmi)

        self.label_bmi = tk.Label(master, text="BMI:")
        self.label_result = tk.Label(master, textvariable=self.bmi_var)

        self.button_save = tk.Button(master, text="Save Data", command=self.save_data)

        self.button_plot = tk.Button(master, text="Plot BMI Trend", command=self.plot_bmi_trend)

        # Grid layout
        self.label_weight.grid(row=0, column=0, padx=10, pady=5)
        self.entry_weight.grid(row=0, column=1, padx=10, pady=5)

        self.label_height.grid(row=1, column=0, padx=10, pady=5)
        self.entry_height.grid(row=1, column=1, padx=10, pady=5)

        self.button_calculate.grid(row=2, column=0, columnspan=2, pady=10)

        self.label_bmi.grid(row=3, column=0, padx=10, pady=5)
        self.label_result.grid(row=3, column=1, padx=10, pady=5)

        self.button_save.grid(row=4, column=0, columnspan=2, pady=10)

        self.button_plot.grid(row=5, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_var.get())
            height = float(self.height_var.get())
            bmi = round(weight / (height ** 2), 2)
            self.bmi_var.set(str(bmi))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for weight and height.")

    def save_data(self):
        try:
            weight = float(self.weight_var.get())
            height = float(self.height_var.get())
            bmi = float(self.bmi_var.get())
            self.user_data.append({"Weight": weight, "Height": height, "BMI": bmi})
            messagebox.showinfo("Success", "Data saved successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please calculate BMI before saving data.")

    def plot_bmi_trend(self):
        if len(self.user_data) < 2:
            messagebox.showerror("Error", "Insufficient data to plot trend.")
            return

        weights = [data["Weight"] for data in self.user_data]
        heights = [data["Height"] for data in self.user_data]
        bmis = [data["BMI"] for data in self.user_data]

        fig, ax = plt.subplots(figsize=(8, 6))

        ax.plot(bmis, label="BMI Trend", marker='o')
        ax.set_xlabel("Data Points")
        ax.set_ylabel("BMI")
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=6, column=0, columnspan=2, pady=10)

# Main application
root = tk.Tk()
bmi_calculator = BMICalculator(root)
root.mainloop()
