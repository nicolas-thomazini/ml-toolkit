## Checking Python Installation

With WSL open and you in the cloned repository directory, follow these steps to install Python:

1. Run the following commands to update the package list and install Python 3:
    ```bash
    sudo apt update
    sudo apt install python3
    ```

2. Verify if Python was successfully installed:
    ```bash
    python --version
    ```

### Setting Up a Virtual Environment

With Python installed, you need to create a new virtual environment, as WSL and newer Linux distributions no longer use PIP by default:

1. Create the virtual environment by running:
    ```bash
    python -m venv path/to_new_virtual_venv
    ```

2. To activate the virtual environment, run:
    ```bash
    source path/to_new_virtual_venv/bin/activate
    ```

## Running the File

After installing all dependencies, you can now run the file. Make sure you are in the directory where you cloned the repository.

1. Ensure you're in the cloned repository path, and then run the setup.py file with the following command:
    ```bash
    python setup.py
    ```

2. In the menu that appears, you can choose options 1 to 10. Option 10 is to exit the setup.

