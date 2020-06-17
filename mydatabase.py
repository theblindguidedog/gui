from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('DataBase')
root.geometry("330x650")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')
# Create cursor (The cursor goes and does everything for you)
c = conn.cursor()


# Create Edit Function to Update a Record
def update_record():
	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor (The cursor goes and does everything for you)
	c = conn.cursor()

	record_id = select.get()

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


def edit_record():
	global editor
	editor = Tk()
	editor.title('Update A Record')
	editor.geometry("")

	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor (The cursor goes and does everything for you)
	c = conn.cursor()

	record_id = select.get()
	# Query the Database
	try:
		c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
		records = c.fetchall()
	except:
		pass

	# Create Global Variables for text box names
	global f_name_editor
	global l_name_editor
	global address_editor
	global city_editor
	global state_editor
	global postcode_editor

	# Create Text Boxes
	f_name_editor = Entry(editor, width=15)
	f_name_editor.grid(row=0, column=1, pady=(10, 0))
	l_name_editor = Entry(editor, width=15)
	l_name_editor.grid(row=1, column=1)
	address_editor = Entry(editor, width=15)
	address_editor.grid(row=2, column=1)
	city_editor = Entry(editor, width=15)
	city_editor.grid(row=3, column=1)
	state_editor = Entry(editor, width=15)
	state_editor.grid(row=4, column=1)
	postcode_editor = Entry(editor, width=15)
	postcode_editor.grid(row=5, column=1)

	# Create Text Box Labels
	f_name_label_editor = Label(editor, text="First Name")
	f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
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


	try:
		# Loop Thru Results
		for record in records:
			f_name_editor.insert(0, record[0])
			l_name_editor.insert(0, record[1])
			address_editor.insert(0, record[2])
			city_editor.insert(0, record[3])
			state_editor.insert(0, record[4])
			postcode_editor.insert(0, record[5])

			# Create a Save Button to Save Edited Records
			edit_btn = Button(editor, text="Update Record", command=update_record)
			edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10)
	except UnboundLocalError:
		pass

# Create Function to Delete a Record
def delete_record():
	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor (The cursor goes and does everything for you)
	c = conn.cursor()

	record_id = select.get()

	# Delete a Record
	c.execute("DELETE from addresses WHERE oid = " + record_id)
	select_window.delete(0, END)


	# Commit Changes
	conn.commit()
	# Close Connection
	conn.close()


# Create Submit Function for Database
def add_record():
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
	f_name.delete(0,END)
	l_name.delete(0,END)
	address.delete(0,END)
	city.delete(0,END)
	state.delete(0,END)
	postcode.delete(0,END)


# Create query Function New Window
def show_all_records():
	global all_data_records
	all_data_records = Tk()
	all_data_records.title('All Records')
	all_data_records.geometry("")

	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor (The cursor goes and does everything for you)
	c = conn.cursor()

	# Query the Database
	c.execute("SELECT *, oid FROM addresses") # '*' means 'All' and 'oid' is the 'Primary Key'
	records = c.fetchall() # Also fetchone() or fetchmany(50)

	# Loop Through Results
	print_records = ''
	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

	show_all_window = Label(all_data_records, text=print_records)
	show_all_window.grid(row=0, column=0, padx=20, pady=(10, 0))

	# Commit Changes
	conn.commit()

	# Close Connection
	conn.close()


# Create Text Boxes
f_name = Entry(root, width=20)
f_name.grid(row=1, column=0)
l_name = Entry(root, width=20)
l_name.grid(row=3, column=0, padx=20)
address = Entry(root, width=20)
address.grid(row=5, column=0, padx=20)
city = Entry(root, width=20)
city.grid(row=7, column=0, padx=20)
state = Entry(root, width=20)
state.grid(row=9, column=0, padx=20)
postcode = Entry(root, width=20)
postcode.grid(row=11, column=0, padx=20)

select = Entry(root, width=5)
select.grid(row=13, column=0)

# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, padx=20, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=2, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=4, column=0)
city_label = Label(root, text="City")
city_label.grid(row=6, column=0)
state_label = Label(root, text="State")
state_label.grid(row=8, column=0)
postcode_label = Label(root, text="Postcode")
postcode_label.grid(row=10, column=0)

select_window_label = Label(root, text="Select ID")
select_window_label.grid(row=12, column=0, padx=20, pady=(10, 0))

# Create Submit Button
add_record_btn = Button(root, text="Add Record", command=add_record)
add_record_btn.grid(row=14, column=0, padx=20, pady=(10, 0))

# Create an Edit Button
edit_record_btn = Button(root, text="Edit Record", command=edit_record)
edit_record_btn.grid(row=16, column=0, padx=20, pady=(10, 0))

# Create a Delete Button
delete_record_btn = Button(root, text="Delete Record", command=delete_record)
delete_record_btn.grid(row=17, column=0, padx=20, pady=(10, 0))

# Create a Query Button (Show Records)
show_all_records_btn = Button(root, text="Show All Records", command=show_all_records)
show_all_records_btn.grid(row=18, column=0, padx=20, pady=(10, 0))



# Commit Changes
conn.commit()

# Close Connection
conn.close()


root.mainloop()
