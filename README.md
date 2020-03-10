# Simple PoC for connecting PyQt5 to Sqlite 

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
$ python sa_version.py
```


> NOTES : 
>1. This repo contains the `form.ui` file which can be used with `Qt 5 Designer`.
>2. Command to convert a `.ui` file to `.py` is :
    >```bash
    >$ python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py
    >```
