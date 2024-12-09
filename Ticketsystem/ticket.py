import sqlite3
import time

# Creating database connection
conn = sqlite3.connect("Ticket_Records.db")
c = conn.cursor()

# Creating table
c.execute('''CREATE TABLE IF NOT EXISTS vehicle(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          username TEXT,
          phone INTEGER,
          vehicle_number TEXT,
          entry_time DATE,
          total_price INTEGER,
          vehicle_type TEXT )
''')
conn.commit()

# Functions
def create_user(username, phone, vehicle_number, entry_time, vehicle_type, total_price):
    c.execute("INSERT INTO vehicle(username, phone, vehicle_number, entry_time, vehicle_type, total_price) VALUES (?, ?, ?, ?, ?, ?)", 
              (username, phone, vehicle_number, entry_time, vehicle_type, total_price))
    conn.commit()

def read_user():
    c.execute("SELECT * FROM vehicle")
    rows = c.fetchall()
    for row in rows:
        print(row)

# Entry part
try:
    username = input("Enter name: ")
except:
    print("You have entered some other characters")

phone = int(input("Enter phone number: "))
vehicle_number = input("Enter vehicle number: ")
vehicle_type = int(input("Choose vehicle type \n 1. Two_Wheeler \n 2. Four_Wheeler\n"))
if vehicle_type == 1:
    vehicle = "Two_Wheeler"
elif vehicle_type == 2:
    vehicle = "Four_Wheeler"
else:
    print("Invalid option")
    vehicle = None



# Get the current time
t = time.localtime()
entry_time = time.strftime("%H:%M:%S", t)
total_price=0

if vehicle:
    create_user(username, phone, vehicle_number, entry_time, vehicle, total_price)

# # Slip
# def get_slip():
#     c.execute("SELECT * FROM vehicle")
#     rows = c.fetchall()
#     for row in rows:
#         print(row)

# # Example usage
# get_slip()
