# Financial Transaction Recording System (Flask)

A simple Flask web application to create, view, edit, and delete
financial transactions.\
Built as part of a Flask web development assignment.

## Features

-   View all transactions
-   Add a new transaction
-   Edit an existing transaction
-   Delete a transaction
-   Simple HTML interface using Flask templates

## Tech Stack

-   Python 3
-   Flask
-   Jinja2 (template engine)

## Project Structure

    .
    ├── app.py
    ├── templates/
    │   ├── transactions.html
    │   ├── form.html
    │   ├── search.html
    │   └── edit.html
    ├── README.md
    └── .gitignore

## Setup Instructions (Mac with Conda)

### 1. Clone the repository

``` bash
git clone https://github.com/aghababaeiali/financial-transaction-recording-system.git
cd financial-transaction-recording-system
```

### 2. Create and activate the conda environment

``` bash
conda create -n flasklab python=3.11 -y
conda activate flasklab
```

### 3. Install dependencies

``` bash
conda install flask -y
```

### 4. Run the application

``` bash
python app.py
```

Open your browser and go to:

    http://127.0.0.1:5000

## How It Works

-   Transactions are stored in a Python list in memory.
-   Each transaction has:
    -   `id`
    -   `date`
    -   `amount`
-   The app supports full CRUD operations through Flask routes.

## Routes

  Route            Method      Description
  ---------------- ----------- -----------------------
  `/`              GET         Show all transactions
  `/add`           GET, POST   Add a new transaction
  `/edit/<id>`     GET, POST   Edit a transaction
  `/delete/<id>`   GET         Delete a transaction

## Notes

-   This app uses in-memory storage.
-   All transactions reset when the server restarts.
-   Intended for learning purposes.

## Author

Ali Aghababaei

## License

This project is for educational use.
