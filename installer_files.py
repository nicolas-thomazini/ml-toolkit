#libraries
import pyautogui as gui
import time
import os
import subprocess
import setup

class Installer:
    def install_python():
        print("a")
        ''''
        try:
            print("Baixando e instalando o Python...")
            subprocess.run(["sudo", "apt", "install", "-y", "python"], check=True)
            print(Python instalado com Sucesso!
                
                    Retornando à Tela Principal...   
                )
        except subprocess.CalledProcessError as e:
            print(f"Erro durante a instalação do Python: {e}")
        '''
    def install_pip():
        try:
            print("Baixando e instalando o Pip...")
            subprocess.run(["sudo", "apt", "install", "-y", "pip"], check=True)
            print('''PIP instalado com Sucesso!
                
                    Retornando à Tela Principal...   
                ''')
        except subprocess.CalledProcessError as e:
            print(f"Erro durante a instalação do Pip: {e}")

    def download_python():
        a = 0
    def download_jupyter():
        a = 0
    def download_vscode():
        a = 0
    def install_vscode():
        a = 0
    def install_libraries():
        a = 0