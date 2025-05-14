# Shell Skeleton
Skeleton app for shell-like programs. It takes and parses commands from the
console. These commands can be defined and customized in the commands 
package folder. The program also expects a custom context that is passed to the
commands on execution.

A simple use case might be a program that helps grading student exams based on 
Laravel and handed in via GitHub Classrooms. As an example, a little text-based
adventure is added.

## Features
The skeleton hase the following features:
- Basic structure to initialize and run the program. Just instantiate your own 
  context and pass it to the `framework.run()` function.
- Simple and extendable commands. Just add classes in the commands package folder.
- Default commands like 'help', 'undo' and 'quit' are present and customizable.
- Command line arguments and `.env` support built-in.

## Usage
### Step 0: Setup
1. Create a `.env` file using the `.env.example`. 
1. Install Python and Venv

### Step 1: run the app
When you use venv:
1. Activate venv using 
  - Windows: `.venv\Scripts\activate`
  - Linux: `source .venv/bin/activate`
1. When activated, you can install dependencies using `pip`:
  - For instance using the `requirements.txt` file: `pip install -r requirements.txt`
  - Or simply: `pip install <package-name>` (do NOT install globally)
1. Run the app: `python main.py`
  - You can do a dry-run by adding the `python main.py --pretend` switch
1. Deactivate when you're done: `deactivate` (Windows and Linux)
