from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('DataBase')
root.geometry("450x500")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')
# Create cursor (The cursor goes and does everything for you)
c = conn.cursor()

# Create Table (We use triple quotation marks so we can type out multiple lines)
# Databases normally have heaps of data types but sqlite only has 5 which are:
# text
# integers
# real(decimal numbers, doubles, floats)
# null
# blob (image files, video files and stuff like that)


# This creates the Tables
# It is commented out because we only use it once
# c.execute("""CREATE TABLE addresses (
#    first_name text,
#    last_name text,
#    address text,
#    city text,
#    state text,
#    postcode integer
# )""")

# Create Edit Function to Update a Record
def update():
	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor (The cursor goes and does everything for you)
	c = conn.cursor()

	record_id = delete_box.get()

	c.execute("""UPDATE addresses SET
		first_name = :first,
		last_name = :last,
		address = :address,
		city = :city,
		state = :state,
		postcode = :postcode

		WHERE oid = :oid""",
		{
		'first': f_name_editor.get(),
		'last': l_name_editor.get(),
		'address': address_editor.get(),
		'city': city_editor.get(),
		'state': state_editor.get(),
		'postcode': postcode_editor.get(),
		'oid': record_id
		})

	# Commit Changes
	conn.commit()
	# Close Connection
	conn.close()

	editor.destroy()


def edit():
	global editor
	editor = Tk()
	editor.title('Update A Record')
	editor.geometry("450x240")

	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor (The cursor goes and does everything for you)
	c = conn.cursor()

	record_id = delete_box.get()
	# Query the Database
	c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
	records = c.fetchall()

	# Create Global Variables for text box names
	global f_name_editor
	global l_name_editor
	global address_editor
	global city_editor
	global state_editor
	global postcode_editor


	# Create Text Boxes
	f_name_editor = Entry(editor, width=30)
	f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
	l_name_editor = Entry(editor, width=30)
	l_name_editor.grid(row=1, column=1, padx=20)
	address_editor = Entry(editor, width=30)
	address_editor.grid(row=2, column=1, padx=20)
	city_editor = Entry(editor, width=30)
	city_editor.grid(row=3, column=1, padx=20)
	state_editor = Entry(editor, width=30)
	state_editor.grid(row=4, column=1, padx=20)
	postcode_editor = Entry(editor, width=30)
	postcode_editor.grid(row=5, column=1, padx=20)

	# Create Text Box Labels
	f_name_label_editor = Label(editor, text="First Name")
	f_name_label_editor.grid(row=0, column=0, padx=20, pady=(10, 0))
	l_name_label_editor = Label(editor, text="Last Name")
	l_name_label_editor.grid(row=1, column=0)
	address_label_editor = Label(editor, text="Address")
	address_label_editor.grid(row=2, column=0)
	city_label_editor = Label(editor, text="City")
	city_label_editor.grid(row=3, column=0)
	state_label_editor = Label(editor, text="State")
	state_label_editor.grid(row=4, column=0)
	postcode_label_editor = Label(editor, text="Postcode")
	postcode_label_editor.grid(row=5, column=0)

	# Loop Thru Results
	for record in records:
		f_name_editor.insert(0, record[0])
		l_name_editor.insert(0, record[1])
		address_editor.insert(0, record[2])
		city_editor.insert(0, record[3])
		state_editor.insert(0, record[4])
		postcode_editor.insert(0, record[5])


	# Create a Save Button to Save Edited Records
	edit_btn = Button(editor, text="Save Record", command=update)
	edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=160)



# Create Function to Delete a Record
def delete():
	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor (The cursor goes and does everything for you)
	c = conn.cursor()

	record_id = delete_box.get()
	# Delete a Record
	c.execute("DELETE from addresses WHERE oid = " + record_id)
	delete_box.delete(0, END)


	# Commit Changes
	conn.commit()
	# Close Connection
	conn.close()


# Create Submit Function for Database
def submit():
	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor (The cursor goes and does everything for you)
	c = conn.cursor()

	# Insert into Table
	c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :postcode)",
		{
			'f_name': f_name.get(),
			'l_name': l_name.get(),
			'address': address.get(),
			'city': city.get(),
			'state': state.get(),
			'postcode': postcode.get()
		})

	# Commit Changes
	conn.commit()
	# Close Connection
	conn.close()

	# Clear the Text Boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	postcode.delete(0, END)


# Create query Function
def query():
	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor (The cursor goes and does everything for you)
	c = conn.cursor()

	# Query the Database
	c.execute("SELECT *, oid FROM addresses") # '*' means 'All' and 'oid' is the 'Primary Key'
	records = c.fetchall() # Also fetchone() or fetchmany(50)

	# print to Terminal
	# print(records)

	# Loop Through Results
	print_records = ''
	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

	query_label = Label(root, text=print_records)
	query_label.grid(row=12, column=0, columnspan=2)


	# Commit Changes
	conn.commit()

	# Close Connection
	conn.close()


# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
postcode = Entry(root, width=30)
postcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, padx=20, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
postcode_label = Label(root, text="Postcode")
postcode_label.grid(row=5, column=0)

select_box_label = Label(root, text="Select ID")
select_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# Create a Query Button (Show Records)
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=152)

# Create a Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=152)


# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=160)


# Commit Changes
conn.commit()

# Close Connection
conn.close()


root.mainloop()
