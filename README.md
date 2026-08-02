# CRM Project Python

A simple console-based Customer Relationship Management (CRM) application built with Python. It lets you manage customer records and their contact persons through a basic menu-driven interface.

## Features

- Add new customers
- Update customer information
- Delete customer records
- View customers
- Add and update contact persons for each customer
- Store data in a MySQL database

## Project Structure

- `main.py` - entry point of the application
- `crm_ui.py` - user interface and menu handling
- `customer_manager.py` - business logic for customer and contact operations
- `customer.py` - customer model
- `contact_person.py` - contact person model
- `database.py` - database connection and SQL operations

## Requirements

Make sure you have the following installed:

- Python 3
- MySQL Server
- Python package: `mysql-connector-python`

Install the Python package with:

```bash
pip install mysql-connector-python
```

## Database Setup

Create a MySQL database named `crm_project` and the required tables.

```sql
CREATE DATABASE crm_project;

USE crm_project;

CREATE TABLE company_name (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    mail VARCHAR(100),
    location VARCHAR(100),
    phone VARCHAR(20),
    website VARCHAR(100),
    note TEXT
);

CREATE TABLE contact_person (
    contact_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    name VARCHAR(100),
    designation VARCHAR(100),
    phone VARCHAR(20),
    mail VARCHAR(100),
    FOREIGN KEY (customer_id) REFERENCES company_name(customer_id)
);
```

## Configuration

The database connection details are currently set in `database.py`.
If your MySQL username/password/database name are different, update them there before running the app.

## How to Run

From the project folder, run:

```bash
python main.py
```

You will see a menu with options like:

- Add New Customer
- Update Customer
- Delete Customer
- View Customers
- Exit

## Notes

This project is a beginner-friendly CRM example and is mainly designed for learning and practice. It uses a terminal-based interface rather than a web or desktop GUI.
