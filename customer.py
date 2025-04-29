class Customer:
    def __init__(self, name, mail, location, phone, note, website, id):
        self.customerName = name
        self.customerMail = mail
        self.customerLocation = location
        self.customerPhone = phone
        self.customerNote = note
        self.customerWebsite = website
        self.customerId = id
        self.contactPerson = []

    def setName(self, name):
        self.customerName = name

    def setPhone(self, phone):
        self.customerPhone = phone

    def setMail(self, mail):
        self.customerMail = mail

    def setSite(self, site):
        self.customerWebsite = site

    def setNote(self, note):
        self.customerNote = note

    def setLocation(self, location):
        self.customerLocation = location

    def getId(self):
        return self.customerId

    def getName(self):
        return self.customerName

    def getMail(self):
        return self.customerMail

    def getLocation(self):
        return self.customerLocation

    def getPhone(self):
        return self.customerPhone

    def getWebsite(self):
        return self.customerWebsite

    def getNote(self):
        return self.customerNote

    def addContactPerson(self, person):
        self.contactPerson.append(person)

    def clearContactPerson(self):
        self.contactPerson.clear()

    def getContactPersonsRef(self):
        return self.contactPerson

    def getContactPersonsCopy(self):
        return self.contactPerson.copy()
