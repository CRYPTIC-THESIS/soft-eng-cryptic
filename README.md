# Introduction #
`CRYPTIC` is a CNN-LSTM based application that forecast cryptocurrency prices of Bitcoin, Ethereum, and Dogecoin.
A Fuzzy-Logic module is added to give investment move suggestions.

# Requirements #
1. To run the application, the latest Python version needs to be installed.

2. A disk space of 2GB or more.

3. Windows 10 or above

4. Stable internet connection

* Visual Studio Code is the recommended IDE to run the application

# Installation #

### For Git:
> Note: Make sure to setup first your ssh key. You can follow the steps in this link: https://www.youtube.com/watch?v=8X4u9sca3Io

1. Copy the SSH key of the repository: `git@github.com:CRYPTIC-THESIS/soft-eng-cryptic.git`

2. Create a new workspace or folder in Visual Studio Code

3. Then open a terminal in VS Code and type:
    
    ```
    $ git clone git@github.com:CRYPTIC-THESIS/soft-eng-cryptic.git
    ```
    
4. Go to the directory of the repository you copied

    ```
    $ cd soft-eng-cryptic
    ```

5. Then install the `requirements.txt`

    ```
    $ pip install -r requirements.txt
    ```

### For Manual Installation:

1. Download the zip file at: 
    `https://drive.google.com/drive/folders/1bIkprBhCTrWB2cyxxRAFtUJ0GQo4eXmT?usp=sharing`

2. Extract the zip file to a new folder

3. Open the folder in VS Code then open a terminal, setting the directory at:

    ```
    $ cd soft-eng-cryptic
    ```

4. Then install the `requirements.txt`

    ```
    $ pip install -r requirements.txt
    ```

# Run the Application #
1. Open a terminal and make sure that the directory is in `.../soft-eng-cryptic/admin`
   
    ```
    $ cd soft-eng-cryptic/admin
    ```
    
2. Then run:

    ```
    $ python main.py
    ```
