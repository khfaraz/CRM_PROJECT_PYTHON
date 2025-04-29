from customer_manager import CustomerManager

class CRM_UI:
    def __init__(self, manager: CustomerManager):
        self.manager = manager

    def addCustomerUI(self):
        print("----- ADD NEW CUSTOMER -----")
        name = input("Enter Company Name: ")
        mail = input("Enter Company Mail: ")
        location = input("Enter Company Location: ")
        phone = input("Enter Company Mobile: ")
        site = input("Enter Company Website: ")
        note = input("Enter Company Note: ")

        
        customer_id = self.manager.addCustomer(name, mail, location, phone, site, note)

        
        while True:
            self.addContactUI(customer_id)
            add_more = input("Add another contact person for this customer? (y/n): ")
            if add_more.lower() != 'y':
                break

    def addContactUI(self, customer_id):
        print("---------- Contact Person Info ---------")
        name = input("Enter Contact person name: ")
        designation = input("Enter Contact person designation: ")
        mail = input("Enter Contact person mail: ")
        phone = input("Enter Contact person phone: ")
        
        self.manager.addContact(customer_id, name, designation, phone, mail)

    def displayCustomersUI(self):
        #customers = self.manager.getAllCustomers()
        self.manager.getAllCustomers()

        """
        if not customers:
            print("No customers found!")
            return

        for customer in customers:
            print("\n=====> CUSTOMER INFORMATION <=======")
            print(f"Customer Id      : {customer.getId()}")
            print(f"Customer Name    : {customer.getName()}")
            print(f"Customer Mail    : {customer.getMail()}")
            print(f"Customer Location: {customer.getLocation()}")
            print(f"Customer Website : {customer.getWebsite()}")
            print(f"Customer Note    : {customer.getNote()}")

            contacts = customer.getContactPersonsCopy()
            if not contacts:
                print("  ---> No Contact Persons added! <---")
            else:
                for cp in contacts:
                    print("  ---> CONTACT PERSON <---")
                    print(f"  Name       : {cp.getName()}")
                    print(f"  Designation: {cp.getDesignation()}")
                    print(f"  Phone      : {cp.getNumber()}")
                    print(f"  Mail       : {cp.getMail()}")
                    print()
        """

    def updateCustomerUI(self):
        
        id = int(input("ENTER THE CUSTOMER ID: "))
        print("PRESS 1 TO UPDATE CUSTOMER INFORMATION")
        print("PRESS 2 TO UPDATE CONTACT PERSON INFORMATION")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.updateCustomerInfoUI(id)
        elif choice == '2':
            self.updateContactPersonInfoUI(id)
        else:
            print("Invalid choice!")

    def updateCustomerInfoUI(self, customer_id):
        print("---- UPDATE CUSTOMER INFO ----")
        name = input("Enter New Name: ")
        location = input("Enter New Location: ")
        mail = input("Enter New Mail: ")
        phone = input("Enter New Phone: ")
        site = input("Enter New Website: ")
        note = input("Enter New Note: ")
        
        
        self.manager.updateCustomerInfo(customer_id, name, location, mail, phone, site, note)
        print(f"Customer with ID {customer_id} updated successfully.")

    def updateContactPersonInfoUI(self, customer_id):
        print("---- UPDATE CONTACT PERSON INFO ----")
        existing_number = input("Enter Existing Contact Person Number: ")

        name = input("Enter New Contact Name: ")
        designation = input("Enter New Designation: ")
        phone = input("Enter New Phone Number: ")
        mail = input("Enter New Mail: ")

        
        self.manager.updateContactPersonInfo(customer_id, existing_number, name, designation, phone, mail)
        print(f"Contact person for customer {customer_id} updated successfully.")

    def deleteCustomerUI(self):
        try:
            id = int(input("Enter the Customer ID to delete: "))
            self.manager.deleteUser(id)
            print(f"Customer with ID {id} deleted successfully.")
        except ValueError:
            print("Invalid input! Customer ID must be an integer.")
