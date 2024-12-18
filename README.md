# ML-Toolkit

    A toolkit for Machine Learning to helps  and acelerate the process to install softwares, toolkits and packages that a person uses Machine Learning to work or study.

## Index
1. [Description](#description)
2. [Instalation](#instalation)
3. [Use](#use)
4. [Functionals](#functionals)
5. [Technologies](#technologies)
6. [Examples](#examples)
7. [Problems](#problems)

## 1. Description
The project has 10 options of 1 to 10 that can be choiced one time select.

The options will be selected by the necessity of the person. All choices presents are relation to ML, for example installations of softwares or packages that used for training a model, toolkits that used for users, example of git.

## 2. Instalation
To use the setup.py, you need to install WSL. In <a>docs/python/index.md</a> and <a> docs/python/usage.md </a> you can see the instructions for install WSL and run the file.

## 3. Use
To use ml-toolkit, you need to run the file in the WSL prompt, or Linux distribuition.

1. Check the dependecies project. With Python installed and packages udpateds, you can run:
    ```bash
    python setup.py
2. If python it's defined width python3, run:
    ```bash
    python3 setup.py
Certify if you stay in the git clone path in case to generated a error directory.

## 4. Functionals

With project open, you can choice the option that appear:

<u>[1] Option 1:</u> update packages and system dependecies, include python packages.

<u>[2] Option 2:</u> verify the system distribuition and next install python.

<u>[3] Option 3:</u> download and install pip.

<u>[4] Option 4:</u> upgrade pip packages.

<u>[5] Option 5:</u> download and install Virtual Enviroment (venv)

<u>[6] Option 6:</u> download and install jupyter notebook and jupyter lab

<u>[7] Option 7:</u> download python packages (pandas, matplotlib, scikit-learn)

<u>[8] Option 8:</u> install git. To use git, you need to an account in GitHub, one time this it used to up projetcs.

<u>[9] Option 9:</u> the system will be verify your distribution and install vscode based you have.

<u>[10] Option 10:</u> install docker. 

## 5. Technologies

To made the project, was used Python language and subprocess and os library, in addition a class that we created that called "Installer", where created a library that call installer.py (utils/installer.py).

## 6. Examples

- To update sudo:
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

If user run the file in Windows distribuitions, the setup.py cannot be work well, one time the options that selected in the project was projcted to WSL distribuition or system Linux.
