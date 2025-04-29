from customer_manager import CustomerManager
from crm_ui import CRM_UI

def main():
    manager = CustomerManager()
    ui = CRM_UI(manager)

    while True:
        print("\n==== CUSTOMER MANAGEMENT MENU ====")
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. View Customers")
        print("0. Exit")


        option = int(input("Enter option: "))

        if option == 1:
            ui.addCustomerUI()
        elif option == 2:
            ui.updateCustomerUI()
        elif option == 3:
            ui.deleteCustomerUI()
        elif option == 4:
            ui.displayCustomersUI()
        elif option == 0:
            print("Banga Baltu More nai xD")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
