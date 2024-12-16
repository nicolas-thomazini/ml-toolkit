# Libraries
import os
import subprocess
from utils.installer import Installer

def main():
    while True:
        option = int(input('''Select the option that you want to do: 
                    [1] Update Sudo       
                    [2] Download and Installation Python
                    [3] Download and Install PIP
                    [4] Upgrade PIP
                    [5] Download and Install Virtual Enviroment (venv)    
                    [6] Download and Installation Jupyter Notebook and Lab
                    [7] Install ML Python Packages
                    [8] Install Git
                    [9] Download and Installation VsCode
                    [10] Install Docker
                    [0] Exit    
                    '''))

        match option:
            case 1:
                Installer.update()
            case 2:
                Installer._python()
            case 3:
                Installer._pip()
            case 4:
                Installer.up_pip()
            case 5:
                Installer._venv()
            case 6:
                Installer.jupyter()
            case 7:
                Installer.packages()
            case 8:
                Installer.git()
            case 9:
                Installer.vscode()
            case 10:
                Installer.docker()
            case 0:
                print("Exiting ML-Toolkit...")
                break
            case _:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()