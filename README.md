# ML-Toolkit

A toolkit for Machine Learning that helps and accelerates the process of installing software, toolkits, and packages commonly used for training models and working or studying Machine Learning.

## Index
1. [Description](#description)
2. [Installation](#installation)
3. [Use](#use)
4. [Functionality](#functionality)
5. [Technologies](#technologies)
6. [Examples](#examples)
7. [Problems](#problems)

## 1. Description
The project offers 10 options, numbered from 1 to 10, which can be selected one at a time.

The options are designed to meet the user's needs. All choices are related to Machine Learning, such as installing software, packages used for model training, toolkits for users, or examples of Git usage.

## 2. Instalation
To use setup.py, you need to install WSL. You can find instructions for installing WSL and running the file in docs/python/index.md and docs/python/usage.md.

## 3. Usage
To use ml-toolkit, you need to run the file in the WSL prompt or a Linux distribution.

1. First, check the project dependencies. With Python installed and packages updated, run:
    ```bash
    python setup.py
2. If Python is defined as python3, run:
    ```bash
    python3 setup.py
Make sure you are in the correct Git clone directory to avoid errors related to the directory path.

## 4. Functionals

Once the project is open, you can choose from the following options:

<u>[1] Option 1:</u> Update packages and system dependencies, including Python packages.

<u>[2] Option 2:</u> Verify the system distribution and then install Python.

<u>[3] Option 3:</u> Download and install pip.

<u>[4] Option 4:</u> Upgrade pip packages.

<u>[5] Option 5:</u> Download and install the Virtual Environment (venv).

<u>[6] Option 6:</u> Download and install Jupyter Notebook and Jupyter Lab. 

<u>[7] Option 7:</u> Download Python packages (pandas, matplotlib, scikit-learn).

<u>[8] Option 8:</u> Install Git. To use Git, you need a GitHub account. Once set up, you can use it to push projects.

<u>[9] Option 9:</u> The system will verify your distribution and install VSCode based on your system.

<u>[10] Option 10:</u> Install Docker.

## 5. Technologies

To build the project, Python was used along with the subprocess and os libraries. Additionally, we created a class called Installer, and inside it, a library named installer.py (located in utils/installer.py).

## 6. Examples

- To update sudo, select 1:
    ```bash
    nicolas@DESKTOP-FSA8S98:~/ml-toolkit$ python3 setup.py
    Select the option that you want to do:
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

## 7. Problems

If the user runs the file on a Windows distribution, setup.py might not work correctly, as the options selected in the project are designed for a WSL or Linux distribution/system.