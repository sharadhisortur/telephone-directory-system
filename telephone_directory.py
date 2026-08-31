import os

# ============================================================
# TELEPHONE DIRECTORY MAINTENANCE SYSTEM
# ============================================================

DEPT_FILE = "dept.txt"
EMP_FILE = "emp.txt"
TEL_FILE = "tel.txt"

# Change this to the User ID allowed to log in
VALID_USER_ID = "1000"


# ============================================================
# COMMON FUNCTIONS
# ============================================================

def initialize_files():
    """Create the required text files if they do not exist."""
    for filename in [DEPT_FILE, EMP_FILE, TEL_FILE]:
        if not os.path.exists(filename):
            with open(filename, "w"):
                pass


def pause():
    """Wait for the user before continuing."""
    input("\nPress Enter to continue...")


def get_yes_no(message):
    """Accept only Y/y or N/n as input."""
    while True:
        choice = input(message).strip().lower()

        if choice in ["y", "n"]:
            return choice

        print("Invalid input. Please enter Y or N.")


# ============================================================
# DEPARTMENT FILE FUNCTIONS
# ============================================================

def read_departments():
    """
    Read department records from dept.txt.

    Format:
    DepartmentCode|DepartmentName
    """
    departments = []

    with open(DEPT_FILE, "r") as file:
        for line in file:
            line = line.strip()

            if line:
                data = line.split("|")

                if len(data) == 2:
                    departments.append({
                        "code": data[0],
                        "name": data[1]
                    })

    return departments


def save_department(code, name):
    """Save a department record to dept.txt."""
    with open(DEPT_FILE, "a") as file:
        file.write(f"{code}|{name}\n")


# ============================================================
# DEPARTMENT CODE MAINTENANCE
# ============================================================

def generate_department_code():
    """Generate the next 4-digit department code starting from 1000."""
    departments = read_departments()

    if not departments:
        return "1000"

    highest_code = max(int(department["code"]) for department in departments)
    return str(highest_code + 1)


def add_department():
    """Add one or more departments."""

    while True:
        print("\n========== ADD DEPARTMENT ==========")

        while True:
            department_name = input("Enter Department Name: ").strip()

            if department_name == "":
                print("Error: Department name is mandatory.")

            elif len(department_name) > 15:
                print("Error: Department name should not exceed 15 characters.")

            else:
                departments = read_departments()

                duplicate_found = any(
                    department["name"].lower() == department_name.lower()
                    for department in departments
                )

                if duplicate_found:
                    print("Error: Department name already exists.")
                else:
                    break

        department_code = generate_department_code()
        save_department(department_code, department_name)

        print("\nDepartment added successfully!")
        print("Generated Department Code:", department_code)

        choice = get_yes_no(
            "\nDo you want to add another department? (Y/N): "
        )

        if choice == "n":
            break


def view_departments():
    """Display all departments in tabular format."""
    departments = read_departments()

    print("\n========== ALL DEPARTMENTS ==========")

    if not departments:
        print("No departments found.")
        return

    print("-" * 45)
    print(f"{'DEPARTMENT CODE':<20}{'DEPARTMENT NAME':<20}")
    print("-" * 45)

    for department in departments:
        print(
            f"{department['code']:<20}"
            f"{department['name']:<20}"
        )

    print("-" * 45)


def department_menu():
    """Department Code Maintenance menu."""

    while True:
        print("\n========== DEPARTMENT CODE MAINTENANCE ==========")
        print("1. Add Department")
        print("2. View All Departments")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_department()

        elif choice == "2":
            view_departments()
            pause()

        elif choice == "3":
            break

        else:
            print("Error: Invalid choice.")
            pause()


# ============================================================
# EMPLOYEE FILE FUNCTIONS
# ============================================================

def read_employees():
    """
    Read employee records from emp.txt.

    Format:
    EmployeeID|EmployeeName|DepartmentCode|DepartmentName|Location
    """
    employees = []

    with open(EMP_FILE, "r") as file:
        for line in file:
            line = line.strip()

            if line:
                data = line.split("|")

                if len(data) == 5:
                    employees.append({
                        "id": data[0],
                        "name": data[1],
                        "department_code": data[2],
                        "department_name": data[3],
                        "location": data[4]
                    })

    return employees


def save_employee(employee):
    """Save an employee record to emp.txt."""
    with open(EMP_FILE, "a") as file:
        file.write(
            f"{employee['id']}|"
            f"{employee['name']}|"
            f"{employee['department_code']}|"
            f"{employee['department_name']}|"
            f"{employee['location']}\n"
        )


# ============================================================
# EMPLOYEE MASTER MAINTENANCE
# ============================================================

def generate_employee_id():
    """Generate the next 4-digit employee ID starting from 1000."""
    employees = read_employees()

    if not employees:
        return "1000"

    highest_id = max(int(employee["id"]) for employee in employees)
    return str(highest_id + 1)


