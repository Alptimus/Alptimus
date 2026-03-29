# Baseline Setup

## [Download Python](https://www.python.org/downloads/)
<sub>Note: This course uses Python 3.11 but I used 3.10.12</sub>

## Python Installation Guides

1. [Windows](https://www.digitalocean.com/community/tutorials/install-python-windows-10)
2. [Linux](https://docs.python-guide.org/starting/install3/linux/)
3. [MacOS](https://www.dataquest.io/blog/installing-python-on-mac/)

## IDE Setup

We recommend using [Visual Studio Code](https://code.visualstudio.com/) as our IDE. Alternatively, you can use Sublime Text if it suits your preferences.

1. [Download & Install Visual Studio Code](https://www.liquidweb.com/kb/how-to-install-vscode-on-linux-mac-windows/#:~:text=Installing%20VSCode%20on%20Linux%2C%20Mac,that%20you%20can%20begin%20coding.)

2. **Helper Extensions:**
    - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) (optional)
    - [Jinja](https://marketplace.visualstudio.com/items?itemName=wholroyd.jinja) (optional)

## Virtual Environment Setup

1. Update system pip:
    ```
    pip install -U pip
    ```

2. Install virtualenv:
    ```
    pip install virtualenv
    ```

3. Create a new virtual environment:
    ```
    python3 -m venv ./<your_venv_name>
    ```

4. Activate the virtual environment:
    ```
    source <your_venv_name>/bin/activate
    ```

5. Create requirements.txt to manage packages:
    - Django==4.2  
    <sub>Note: This course uses Django 4.1 but I used 4.2</sub>

6. Install packages from requirements.txt:
    ```
    pip install -r requirements.txt
    ```

7. Deactivate the virtual environment:
    ```
    deactivate
    ```

## Success!

Congratulations! You have successfully set up Django in your virtual environment and are ready to proceed with the course.