# Electronics Store Inventory Python Module
### Project 1 for Data Structures by Jared Byer

Welcome! This project allows the user to create and manage an inventory designed for an electronics store.
There are many features included in this project, such as:
  - Creating inventory table and automatically adding new items to table
  - Automatically storing variables and table with SQLITE3 and pickle
  - Generating report at any time, using SQLITE3 table to CSV conversion
    - Note: Generated report uses .csv, allowing easy conversion to excel
  - Auto-adding items to inventory may be disabled, allowing user to edit AddItem() class objects and add to inventory later
  - Simple security system utilizing base64 encoding, preventing unauthorized access to delicate inventory table
    - Note: Security system has flaws which will be discussed later

This project includes several files, including main.py, main-example.py, and report.csv. Only main.py is necessary to run, as main-example.py and report.csv are examples of the project in use. Main.py will automatically generate security.pkl and item_data.db, where important information is stored. Do not edit, remove or move these files.

*To view structure of code, please view main.py, which contains many comments for ease of reading.*

## How to create your own electronic store inventory:
*Note: Basic understanding of python is useful to correctly operating main.py.*

#### Step 1: Open and run main.py
  - Download main.py from the project's directory
  - Run main.py, ensuring that item_data.db was added within main.py's           directory.
    - Note: Optionally, the user may edit main.py with an IDE instead. In          this case, be sure to write inputs below line 250, and commenting out        the "While True" statement allowing user inputs.

#### Step 2: Create/Log-in to admin account
  - As a security measure, to prevent unwelcome access to crucial inventory      information, the classes AddItem() and Inventory() are automatically         protected and require a logged-in admin to access.
  - If this is the first time running main.py:
      - *Warnings may appear at the top of the terminal, explaining that the         admin is not logged in. This is expected* 
      - Type 'Admin.register("password")', replacing password with a string         value of a secure password.
        - Ensure that security.pkl was added within main.py's directory.
      - Type 'Admin.login("password")', replacing password with the password         used in the previous step.
        
  - If this is not the first time running main.py:
    - Login using 'Admin.login("password")', if not logged in.
        
  - Note:
     - If password is forgotten, simply delete security.pkl and create a new      admin account
     - Security vulnerabilities exist within the security class. To reduce         risk of attacks, it is reccomended to change privilages of                   security.pkl so it cannot be deleted.

#### Step 3: Use AddItem() class to add items to inventory.
  - Type 'AddItem(id, "name", "category", "desc", price, quantiy)',             replacing:
    - id with a unique integer (int) that was not used for another item
    - name, category, and desc with a string
    - price and quantity with an int or float (decimal value)
  *Example: AddItem(1, "laptop", "computers", "Microsoft Surface Pro 2019",     999.95, 11)*

  - Continue this process for all items to add! Note: more items       can     be added at any point after this step.

  - Optionally:
      - The user may opt to temporatily save an item as an AddItem class           object. This may be useful since items in inventory are much less            changeable. Note: These objects do not save when closing program.
      - To achieve this, simply use 'myObject = AddItem(...)' replacing             myObject with a unique string identifying the object, and ... with           the usual paramters of AddItem().
        
      - To edit object values, simply set the paramter to a new value:
        - Example: myObject.name = "Computer"

      - The user may call controlAutoAdd() to enable or disable auto adding
        an object to the inventory, so it can be added later. To add an              object later, simply call myObject.addToInventory(), replacing               myObject with the name of your object.


#### Step 4: Manage current inventory table
  - The user can remove, change quanatity of items, and add and remove sales   once an item is added to the inventory.
    
  - To remove an item:
    - Type 'remove_item(id)', replacing id with the int value of the id of         the item you would like to remove. Note: This cannot be undone.

  - To update the quantity of an item:
    - Type 'changeQuantity(id, newAmnt)', replacing id with the int value of     the id of the item you want to change, and newAmnt with the updated          quantity value in int or float.

  - To add a sale to an item:
    - Type 'addSale(id, amnt)', replacing id with the int value of the id of       the item you want to change, and amnt with the int or float of the           sale value.

  - To remove a sale from an item:
    Type 'removeSale(id)', replacing id with the int value of the id of the      item you would like to remove.

#### Step 5: Generate a report of the inventory:
  - The user can generate a report of the inventory at any time. To do this,     type 'Report.generate()'. The file 'report.csv' should quickly appear        within main.py's directory.
  - For ease of reading, report.csv can be easily viewed within Microsoft       Excel or Google Sheets. Users may find that report.csv is easier to view     with these programs.

#### Step 6: Logout and close the program:
  - Type 'Admin.logout()'.
  - Close the program by typing 'exit'.


### My personal findings
  I enjoyed creating a electronic inventory management system within Python. I discovered the importance of object-oriented programming by utilizing objects and classes, and utilized different types of class methods, including static methods. One of the biggest challenges I faced when creating main.py was how to save the inventory table accross instances of the program. I originally had csv files in mind, but I quickly found that they were difficult because they do not allow editing of specific cells of a table. I learned how to use SQLITE3 to store the inventory as a table on a databse, which I found to be much easier then using a CSV to store and read data. Another challenge I faced was adding security to the program, as I wanted the password to be encoded from the user. Unfortunately, there are security vulnerabilites, because the user can run any line of code they choose, thus potentially navigating between the admin class. In the future, I plan to take steps to prevent this.
With these challenges, however, I learned a lot about Python coding. I learned how to use SQLITE3 tables and databases, and I learned how to encode strings in base64. Furthermore, I used the datetime module to generate a date and time when the user generates a report. I also learned how to use the pickle module to save the user's password and a boolean value detecting whether or not an admin is logged in.



