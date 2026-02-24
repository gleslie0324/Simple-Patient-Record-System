import sys
from patient_registry import PatientRegistry

MAIN_MENU = ("Welcome to the Simple Patient Record System (SPRS)\n"
              "--------------------------------------------------\n"
              "Please select one of the following options:\n"
              "\t 1. Run Application\n"
              "\t 2. Exit\n")

APP_MENU = ("Please select one of the following options:\n"
            "\t1. Register new patient\n"
            "\t2. Retrieve patient by ID\n"
            "\t3. Update patient name (ID cannot be changed)\n"
            "\t4. Delete patient by ID\n"
            "\t5. List all patients\n"
            "\t6. Go back to main\n"
            "\t7. Exit\n")

def get_menu_input(menu:str) -> str:
    '''
    Prints the menu and takes input for it

    Args:
        name (str) - patient's name

    Returns:
        option (str) - choice inputted by user
    '''
    print(menu)

    option = input("Your Choice: ").strip()

    return option

def run_application(registry:PatientRegistry):
    '''
    Runs the main Simple Patient Record System

    Args:
        registry (PatientRegistry) - class holding the data and methods for the program
    '''
    while True:
                
                print("-" * 50)
                app_input = get_menu_input(APP_MENU)
                print("-" * 50)

                # Exit the program
                if app_input == "7":
                    print("Exiting SPRS...")
                    sys.exit()
                # Register new patient
                elif app_input == "1":
                    name = input("Enter Pateint Name: ").strip()
                    pid = registry.register_patient(name)
                    print("Registered: ", pid)
                # Retrieve patient ID
                elif app_input == "2":
                    pid = input("Enter ID of Patient: ").strip()
                    print(registry.get_patient(pid))
                # Update patient name
                elif app_input == "3":
                    pid = input("Enter ID of Patient to be Changed: ").strip()
                    pid = registry.update_patient_name(pid)
                    print("Updated: ", pid)
                # Delete patient by ID
                elif app_input == "4":
                    pid = input("Enter ID of Patient to be Deleted: ").strip()
                    deleted = registry.delete_patient(pid)
                    if deleted:
                        print("Deletion of " + pid + " successful.")
                    else:
                        print("***ERROR*** - " + pid + " could not be deleted.")
                # List all patients
                elif app_input == "5":
                    print(registry.list_patients())
                # Go back to main
                elif app_input == "6":
                    break
                # Error catch for other input
                else:
                    print("***ERROR*** - Input must be a whole number between 1 and 7 inclusively.")

def main():
    '''Entry point of the program'''
    registry = PatientRegistry()
    while True:
        main_input = get_menu_input(MAIN_MENU)
        print("-" * 50)
        # Exit the program
        if main_input == "2":
            print("Exiting SPRS...")
            sys.exit()
        # Run the SPRS
        elif main_input == "1":
            run_application(registry)    
        # Error catch for other input
        else:
            print("***ERROR*** - Input must be 1 or 2.")

if __name__ == "__main__":
    main()