import mysql.connector

class Database:
    def __init__(self, host="localhost", user="your_username", password="your_password", database="your_database"):
       
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="fron@ture",
            database="crm_project"
        )
        self.cursor = self.connection.cursor()

    def insertCustomer(self, name, mail, location, phone, website, note):
        query = """
        INSERT INTO company_name (name, mail, location, phone, website, note)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (name, mail, location, phone, website, note)
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def insertContact(self, customer_id, name, designation, phone, mail):
        query = """
        INSERT INTO contact_person (customer_id, name, designation, phone, mail)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (customer_id, name, designation, phone, mail)
        self.cursor.execute(query, values)
        self.connection.commit()

    def modifyCustomer(self, customer_id, name, location, mail, phone, website, note):
        query = """
        UPDATE company_name
        SET name=%s, location=%s, mail=%s, phone=%s, website=%s, note=%s
        WHERE customer_id=%s
        """
        values = (name, location, mail, phone, website, note, customer_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def modifyContactPerson(self, customer_id, old_phone, name, designation, phone, mail):
        query = """
        UPDATE contact_person
        SET name=%s, designation=%s, phone=%s, mail=%s
        WHERE customer_id=%s AND phone=%s
        """
        values = (name, designation, phone, mail, customer_id, old_phone)
        self.cursor.execute(query, values)
        self.connection.commit()

    def removeUser(self, customer_id):
        query = "DELETE FROM company_name WHERE customer_id=%s"
        self.cursor.execute(query, (customer_id,))
        self.connection.commit()

    def fetch_all_customer(self):
        query = """
        SELECT 
            c.customer_id, c.name, c.mail, c.location, c.phone, c.website, c.note,
            cp.name, cp.designation, cp.phone, cp.mail
        FROM company_name c
        LEFT JOIN contact_person cp ON c.customer_id = cp.customer_id
        ORDER BY c.customer_id
        """
        self.cursor.execute(query)
    def close(self):
        self.cursor.close()
        self.connection.close()
