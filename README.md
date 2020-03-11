# Simple PoC for connecting PyQt5 to Sqlite 

## Prerequisites : 
_The **How to Setup** section assumes you have installed and/or are familiar with the following:_
* Git 
    > You can find how to install git [Here](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/)
* Anaconda
    > You can find how to install Anaconda [Here](https://www.datacamp.com/community/tutorials/installing-anaconda-windows)
* PyQt5 
    > You can find a comprehensive tutorial on PyQt5 [Here](https://www.youtube.com/playlist?list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj)


## How to setup :

### Step 1: Clone this repository.
```bash
$ git clone https://github.com/programmer290399/Connecting-PyQt5-to-Sqlite.git
```

### Step 2: Install the Dependencies.
```bash
$ conda create --name <name_of_your_env> --file requirements.txt 
```
### Step 3: Run the Application.

```bash
$ conda activate <name_of_your_env>
$ python sa_version.py
```


> NOTES : 
>1. This repo contains the `form.ui` file which can be used with `Qt 5 Designer`.
>2. Command to convert a `.ui` file to `.py` is :
    >```bash
    >$ python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py
    >```
