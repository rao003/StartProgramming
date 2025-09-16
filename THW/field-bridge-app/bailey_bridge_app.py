# bailey_bridge_app.py

import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF
import datetime

# --- PHASE 1: COMPONENT DATA (from previous step) ---

class Component:
    """A generic class to represent a Bailey bridge component."""

    def __init__(self, name, weight_kg, dimensions_m, description):
        self.name = name
        self.weight_kg = weight_kg
        self.dimensions_m = dimensions_m
        self.description = description

# Define the Bailey Bridge components
PANEL = Component("Panel", 259, (3.048, 0.448, 1.448), "The main structural unit of the bridge truss.")
PANEL_PIN = Component("Panel Pin", 2.5, (0.041, 0.178, 0.041), "Connects panels together.")
TRANSOM = Component("Transom", 250, (3.25, 0.45, 0.15), "Cross-girder that supports the roadway.")
LAUNCHING_NOSE_PANEL = Component("Launching Nose Panel", 150, (3.048, 0.448, 1.448), "Lighter panel used for the launching nose.")
ROCKING_ROLLER = Component("Rocking Roller", 150, (0.45, 0.45, 0.2), "Roller base for launching the bridge.")

component_database = {
    "Panel": PANEL,
    "Panel Pin": PANEL_PIN,
    "Transom": TRANSOM,
    "Launching Nose Panel": LAUNCHING_NOSE_PANEL,
    "Rocking Roller": ROCKING_ROLLER
}

# --- PHASE 1: STRUCTURAL CALCULATIONS (from previous step) ---

BRIDGE_CONFIGURATIONS = {
    'Single-Single': [(12.2, 70), (18.3, 40), (24.4, 12)],
    'Single-Double': [(18.3, 70), (24.4, 40), (30.5, 12)],
    'Single-Triple': [(24.4, 70), (30.5, 40), (36.6, 12)],
    'Double-Single': [(24.4, 70), (30.5, 40), (42.7, 12)],
    'Double-Double': [(30.5, 70), (36.6, 40), (48.8, 12)],
    'Double-Triple': [(36.6, 70), (42.7, 40), (54.9, 12)],
}

def calculate_bridge_configuration(span_m, load_class_tons):
    sorted_configs = sorted(
        BRIDGE_CONFIGURATIONS.keys(),
        key=lambda k: (
            k.count('Single') + k.count('Double') * 2 + k.count('Triple') * 3,
            k.count('Single') + k.count('Double') * 2
        )
    )

    for config in sorted_configs:
        for max_span, max_load in BRIDGE_CONFIGURATIONS[config]:
            if span_m <= max_span and load_class_tons <= max_load:
                num_panels = int(span_m / 3.048)
                if span_m % 3.048 != 0:
                    num_panels += 1
                num_panels = max(num_panels, 4)

                wall_multiplier = config.count('Single') + config.count('Double') * 2 + config.count('Triple') * 3
                story_multiplier = 1 if 'Single' in config else 2
                
                total_panels = num_panels * wall_multiplier * story_multiplier
                total_transoms = num_panels
                
                # Simplified component list
                components = {
                    "Panel": total_panels,
                    "Transom": total_transoms,
                    "Panel Pin": total_panels * 2,
                    "Launching Nose Panel": 4 * wall_multiplier * story_multiplier,
                    "Rocking Roller": 2
                }
                
                return config, num_panels, components

    return None, None, None

# --- PHASE 1: LOGISTICS CALCULATIONS (from previous step) ---

def calculate_roller_placement(num_panels):
    PANEL_LENGTH_M = 3.048
    roller_distance_from_bank = 1.5 * PANEL_LENGTH_M
    return roller_distance_from_bank

def calculate_height_adjustment(near_bank_elevation_m, far_bank_elevation_m, bridge_span_m):
    sag_compensation_m = bridge_span_m / 400
    elevation_difference_m = far_bank_elevation_m - near_bank_elevation_m
    required_adjustment_m = elevation_difference_m + sag_compensation_m
    return required_adjustment_m

# --- PHASE 2 & 3: GUI & REPORTING ---

