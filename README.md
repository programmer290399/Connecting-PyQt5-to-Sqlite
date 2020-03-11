# Simple PoC for connecting PyQt5 to Sqlite 

## Prerequisites :
* Git: you must have git installed on your machine. 
> You can find how to install git [Here](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/)
* Anaconda


## How to setup :

### Step 1: Clone this repository.
```bash
$ git clone <>
```

### Step 2: Install the Dependencies.
```bash
$ conda create --name <name_of_your_env> --file requirements.txt 
```
### Step 3: Run the Application.

```bash
$ python sa_version.py
```


> NOTES : 
>1. This repo contains the `form.ui` file which can be used with `Qt 5 Designer`.
>2. Command to convert a `.ui` file to `.py` is :
    >```bash
    >$ python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py
    >```
