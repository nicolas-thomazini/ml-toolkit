import os
import platform
import subprocess
import urllib.request

system = platform.system()

class Installer:
    @staticmethod
    def update():
        try:
            print("Updating Sudo...")
            subprocess.run(["sudo", "apt", "update"])
            print("Update with Success!")
        except subprocess.CalledProcessError as e:
            print(f"Fail to update Sudo: {e}")

    @staticmethod
    def _python():
        system = platform.system()

        try:
            if system == "Windows":
                print("Install Python on Windows...")
                url = "https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe"
                installer_path = "python_installer.exe"
                
                urllib.request.urlretrieve(url, installer_path)
                
                subprocess.run([installer_path, "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)
                os.remove(installer_path)
                print("Python installed with Sucess!")
                
            elif system == "Linux":
                print("Install Python on Linux...")
                subprocess.run(["sudo", "apt-get", "install", "-y", "python3"], check=True)
                print("Python installed with Success!")
                
            else:
                print("System not supported.")
        
        except subprocess.CalledProcessError as e:
            print(f"Error to install Python: {e}")
            if system == "Windows":
                print("Make sure you have administrator permissions to run the installer.")
            elif system == "Linux":
                print("Check if you have sudo permissions or if apt-get is configured correctly.")
        except Exception as e:
            print(f"Erro inesperado ao instalar o Python: {e}")

    @staticmethod
    def _venv():
        try:
            print("Downloading and Installing Venv...")
            subprocess.run(["python", "-m", "pip", "install", "--user", "virtualenv"], check=True)
            print("VirtualEnv installed!")
        except subprocess.CalledProcessError as e:
            print(f"Error to install VirtualEnv {e}")

    @staticmethod
    def _pip():
        try:
            print("Downloading and Installing Pip..")
            subprocess.run(["python", "-m", "ensurepip", "--upgrade"], check=True)
            print("PIP installed with Success!")
        except subprocess.CalledProcessError as e:
            print(f"Error to install Pip: {e}")
    
    def up_pip():
        try:
            print("Upgrading pip...")
            subprocess.run(["python.exe", "-m", "pip", "install", "--upgrade", "pip"])
            print("Upgrade PIP with Success!")
        except subprocess.CalledProcessError as e:
            print(f"Error to upgrade PIP: {e}")
    
    @staticmethod
    def jupyter():
        try:
            print("Downloading and isntalling jupyterlab and jupyter notebook...")
            subprocess.run(["pip3", "install", "jupyterlab"], check=True)
            subprocess.run(["pip3", "install", "notebook"], check=True)
            print("Jupyter installed with Success!")
        except subprocess.CalledProcessError as e:
            print(f"Error to install Jupyter: {e}")

    @staticmethod
    def vscode():
        try:
         
            print("Downloading installer VsCode...")
            url = "https://update.code.visualstudio.com/latest/win32-x64-user/stable"
            installer_name = "vscode-installer.exe"
            subprocess.run(["powershell", "-Command", f"curl -o {installer_name} {url}"], check=True)
            print("Download and installing VsCode...")
            subprocess.run([installer_name, "/silent"], check=True)
            print("Download finished. Exiting...")
            os.remove(installer_name)
            print("Installer Removed.")
            print("VsCode installed with Success!")
        except subprocess.CalledProcessError as e:
            print(f"Fail to install VsCode: {e}")

    @staticmethod
    def git():
        try:
            print("Downloading and installing git...")
            subprocess.run(["sudo", "apt", "install", "git-all"], check=True)
            print("Download finished. Exiting...")
        except subprocess.CalledProcessError as e:
            print("Failed to Install Git")
        
    @staticmethod    
    def packages():
        try:
            print("Installing packages...")
            subprocess.run(["pip3", "install", "pandas"])
            subprocess.run(["pip3", "install", "matplotlib"])
            subprocess.run(["pip3", "install", "scikit-learn"])
            print("The Packages has been Installed. Exiting...")
        except subprocess.CalledProcessError as e:
            print("Error to install packages.")
    
    @staticmethod
    def docker():
        try:
            print("Installing docker...")
            subprocess.run(["pip3", "install", "docker"])
            print("Docker installed with Success!")
        except subprocess.CalledProcessError as e:
            print("Fail to install Docker.")
    