def find_department(department_code):
    """Find and return a department using its code."""
    departments = read_departments()

    for department in departments:
        if department["code"] == department_code:
            return department

    return None


def add_employee():
    """Add one or more employees."""

    departments = read_departments()

    if not departments:
        print("\nError: No departments exist.")
        print("Please add a department first.")
        pause()
        return

    while True:
        print("\n========== ADD NEW EMPLOYEE ==========")

        # Employee name validation
        while True:
            employee_name = input("Enter Employee Name: ").strip()

            if employee_name == "":
                print("Error: Employee name is mandatory.")

            elif len(employee_name) > 25:
                print("Error: Employee name should not exceed 25 characters.")

            else:
                break

        # Employee ID generated automatically
        employee_id = generate_employee_id()
        print("Generated Employee ID:", employee_id)

        # Display available departments
        print("\nAvailable Departments:")
        view_departments()

        # Department selection
        while True:
            department_code = input("\nEnter Department Code: ").strip()

            department = find_department(department_code)

            if department is None:
                print("Error: Department Code does not exist.")
            else:
                department_name = department["name"]
                print("Department Name:", department_name)
                break

        # Location validation
        while True:
            location = input("Enter Location: ").strip()

            if location == "":
                print("Error: Location is mandatory.")

            elif len(location) > 5:
                print("Error: Location should not exceed 5 characters.")

            else:
                break

        employee = {
            "id": employee_id,
            "name": employee_name,
            "department_code": department_code,
            "department_name": department_name,
            "location": location
        }

        save_employee(employee)

        print("\nEmployee added successfully!")
        print("Employee ID:", employee_id)

        choice = get_yes_no(
            "\nDo you want to add another employee? (Y/N): "
        )

        if choice == "n":
            break


def view_employees():
    """Display all employees in tabular format."""
    employees = read_employees()

    print("\n========== ALL EMPLOYEES ==========")

    if not employees:
        print("No employees found.")
        return

    print("-" * 100)
    print(
        f"{'EMP ID':<10}"
        f"{'EMPLOYEE NAME':<27}"
        f"{'DEPT CODE':<12}"
        f"{'DEPT NAME':<20}"
        f"{'LOCATION':<10}"
    )
    print("-" * 100)

    for employee in employees:
        print(
            f"{employee['id']:<10}"
            f"{employee['name']:<27}"
            f"{employee['department_code']:<12}"
            f"{employee['department_name']:<20}"
            f"{employee['location']:<10}"
        )

    print("-" * 100)


def employee_menu():
    """Employee Master Maintenance menu."""

    while True:
        print("\n========== EMPLOYEE MASTER MAINTENANCE ==========")
        print("1. Add New Employee")
        print("2. View All Employees")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()
            pause()

        elif choice == "3":
            break

        else:
            print("Error: Invalid choice.")
            pause()


# ============================================================
# TELEPHONE FILE FUNCTIONS
# ============================================================

def read_telephones():
    """
    Read telephone records from tel.txt.

    Format:
    TelephoneNumber|EmployeeID|EmployeeName|DepartmentCode|
    DepartmentName|Location
    """
    telephones = []

    with open(TEL_FILE, "r") as file:
        for line in file:
            line = line.strip()

            if line:
                data = line.split("|")

                if len(data) == 6:
                    telephones.append({
                        "telephone_number": data[0],
                        "employee_id": data[1],
                        "employee_name": data[2],
                        "department_code": data[3],
                        "department_name": data[4],
                        "location": data[5]
                    })

    return telephones


def save_telephone(telephone):
    """Save a telephone record to tel.txt."""
    with open(TEL_FILE, "a") as file:
        file.write(
            f"{telephone['telephone_number']}|"
            f"{telephone['employee_id']}|"
            f"{telephone['employee_name']}|"
            f"{telephone['department_code']}|"
            f"{telephone['department_name']}|"
            f"{telephone['location']}\n"
        )


# ============================================================
# TELEPHONE DIRECTORY MAINTENANCE
# ============================================================

def find_employee(employee_id):
    """Find and return an employee using their Employee ID."""
    employees = read_employees()

    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    return None


def generate_telephone_number(department_code):
    """
    Generate a seven-digit telephone number.

    Format:
    4-digit Department Code + 3-digit sequential number.

    Example:
    1000 -> 1000001
    1000 -> 1000002
    1001 -> 1001001
    """
    telephones = read_telephones()
    sequences = []

    for telephone in telephones:
        if telephone["department_code"] == department_code:
            sequence = int(telephone["telephone_number"][-3:])
            sequences.append(sequence)

    if not sequences:
        next_sequence = 1
    else:
        next_sequence = max(sequences) + 1

    return department_code + str(next_sequence).zfill(3)


