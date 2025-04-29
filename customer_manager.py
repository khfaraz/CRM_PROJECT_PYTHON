'''
from customer import Customer
from contact_person import ContactPerson

class CustomerManager:
    def __init__(self):
        self.customer_list = []
        self.customer_id = 0

    def addCustomer(self, name, mail, location, phone, site, note):
        self.customer_id += 1
        customer = Customer(name, mail, location, phone, note, site, self.customer_id)
        self.customer_list.append(customer)

    def addContact(self, customer_id, name, designation, phone, mail):
        if 0 < customer_id <= len(self.customer_list):
            contact = ContactPerson(name, phone, mail, designation)
            self.customer_list[customer_id - 1].addContactPerson(contact)

    def updateCustomerInfo(self, id, name, location, mail, phone, site, note):
        if 0 < id <= len(self.customer_list):
            customer = self.customer_list[id - 1]
            customer.setName(name)
            customer.setLocation(location)
            customer.setMail(mail)
            customer.setPhone(phone)
            customer.setSite(site)
            customer.setNote(note)


    def updateContactPersonInfo(self, customer_id, old_phone, name, designation, phone, mail):
        if 0 < customer_id <= len(self.customer_list):
            contacts = self.customer_list[customer_id - 1].getContactPersonsRef()
            for person in contacts:
                if person.getNumber() == old_phone:
                    person.setName(name)
                    person.setDesignation(designation)
                    person.setNumber(phone)
                    person.setMail(mail)
                    print("Contact updated successfully!")
                    return
            print("Contact person not found!")

    def deleteUser(self, id):
        if 0 < id <= len(self.customer_list):
            customer = self.customer_list[id - 1]
            customer.clearContactPerson()
            customer.setName("")
            customer.setMail("")
            customer.setLocation("")
            customer.setPhone("")
            customer.setSite("")
            customer.setNote("")

    def getAllCustomers(self):
        return self.customer_list

    def getCustomerId(self):
        return self.customer_id
'''

from database import Database

class CustomerManager:
    def __init__(self):
        self.db = Database(
            host="localhost",
            user="root",
            password="fron@ture",
            database="crm_project"
        )

    def addCustomer(self, name, mail, location, phone, site, note):
        customer_id = self.db.insertCustomer(name, mail, location, phone, site, note)
        return customer_id

    def addContact(self, customer_id, name, designation, phone, mail):
        self.db.insertContact(customer_id, name, designation, phone, mail)

    def updateCustomerInfo(self, customer_id, name, location, mail, phone, site, note):
        self.db.modifyCustomer(customer_id, name, location, mail, phone, site, note)

    def updateContactPersonInfo(self, customer_id, old_phone, name, designation, phone, mail):
        self.db.modifyContactPerson(customer_id, old_phone, name, designation, phone, mail)

    def deleteUser(self, customer_id):
        self.db.deleteUserDb(customer_id)

    def getAllCustomers(self):
        self.db.fetch_all_customer()

    def closeConnection(self):
        self.db.close()
