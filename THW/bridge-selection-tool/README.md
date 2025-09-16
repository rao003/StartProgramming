# Bridge Selection Tool

## Overview
The Bridge Selection Tool is a Python application designed to assist users in selecting the appropriate bridge configuration based on their specific requirements. The tool features a graphical user interface (GUI) that allows users to input the required span and load capacity, and it provides recommendations based on predefined bridge configurations.

## Features
- User-friendly GUI for easy input of bridge requirements.
- Accurate calculations for bridge configurations based on user input.
- Generates a detailed component list for the recommended bridge configuration.
- Provides a user guide for assistance.

## Installation
To set up the Bridge Selection Tool, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd bridge-selection-tool
   ```

3. Install the required dependencies. You can use pip to install the necessary packages listed in `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application by executing the `gui.py` script:
   ```
   python src/gui.py
   ```

2. Input the required span (in meters) and load capacity (in tons) in the GUI.

3. Click the "Calculate" button to receive the recommended bridge configuration.

4. Review the results displayed in the GUI, which includes the configuration name, number of panels, and an estimated component list.

## User Guide
For detailed instructions on how to use the Bridge Selection Tool, please refer to the `user_guide.txt` file included in the project.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.