class BaileyBridgeApp:
    def __init__(self, master):
        self.master = master
        master.title("Bailey Bridge App")

        self.create_widgets()

    def create_widgets(self):
        # Frame for input fields
        input_frame = tk.LabelFrame(self.master, text="Bridge Requirements", padx=10, pady=10)
        input_frame.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Label(input_frame, text="Span (meters):").grid(row=0, column=0, sticky="W")
        self.span_entry = tk.Entry(input_frame)
        self.span_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="Load Class (tons):").grid(row=1, column=0, sticky="W")
        self.load_entry = tk.Entry(input_frame)
        self.load_entry.grid(row=1, column=1)

        tk.Label(input_frame, text="Near Bank Elevation (m):").grid(row=2, column=0, sticky="W")
        self.near_elev_entry = tk.Entry(input_frame)
        self.near_elev_entry.grid(row=2, column=1)

        tk.Label(input_frame, text="Far Bank Elevation (m):").grid(row=3, column=0, sticky="W")
        self.far_elev_entry = tk.Entry(input_frame)
        self.far_elev_entry.grid(row=3, column=1)
        
        # Calculate button
        calculate_button = tk.Button(input_frame, text="Calculate & Generate Report", command=self.run_calculations)
        calculate_button.grid(row=4, columnspan=2, pady=10)

        # Output Text Box
        self.output_text = tk.Text(self.master, height=15, width=60)
        self.output_text.pack(padx=10, pady=5)

    def run_calculations(self):
        try:
            span = float(self.span_entry.get())
            load_class = int(self.load_entry.get())
            near_elev = float(self.near_elev_entry.get())
            far_elev = float(self.far_elev_entry.get())

            # Clear previous output
            self.output_text.delete('1.0', tk.END)

            # Structural Calculations
            config, num_panels, components = calculate_bridge_configuration(span, load_class)

            if not config:
                messagebox.showerror("Error", "No valid bridge configuration found for these specifications.")
                self.output_text.insert(tk.END, "Error: No valid configuration found.")
                return

            self.output_text.insert(tk.END, f"Bridge Design Summary\n\n")
            self.output_text.insert(tk.END, f"Span: {span:.2f} m\n")
            self.output_text.insert(tk.END, f"Load Class: {load_class} tons\n")
            self.output_text.insert(tk.END, f"Recommended Configuration: {config}\n")
            self.output_text.insert(tk.END, f"Number of Panels per Chord: {num_panels}\n")
            self.output_text.insert(tk.END, "\nComponent List:\n")
            
            for item, count in components.items():
                self.output_text.insert(tk.END, f"  - {item}: {count}\n")
            
            # Logistics Calculations
            roller_placement = calculate_roller_placement(num_panels)
            height_adjustment = calculate_height_adjustment(near_elev, far_elev, span)
            
            self.output_text.insert(tk.END, f"\nLogistics & Placement\n\n")
            self.output_text.insert(tk.END, f"Recommended roller placement from near bank: {roller_placement:.2f} m\n")
            self.output_text.insert(tk.END, f"Required height adjustment: {height_adjustment:.2f} m (raise if positive, lower if negative)\n")
            
            # Generate PDF Report
            self.generate_pdf_report(span, load_class, config, num_panels, components, roller_placement, height_adjustment)
            
            messagebox.showinfo("Success", "Calculations complete. A PDF report has been generated.")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numerical values for all fields.")

    def generate_pdf_report(self, span, load_class, config, num_panels, components, roller_placement, height_adjustment):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", size=16)
        
        # Title
        pdf.cell(200, 10, txt="Bailey Bridge Calculation Report", ln=1, align="C")
        pdf.set_font("Helvetica", size=12)
        pdf.cell(200, 10, txt=f"Report Date: {datetime.date.today()}", ln=1, align="C")
        
        # Section 1: Bridge Design Summary
        pdf.ln(10)
        pdf.set_font("Helvetica", style="B", size=14)
        pdf.cell(200, 10, txt="1. Bridge Design Summary", ln=1)
        pdf.set_font("Helvetica", size=12)
        pdf.cell(200, 7, txt=f"Span: {span:.2f} m", ln=1)
        pdf.cell(200, 7, txt=f"Load Class: {load_class} tons", ln=1)
        pdf.cell(200, 7, txt=f"Recommended Configuration: {config}", ln=1)
        pdf.cell(200, 7, txt=f"Number of Panels per Chord: {num_panels}", ln=1)
        
        # Section 2: Component List
        pdf.ln(10)
        pdf.set_font("Helvetica", style="B", size=14)
        pdf.cell(200, 10, txt="2. Required Components", ln=1)
        pdf.set_font("Helvetica", size=12)
        for item, count in components.items():
            pdf.cell(200, 7, txt=f"  - {item}: {count}", ln=1)
        
        # Section 3: Logistics & Placement
        pdf.ln(10)
        pdf.set_font("Helvetica", style="B", size=14)
        pdf.cell(200, 10, txt="3. Logistics & Placement", ln=1)
        pdf.set_font("Helvetica", size=12)
        pdf.cell(200, 7, txt=f"Recommended roller placement from near bank: {roller_placement:.2f} m", ln=1)
        pdf.cell(200, 7, txt=f"Required height adjustment: {height_adjustment:.2f} m", ln=1)
        if height_adjustment > 0:
            pdf.cell(200, 7, txt=f"(Raise the roller base by {height_adjustment:.2f} m)", ln=1)
        else:
            pdf.cell(200, 7, txt=f"(Lower the roller base by {-height_adjustment:.2f} m)", ln=1)
            
        pdf.output("Bailey_Bridge_Report.pdf")

if __name__ == "__main__":
    root = tk.Tk()
    app = BaileyBridgeApp(root)
    root.mainloop()