# D-Brücke Bridge Selector

## Overview
The D-Brücke Bridge Selector is a Python program designed to assist engineers and planners in selecting the most suitable bridge configuration based on specific span and load requirements. Utilizing data from the D-brücke manual, the program prioritizes accuracy in determining the best bridge type for construction.

## Features
- Input span and load requirements.
- Retrieve the best bridge configuration based on the D-brücke manual.
- Provides detailed information about the recommended bridge type.

## Installation
To set up the D-Brücke Bridge Selector, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/d-bruecke-bridge-selector.git
   ```

2. Navigate to the project directory:
   ```
   cd d-bruecke-bridge-selector
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To use the D-Brücke Bridge Selector, run the `bridge_selector.py` script:

```
python src/bridge_selector.py
```

You will be prompted to enter the required span (in meters) and load capacity (in tons). The program will then output the best bridge configuration based on your input.

## Testing
To ensure the functionality of the bridge selection logic, unit tests are provided. You can run the tests using:

```
pytest tests/test_bridge_selector.py
```

## Contributing
Contributions are welcome! If you have suggestions for improvements or additional features, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.