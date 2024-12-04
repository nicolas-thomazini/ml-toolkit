#libraries
import pyautogui as gui
import time
import os
import subprocess

#parameters

#function main, that we choice the option

def main():
    option = int(input('''Select the option that you want to do: 
                   [1] Download and Installation Python
                   [2] Download and Install PIP     
                   [3] Download and Installation Jupyter
                   [4] Download and Installation VsCode
                   [5] Install Git
                   [6] Install ML Python Packages
                   [7] Install Docker
                   '''))
    
    match option:
        case 1:
            from installer_files import Installer
            Installer.install_python()
        case _:
            print("Invalid Option")
            exit()

if __name__ == "__main__":
    main()