def add_telephone():
    """Allocate telephone numbers to existing employees."""

    employees = read_employees()

    if not employees:
        print("\nError: No employees exist.")
        print("Please add an employee first.")
        pause()
        return

    while True:
        print("\n========== ADD NEW TELEPHONE ==========")

        employee_id = input("Enter Employee ID: ").strip()

        if employee_id == "":
            print("Error: Employee ID is mandatory.")
        else:
            employee = find_employee(employee_id)

            if employee is None:
                print("Error: Employee ID does not exist.")

            else:
                # Details are fetched from Employee Master
                print("\nEmployee Name    :", employee["name"])
                print("Department Code  :", employee["department_code"])
                print("Department Name  :", employee["department_name"])
                print("Location         :", employee["location"])

                # Generate telephone number automatically
                telephone_number = generate_telephone_number(
                    employee["department_code"]
                )

                print("Telephone Number :", telephone_number)

                telephone = {
                    "telephone_number": telephone_number,
                    "employee_id": employee["id"],
                    "employee_name": employee["name"],
                    "department_code": employee["department_code"],
                    "department_name": employee["department_name"],
                    "location": employee["location"]
                }

                save_telephone(telephone)

                print("\nTelephone number allocated successfully!")

        choice = get_yes_no(
            "\nDo you want to add another telephone? (Y/N): "
        )

        if choice == "n":
            break


def telephone_maintenance_menu():
    """Telephone Directory Maintenance menu."""

    while True:
        print("\n========== TELEPHONE DIRECTORY MAINTENANCE ==========")
        print("1. Add New Telephone")
        print("2. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_telephone()

        elif choice == "2":
            break

        else:
            print("Error: Invalid choice.")
            pause()


# ============================================================
# TELEPHONE ENQUIRY
# ============================================================

def display_telephone_records(records):
    """Display telephone records in tabular format."""

    print("-" * 100)
    print(
        f"{'TELEPHONE':<15}"
        f"{'EMP ID':<10}"
        f"{'EMPLOYEE NAME':<27}"
        f"{'DEPT CODE':<12}"
        f"{'LOCATION':<10}"
    )
    print("-" * 100)

    for telephone in records:
        print(
            f"{telephone['telephone_number']:<15}"
            f"{telephone['employee_id']:<10}"
            f"{telephone['employee_name']:<27}"
            f"{telephone['department_code']:<12}"
            f"{telephone['location']:<10}"
        )

    print("-" * 100)


def enquiry_by_employee_name():
    """Search telephone records by employee name."""

    print("\n========== ENQUIRY BY EMPLOYEE NAME ==========")

    name = input("Enter Employee Name: ").strip()

    if name == "":
        print("Error: Employee name is mandatory.")
        return

    telephones = read_telephones()
    matching_records = []

    # Case-insensitive search
    for telephone in telephones:
        if telephone["employee_name"].lower() == name.lower():
            matching_records.append(telephone)

    if not matching_records:
        print("Error: Employee name does not exist.")
    else:
        print("\nTelephone Details:")
        display_telephone_records(matching_records)


def enquiry_by_telephone_number():
    """Search details using a telephone number."""

    print("\n========== ENQUIRY BY TELEPHONE NUMBER ==========")

    number = input("Enter Telephone Number: ").strip()

    if number == "":
        print("Error: Telephone number is mandatory.")
        return

    telephones = read_telephones()

    for telephone in telephones:
        if telephone["telephone_number"] == number:
            print("\nTelephone Details:")
            display_telephone_records([telephone])
            return

    print("Error: Telephone number does not exist.")


def telephone_enquiry_menu():
    """Telephone Enquiry menu."""

    while True:
        print("\n========== TELEPHONE ENQUIRY ==========")
        print("1. Enquiry by Employee Name")
        print("2. Enquiry by Telephone Number")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            enquiry_by_employee_name()
            pause()

        elif choice == "2":
            enquiry_by_telephone_number()
            pause()

        elif choice == "3":
            break

        else:
            print("Error: Invalid choice.")
            pause()


# ============================================================
# LOGIN
# ============================================================

def login():
    """Allow access only to the valid User ID."""

    print("=" * 55)
    print("    TELEPHONE DIRECTORY MAINTENANCE SYSTEM")
    print("=" * 55)

    user_id = input("\nEnter User ID: ").strip()

    if user_id == VALID_USER_ID:
        print("\nLogin Successful!")
        return True

    print("\nLogin Denied")
    return False


# ============================================================
# MAIN MENU
# ============================================================

def main_menu():
    """Display and control the main menu."""

    while True:
        print("\n" + "=" * 55)
        print("                    MAIN MENU")
        print("=" * 55)

        print("1. Department Code Maintenance")
        print("2. Employee Master Maintenance")
        print("3. Telephone Directory Maintenance")
        print("4. Telephone Enquiry")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            department_menu()

        elif choice == "2":
            employee_menu()

        elif choice == "3":
            telephone_maintenance_menu()

        elif choice == "4":
            telephone_enquiry_menu()

        elif choice == "5":
            print("\nThank you for using the Telephone Directory System!")
            break

        else:
            print("Error: Invalid choice.")
            pause()


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    initialize_files()

    if login():
        main_menu()