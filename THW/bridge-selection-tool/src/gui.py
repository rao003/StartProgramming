from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from structural_calculations import calculate_bridge_configuration

class BridgeSelectionTool:
    def __init__(self, master):
        self.master = master
        master.title("Bridge Selection Tool")

        self.span_label = Label(master, text="Enter Span (m):")
        self.span_label.pack()

        self.span_var = StringVar()
        self.span_entry = Entry(master, textvariable=self.span_var)
        self.span_entry.pack()

        self.load_label = Label(master, text="Enter Load Class (tons):")
        self.load_label.pack()

        self.load_var = StringVar()
        self.load_entry = Entry(master, textvariable=self.load_var)
        self.load_entry.pack()

        self.calculate_button = Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

    def calculate(self):
        try:
            span = float(self.span_var.get())
            load_class = int(self.load_var.get())
            config, num_panels, components = calculate_bridge_configuration(span, load_class)

            if config:
                result_text = f"Recommended Configuration: {config}\n"
                result_text += f"Number of Panels: {num_panels}\n"
                result_text += "Estimated Component List:\n"
                for item, count in components.items():
                    result_text += f"  - {item}: {count}\n"
                self.result_label.config(text=result_text)
            else:
                messagebox.showerror("Error", "No valid configuration found.")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for span and load class.")

if __name__ == "__main__":
    root = Tk()
    bridge_selection_tool = BridgeSelectionTool(root)
    root.mainloop()