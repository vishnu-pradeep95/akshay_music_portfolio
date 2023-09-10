### Installation Steps:

#### Step 1: Install Python

1. **Windows/Mac**: Go to the [Python Downloads Page](https://www.python.org/downloads/) and download the installer for your operating system.
    - **Note**: Ensure that you check the box that says "Add Python to PATH" during the installation.
  
2. **Linux**: Python is usually pre-installed. If not, you can install it using the package manager. For Ubuntu, you can use:
    ```bash
    sudo apt-get install python3
    ```

#### Step 2: Verify Python Installation

Open a command prompt or terminal and run:
```bash
python --version
```
or
```bash
python3 --version
```
You should see the Python version if it's installed correctly.

#### Step 3: Install Git

1. Download and install Git from [Git Downloads Page](https://git-scm.com/downloads).
  
#### Step 4: Clone The Repository

1. Open command prompt or terminal.
2. Navigate to the folder where you want to clone the repository.
    ```bash
    cd path/to/folder
    ```
3. Run the following Git command:
    ```bash
    git clone https://github.com/vishnu-pradeep95/akshay_music_portfolio.git
    ```

#### Step 5: Install Flask (Python Library)

1. Navigate to the cloned repository folder:
    ```bash
    cd your-repository-name
    ```

2. Run:
    ```bash
    pip install Flask
    ```
   or
    ```bash
    pip3 install Flask
    ```

---

### Running the Project:

#### Step 1: Navigate to Project Folder in the command prompt

```bash
cd /path/to/your/directory
```

Make sure you're in the folder that contains `backend.py`.

#### Step 2: Run The Flask App (python script backend.py)

Run the following command in your terminal:
```bash
python backend.py
```
or
```bash
python3 backend.py
```
You should see output saying that the server is running. It will give you a URL, usually it's `http://127.0.0.1:5000/`.

#### Step 3: Access The Web Page

1. Open your web browser.
2. Go to `http://127.0.0.1:5000/portfolio`.

You should see your portfolio web page!

---

### Troubleshooting:

1. If you get a "command not found" error for Python or Pip, make sure they are correctly installed and added to your PATH.

2. If the `http://127.0.0.1:5000/portfolio` URL doesn't work, make sure the Flask app is still running in your terminal.

---

Feel free to share this guide with anyone who wants to run your project.
