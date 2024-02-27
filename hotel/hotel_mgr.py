import sqlite3
con = sqlite3.connect('hotel.db')
cur = con.cursor()

initialization = input("Would you like to initialize the database? (Y/N) ")

if initialization.lower() == "y":
    # Set up ROOMS
    cur.execute("CREATE TABLE IF NOT EXISTS rooms (room_number INTEGER, status TEXT CHECK (status IN ('clean', 'dirty', 'ooo')), room_type TEXT CHECK (room_type IN ('K', 'QQ', 'KS', 'QQS', 'KH', 'QQH')), availability TEXT CHECK (availability IN ('vacant', 'occupied')))")

    rooms = [
        (201, 'clean', 'K', 'vacant'),
        (202, 'clean', 'K', 'vacant'),
        (203, 'dirty', 'K', 'occupied'), 
        (204, 'dirty', 'K', 'occupied'), 
        (205, 'dirty', 'QQ', 'vacant'), 
        (206, 'dirty', 'QQ', 'occupied'), 
        (207, 'clean', 'QQ', 'vacant'), 
        (208, 'clean', 'QQ', 'vacant'), 
        (209, 'clean', 'QQ', 'vacant'), 
        (210, 'dirty', 'QQ', 'occupied'), 
        (211, 'dirty', 'QQ', 'vacant'), 
        (212, 'dirty', 'QQ', 'occupied'), 
        (213, 'clean', 'KH', 'vacant'), 
        (214, 'clean', 'K', 'vacant'), 
        (215, 'dirty', 'K', 'vacant'), 
        (217, 'clean', 'K', 'vacant'), 
        (219, 'clean', 'K', 'vacant'), 
        (220, 'clean', 'KS', 'vacant'), 
        (221, 'ooo', 'QQ', 'vacant'), 
        (222, 'clean', 'QQ', 'vacant'), 
        (223, 'dirty', 'QQ', 'vacant'), 
        (224, 'dirty', 'QQ', 'vacant'), 
        (225, 'dirty', 'QQ', 'vacant'), 
        (226, 'dirty', 'QQ', 'occupied'), 
        (227, 'clean', 'QQ', 'vacant'), 
        (228, 'clean', 'QQ', 'vacant'), 
        (229, 'clean', 'K', 'vacant'), 
        (230, 'clean', 'K', 'vacant'), 
        (231, 'dirty', 'K', 'vacant'),
        (232, 'clean', 'K', 'vacant')
    ]

    for room in rooms:
        cur.execute("INSERT OR IGNORE INTO rooms VALUES (?, ?, ?, ?)", room)

    con.commit()


choice = 0
while choice != 5:
    print("Welcome to the Hotel Management System!")

    print("Select an option: ")
    print("1. Check In") 
    print("2. Check Out")
    print("3. View Rooms") 
    print("4. Clean Rooms")
    print("5. Exit")

    try:
        choice = int(input("> "))

    except:
        print("")

    else:
        if choice == 1: # Check In
            loop = True
            while loop == True:
                print("Here are the available rooms:")
                cur.execute("SELECT room_type, count(room_type) FROM rooms where status = 'clean' AND availability = 'vacant' ORDER BY room_type")
                room_choice = input("What type of room is wanted? \n1. K-King \n2. KH-King (Handicapped) \n3. KS-King Suite \n4. QQ-Double Queen \n5. QQH-Double Queen (Handicapped) \n6. QQS. Double Queen Suite\n")

                if room_choice == "1" or room_choice.upper() == "K":
                    room_choice = "K"
                    loop = False
                elif room_choice == "2" or room_choice.upper() == "KH":
                    room_choice = "KH"
                    loop = False
                elif room_choice == "3" or room_choice.upper() == "KS":
                    room_choice = "KS"
                    loop = False
                elif room_choice == "4" or room_choice.upper() == "QQ":
                    room_choice = "QQ"
                    loop = False
                elif room_choice == "5" or room_choice.upper() == "QQH":
                    room_choice = "QQH"
                    loop = False
                elif room_choice == "6" or room_choice.upper() == "QQS":
                    room_choice = "QQS"
                    loop = False
                else: 
                    loop = True
            
            # Pick an empty, clean room that matches what the guest wants.
            status = 'clean'
            availability = 'vacant'

            cur.execute("SELECT room_number FROM rooms WHERE status = ? AND room_type = ? AND availability = ? LIMIT 1", (status, room_choice, availability))
            room_number = cur.fetchone()

            if room_number: 
                room_number = room_number[0]

                status = 'dirty'
                availability = 'occupied'
                cur.execute("UPDATE rooms SET status = ?, availability = ? WHERE room_number = ?", (status, availability, room_number))

                print(f"The guest has been checked into {room_number}.")
                con.commit()
            
            else:
                print("Sorry, this type of room isn't available.")
            
            
        elif choice == 2: # Check Out
            print("Which room is checking out?")
            print("\nThese rooms are occupied: ")
            cur.execute("SELECT room_number FROM rooms WHERE availability = 'occupied' ORDER BY room_number ASC")
            occupied_rooms = cur.fetchall()
            for room in occupied_rooms:
                print(f"{room[0]}")
            try:
                room_no = int(input("Enter a room number: "))
            except ValueError:
                print("Sorry, that isn't a valid room number.")
            else:
                cur.execute("SELECT availability FROM rooms WHERE room_number = ?", (room_no,))
                room = cur.fetchone()
                if room and room[0] == 'occupied':
                    availability = 'vacant'
                    status = 'dirty'
                    cur.execute("UPDATE rooms SET availability = ?, status = ? WHERE room_number = ?", (availability, status, room_no,))
                    print(f"Room {room_no} has been checked out.")
                    con.commit()
                else:
                    print("Sorry, this room couldn't be checked out.")


        elif choice == 3: # View Rooms
            print("Vacant Rooms: ")
            cur.execute("SELECT room_number, room_type FROM rooms WHERE status = 'clean' and availability = 'vacant' ORDER BY room_number ASC")
            vacant_rooms = cur.fetchall()
            print(f"{vacant_rooms}")

            print("\nOccupied Rooms: ")
            cur.execute("SELECT room_number, room_type FROM rooms WHERE availability = 'occupied' ORDER BY room_number ASC")
            occupied_rooms = cur.fetchall()
            print(f"{occupied_rooms}")

            print("\nDirty Rooms:")
            cur.execute("SELECT room_number, room_type FROM rooms WHERE availability = 'vacant' and status = 'clean' ORDER BY room_number ASC")
            dirty_rooms = cur.fetchall()
            print(f"{dirty_rooms}")

            print("\nOut Of Order Rooms:")
            cur.execute("SELECT room_number, room_type FROM rooms WHERE status = 'ooo' ORDER BY room_number ASC")
            ooo_rooms = cur.fetchall()
            print(f"{ooo_rooms}")

            input("\nPress enter to continue")
        
        elif choice == 4: # Clean Rooms
            cur.execute("SELECT COUNT(room_number) FROM rooms WHERE status = 'dirty' ") #  ORDER BY room_number ASC
            cleaned_rooms = cur.fetchone()[0]
            cur.execute("UPDATE rooms SET status = 'clean' WHERE status = 'dirty' ")

            print(f"You cleaned {cleaned_rooms} rooms.")
            con.commit()
        
        print("")
    

print("Thank you for your time! Until next time!")  
con.close()