# Install Python


Go to https://www.python.org/downloads/

Select Python Version and OS (OS is automatically selected)

We will use Python 3.9.2 (but any version starting with 3 is okay!)

Include your python executable to your **$PATH** 

### To check if you've installed successfully

Open the terminal: 

- For MacOS press (cmd + space) then type "terminal" and press "Enter"
- For Windows Windows+R to open “Run” box, Type “cmd” and then click “OK”

After opening the terminal enter the following command:

> python --version

If you see a version number, then you've successfully installed Python. 


# Download get-pip.py

There are thousands of packages that we can use instead of writing the code from the scratch.

Installing and managing packages can be hard and cumbersome.

Pip helps us install and manage packages.

Download the following link.

https://bootstrap.pypa.io/get-pip.py (right click -> save as)

Note where you saved the get-pip.py file.


# Install Pip

Open the terminal again and navigate to the location where you saved **get-pip.py**.

You can use the following commands to navigate in a terminal (for Linux and MacOS):

- **cd**: Change Directory 
- **ls**: List the contents of current directory
- **pwd**: Print Working Directory (Current directory path)
- **cp**: Copy
- **mkdir**: Make Directory
- **mv**: Move


For example: If your **get-pip.py** file is in /Users/USERNAME/Downloads/ directory, then you can navigate there by typing the following command:
> **cd** /Users/USERNAME/Downloads

Once you've navigated to the correct directory run the following command:

> python get-pip.py

This will install Pip for us.

### To check if you've installed pip successfully

Open the terminal (if it's not already open)

Type the following command:

> pip --version

If you see a version number, then you've successfully installed Pip. 



# Jupyter Notebook

For every programming language, we need a platform to write and execute our code. 
These are called Integrated Development Environment (IDE)

There are many IDEs for different languages. For python we can use:

- IDLE
- PyCharm
- VSCode
- Spyder
- PyDev
- Atom
- etc.



However, my personal favorite is Jupyter Notebooks for couple of reasons:

- It runs on browser so you don't need additional UI.
- You can divide your code into multiple blocks and execute just the parts you want to.
- You can get intermediate results from the code, to check the validity.
- etc.


You can see a sample jupyter notebook environment below.
![title](images/python-jupyter.png)


### To Install Jupyter Notebook

Open a terminal and execute the following command:

> pip install notebook

To check if you have successfully installed Jupyter Notebook, execute the following command:

> jupyter notebook
