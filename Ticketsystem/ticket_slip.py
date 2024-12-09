import sqlite3
import time
from datetime import datetime

# Creating database connection
conn = sqlite3.connect("Ticket_Records.db")
c = conn.cursor()

# current time
t = time.localtime()
exit_time = time.strftime("%H:%M:%S", t)

# Slip
def getslip(number):
    c.execute(f"SELECT * FROM vehicle WHERE phone={number}")
    rows = c.fetchall()
    for row in rows:
        name = row[1]
        phone = row[2]
        vehicle_no = row[3]
        vehicle_type = row[6]
        entry_time_str = row[4]  # Assuming entry time is in a string format (HH:MM:SS)

        # Convert entry time and exit time to datetime objects for proper comparison
        entry_time = datetime.strptime(entry_time_str, "%H:%M:%S")
        exit_time_obj = datetime.strptime(exit_time, "%H:%M:%S")

        # Calculate the time difference in seconds
        time_diff = exit_time_obj - entry_time
        total_seconds = time_diff.total_seconds()

        # Convert seconds to minutes (total minutes as a single variable)
        total_minutes = total_seconds // 60
        hours = total_minutes // 60
        minutes = total_minutes % 60
        seconds = total_seconds % 60

        # Fare cost
        if vehicle_type=='Two_Wheeler':
            fare=10
            addditional_fare=5
        else:
           fare=20
           addditional_fare=10
        if hours<=1:
             total_fare=fare
        else:
             total_fare=fare+addditional_fare
    
        c.execute(f"Update vehicle set total_price={total_fare} where phone={number}")
        conn.commit()

        # Print slip with time spent
        print(f"<<<<<<<<<<<<<<<<<<<<<<<<< SLIP >>>>>>>>>>>>>>>>>>>>>>>>>\n\n"
              f"Name: {name}\nPhone: {phone}\nVehicle Number: {vehicle_no}\n"
              f"Vehicle Type: {vehicle_type}\nTime Spent: {int(hours)}:{int(minutes)}:{int(seconds)} \nTotal_fare={total_fare}")

# User input and processing
num = int(input("Enter phone number: "))
getslip(num)




