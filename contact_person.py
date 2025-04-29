class ContactPerson:
    def __init__(self, name, number, mail, designation):
        self.personName = name
        self.personNumber = number
        self.personMail = mail
        self.personDesignation = designation

    def setName(self, name):
        self.personName = name

    def setNumber(self, number):
        self.personNumber = number

    def setMail(self, mail):
        self.personMail = mail

    def setDesignation(self, designation):
        self.personDesignation = designation

    def getName(self):
        return self.personName

    def getNumber(self):
        return self.personNumber

    def getMail(self):
        return self.personMail

    def getDesignation(self):
        return self.personDesignation
