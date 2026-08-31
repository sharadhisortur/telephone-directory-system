# ☎️ Telephone Directory Maintenance System

A console-based **Telephone Directory Maintenance System** developed in Python to manage departments, employees, telephone numbers, and telephone enquiries using text files for persistent data storage.

## 📌 Project Overview

The Telephone Directory Maintenance System is a menu-driven Python application designed to maintain employee and telephone directory information.

The system allows users to:

* Add and manage departments
* Add and manage employees
* Allocate telephone numbers based on departments
* Search telephone details by employee name
* Search telephone details by telephone number
* Store and retrieve data using text files
* Validate user inputs according to the given project specifications

The project demonstrates the use of **Python fundamentals, file handling, functions, dictionaries, loops, conditional statements, validation, and menu-driven programming**.

---

## ✨ Features

### 🏢 Department Code Maintenance

* Add new departments
* Automatically generate department codes
* Department codes start from `1000`
* Automatically increment department codes for new departments
* Prevent duplicate department names
* Department name comparison is case-insensitive
* Department names are limited to 15 characters
* View all departments in tabular format

### 👨‍💼 Employee Master Maintenance

* Add new employees
* Automatically generate employee IDs
* Employee IDs start from `1000`
* Automatically increment employee IDs
* Employee names are limited to 25 characters
* Select departments from existing department codes
* Automatically retrieve the corresponding department name
* Validate department codes
* Location is limited to 5 characters
* View all employee records in tabular format

### ☎️ Telephone Directory Maintenance

* Add telephone numbers for existing employees
* Validate employee IDs
* Automatically retrieve employee department and location
* Generate telephone numbers based on department codes
* Telephone numbers follow the format:

```text
Department Code + 3-digit sequential number
```

Example:

```text
1000 + 001 = 1000001
1000 + 002 = 1000002
1001 + 001 = 1001001
```

### 🔎 Telephone Enquiry

#### Enquiry by Employee Name

* Search using employee name
* Case-insensitive name matching
* Display all matching telephone records
* Display an error if the employee name does not exist

#### Enquiry by Telephone Number

* Search using telephone number
* Validate whether the number exists
* Display employee and telephone details
* Display an error if the number does not exist

### 🔐 Login

* User authentication through Employee/User ID
* Valid User ID opens the Main Menu
* Invalid User ID displays:

```text
Login Denied
```

and exits the application.

---

## 🛠️ Technologies Used

| Technology     | Purpose                                    |
| -------------- | ------------------------------------------ |
| **Python**     | Application development                    |
| **VS Code**    | Development environment                    |
| **Text Files** | Persistent data storage                    |
| **Git**        | Version control                            |
| **GitHub**     | Project repository and source-code hosting |

---

## 📂 Project Structure

```text
TelephoneDirectory/
│
├── telephone_directory.py
├── dept.txt
├── emp.txt
├── tel.txt
└── README.md
```

### `telephone_directory.py`

Contains the complete Python implementation of the Telephone Directory Maintenance System.

### `dept.txt`

Stores department information.

Format:

```text
DepartmentCode|DepartmentName
```

Example:

```text
1000|CSE
1001|ISE
1002|ECE
```

### `emp.txt`

Stores employee information.

Format:

```text
EmployeeID|EmployeeName|DepartmentCode|DepartmentName|Location
```

Example:

```text
1000|Sharadhi|1000|CSE|DWD
1001|Rahul|1001|ISE|BLR
```

### `tel.txt`

Stores telephone directory information.

Format:

```text
TelephoneNumber|EmployeeID|EmployeeName|DepartmentCode|DepartmentName|Location
```

Example:

```text
1000001|1000|Sharadhi|1000|CSE|DWD
1001001|1001|Rahul|1001|ISE|BLR
```

---

## 🚀 Getting Started

### Prerequisites

Make sure Python is installed on your system.

Check the Python version:

```bash
python --version
```

or on Windows:

```bash
py --version
```

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/TelephoneDirectory.git
```

### 2. Navigate to the project directory

```bash
cd TelephoneDirectory
```

### 3. Run the application

```bash
python telephone_directory.py
```

On Windows, you can also use:

```bash
py telephone_directory.py
```

---

## 🔑 Login

The current implementation uses:

```python
VALID_USER_ID = "1000"
```

Enter:

```text
1000
```

when prompted for the User ID.

The `VALID_USER_ID` value can be changed in the Python source code according to the required project configuration.

---

## 🖥️ Main Menu

After successful login, the application displays:

```text
=======================================================
                    MAIN MENU
=======================================================

1. Department Code Maintenance
2. Employee Master Maintenance
3. Telephone Directory Maintenance
4. Telephone Enquiry
5. Exit
```

Each option opens its corresponding maintenance or enquiry module.

---

## 💾 Data Storage

The application uses three text files as a simple persistent data store:

```text
dept.txt
emp.txt
tel.txt
```

The files are automatically created when the program is run if they do not already exist.

All records are stored using the pipe (`|`) character as a delimiter.

This allows the application to preserve department, employee, and telephone information even after the program is closed.

---

## 🧪 Validation

The application includes validation for:

* Empty mandatory fields
* Department name length
* Duplicate department names
* Employee name length
* Location length
* Valid department codes
* Valid employee IDs
* Valid telephone numbers
* Case-insensitive department name comparison
* Case-insensitive employee name enquiry
* Valid `Y/N` responses
* Login authentication

---

## 📚 Concepts Demonstrated

This project demonstrates several fundamental programming concepts:

* Variables and data types
* Conditional statements
* Loops
* Functions
* Lists
* Dictionaries
* String manipulation
* File handling
* Reading and writing text files
* Input validation
* Searching
* Automatic ID generation
* Menu-driven programming
* Modular program design

---

## 🔄 Application Flow

```text
                    ┌───────────────┐
                    │     LOGIN     │
                    └───────┬───────┘
                            │
                  ┌─────────▼─────────┐
                  │    MAIN MENU      │
                  └─────────┬─────────┘
                            │
       ┌────────────────────┼────────────────────┐
       │                    │                    │
       ▼                    ▼                    ▼
 Department             Employee             Telephone
 Maintenance           Maintenance          Maintenance
       │                    │                    │
       ▼                    ▼                    ▼
  dept.txt              emp.txt              tel.txt
       │                    │                    │
       └────────────────────┼────────────────────┘
                            │
                            ▼
                   Telephone Enquiry
                            │
                    ┌───────┴───────┐
                    ▼               ▼
              By Employee       By Telephone
                  Name              Number
```

---

## 🎯 Project Objectives

The main objectives of this project are to:

1. Develop a functional menu-driven application using Python.
2. Implement persistent data storage using text files.
3. Automate department and employee ID generation.
4. Implement validation according to specified requirements.
5. Establish relationships between departments, employees, and telephone numbers.
6. Provide efficient searching and enquiry functionality.
7. Apply fundamental programming concepts to a practical management system.

---

## 👩‍💻 Author

**Sharadhi Sortur**

CSE Undergraduate Student
SDMCET Dharwad

---

## 📄 License

This project was developed as an academic programming project.

It is intended primarily for educational and learning purposes.
