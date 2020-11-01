# Inventory Management

### APP Info
Types of Employees
* Inventory Manager
* Quality Check Person
* Sales Manager
* IT Admin (Super User)

Permissions
* Quality Check Person and IT Admin can approve the Quality details of Inventory
* All these employees can CRUD the Inventory
* IT Admin can CRUD the whole employees
* Other employees can update their own details 

### API Info
* `/api/employees/`
    * This endpoint is the api root of employee data
    * This endpoint returns the url for handling the employees details
    * You can CRUD the employee details using that URLs

* `/api/inventory/`
    * This endpoint is the api root of inventory data
    * This endpoint returns the url for handling the inventory and it's category data
    * You can CRUD the inventory and it's category data using that URLs

### Steps for running the app
1. Clone the Repo
2. Create and activate the virtual environment using virtualenv (Optional)
3. Install the requirements using `pip install -r requirements.txt`
4. Move to the `InventoryManagement` folder
5. Create the superuser using `python manage.py createsuperuser`
6. Migrate the DB using below commands
    * `python manage.py makemigrations`
    * `python manage.py migrate`
7. Run the server using `python manage.py runserver`