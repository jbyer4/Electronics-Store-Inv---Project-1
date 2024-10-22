# ###################### SCROLL TO BELOW LINE 236 TO INPUT ARGUMENTS! ######################################
import sqlite3
import base64
import pickle
import os
from datetime import datetime
import csv


# Connecting to SQLITE
con = sqlite3.connect('item_data.db')
cur = con.cursor()

#Checking security!
def checkSecurity():
    if os.path.isfile("security.pkl"):
        with open('security.pkl', 'rb') as file:
            loaded = pickle.load(file)
            return loaded[1]
    else:
        print("Please create an admin account to manage inventory and add items by calling Admin.register!")
        return False
if not checkSecurity():
    print("Admin logged out. Please login by calling Admin.login!\n")




#Classes
#Note: Classes AddItem and Inventory are only available to an admin user. Please call Admin.register to create Admin account!
#Adds item to inventory, creating items table
class AddItem():
    autoAdd = True
    def __init__(self, id, name, category, desc, price, quantity):
        #Making sure that user is logged in!
        if not checkSecurity():
            print("Cannot use class. Login with Admin.login!")
            return

        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.desc = desc

        #Checking if id and table already exists
            #Please note: you cannot create object if ID is already taken!
        isIdTaken = None
        try:
            cur.execute("CREATE TABLE items(id, name, category, desc, price, quantity, sale)")
            print("No table found. Making table now!")
        except:
            pass
        cur.execute("SELECT id FROM items")
        ids = [row[0] for row in cur.fetchall()]
        if not ids:
            isIdTaken = False
        else:
            for id in ids:
                if id == self.id:
                    print("Error: ID already exists in inventory, cannot create object. Please change ID")
                    isIdTaken = True
                    self.id = None
                    break
                else:
                    isIdTaken = False

        if isIdTaken == False:

        #Inserting into table (if autoadd is true)
            if AddItem.autoAdd:

                #Inserting to table
                cur.execute(f"""
                    INSERT INTO items (id, name, category, desc, price, quantity, sale) VALUES
                        (?, ?, ?, ?, ?, ?, ?)
                    """, (self.id, self.name, self.category, self.desc, self.price, self.quantity, "N/A"))
                con.commit()
                cur.execute("SELECT id FROM items")
                ids = [row[0] for row in cur.fetchall()]
                print("Added ID number: " + str(self.id) + " to inventory!")

    @staticmethod
    def controlAutoAdd():
        #Making sure that user is logged in!
        if not checkSecurity():
            print("Cannot use class. Login with Admin.login!")
            return

        #Swaps autoAdd value, use only if you don't want objects to be automatically added to inventory!
        AddItem.autoAdd = not AddItem.autoAdd
        if AddItem.autoAdd:
            print("New items will now be auto added to inventory")
        else:
            print("New items will not be auto added to inventory")

    def addToInventory(self):
        #Making sure that user is logged in!
        if not checkSecurity():
            print("Cannot use class. Login with Admin.login!")
            return

        if self.id == None:
            print("Error: please change ID, ID from this object is likely already in inventory.\nUse (object name).id = (new value)")
        else:
            # Inserting to table
            cur.execute(f"""
                INSERT INTO items (id, name, category, desc, price, quantity, sale) VALUES
                    (?, ?, ?, ?, ?, ?, ?)
                """, (self.id, self.name, self.category, self.desc, self.price, self.quantity, "N/A"))
            con.commit()



# Manage current inventory (only relates to database, not class objects from AddItem class)
class Inventory():
    #Can use id or name to remove item from inventory
    @staticmethod
    def remove_item(id):
        #Making sure that user is logged in!
        if not checkSecurity():
            print("Cannot use class. Login with Admin.login!")
            return

        cur.execute("DELETE FROM items WHERE id = ?", (id,))
        con.commit()
        print("Item with ID " + str(id) + " succesfully removed!")

    @staticmethod
    def changeQuantity(id, newAmnt):
        #Making sure that user is logged in!
        if not checkSecurity():
            print("Cannot use class. Login with Admin.login!")
            return

        cur.execute("""
            UPDATE items
            SET quantity = ?
            WHERE id = ?
        """, (newAmnt, id))
        con.commit()
        print("Item quantity with ID " + str(id) + " changed to " + str(newAmnt) + "!")

    @staticmethod
    def addSale(id, amnt):
        #Making sure that user is logged in!
        if not checkSecurity():
            print("Cannot use class. Login with Admin.login!")
            return

        cur.execute("""
            UPDATE items
            SET sale = ?
            WHERE id = ?
        """, (amnt, id))
        print("Sale added to item with ID " + str(id))

    @staticmethod
    def removeSale(id):
        #Making sure that user is logged in!
        if not checkSecurity():
            print("Cannot use class. Login with Admin.login!")
            return

        cur.execute("""
            UPDATE items
            SET sale = ?
            WHERE id = ?
        """, ("N/A", id))
        print("Sale removed from item with ID " + str(id))


class Report():
    #Generates report of entire inventory
    @staticmethod
    def generate():

        path = "report.csv"
        with open(path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            cur.execute("SELECT * FROM items LIMIT 0")
            columns = tuple(description[0] for description in cur.description)
            writer.writerow(columns)
            cur.execute("SELECT * FROM items")
            for row in cur.fetchall():
                writer.writerow(row)

            currentTime = datetime.now()
            time = ("Generated on " + str(currentTime.date()), "at " + str(currentTime.time()))
            writer.writerow((""))
            writer.writerow(time)


class Admin():
    @staticmethod
    def register(password):
        #Checking if security.pkl exists
        if os.path.isfile("security.pkl"):
            print("Admin has already been created. Please login by calling Admin.login!")
        else:
            password = base64.b64encode(password.encode("utf-8"))
            data = [password, False]
            with open('security.pkl', 'wb') as file:
                pickle.dump(data, file)
                print("Admin created successfully. Please login with Admin.login!")

    @staticmethod
    def login(password):
        #Checking if security.pkl exists
        if os.path.isfile("security.pkl"):
            with open('security.pkl', 'rb') as file:
                loaded = pickle.load(file)
                if (base64.b64decode(loaded[0]).decode("utf-8")) == (password):
                    loaded[1] = True
                    with open('security.pkl', 'wb') as file:
                        pickle.dump(loaded, file)
                        print("Successfully logged in!!")
                else:
                    print("Error: password incorrect. Please try again!")
        else:
            print("Error: no admin account found. Please call Admin.register!")

    @staticmethod
    def logout():
        if os.path.isfile("security.pkl"):
            with open('security.pkl', 'rb') as file:
                loaded = pickle.load(file)
                with open('security.pkl', 'wb') as file:
                    loaded[1] = False
                    pickle.dump(loaded, file)
                    print("Successfully logged out!!")
        else:
            print("Error: please create admin account first by calling Admin.register!")

print("Welcome! Type exit to close program!\n\n")

while True:
    userinput = input()
    if userinput.strip().lower() == "exit":
        break
    else:
        try:
            exec(userinput)
        except Exception as e:
            print(e)


# ############################ INPUTS GO BELOW THIS LINE ##################################### #

