class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_booked = False

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"Room {self.room_number} - {self.room_type} - {self.price} rupees - {status}"


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def display_rooms(self):
        print(f"\nRooms in {self.name}:")
        for room in self.rooms:
            print(room)

    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.is_booked:
                    room.is_booked = True
                    print(f"Room {room_number} booked successfully!")
                    return
                else:
                    print("Room is already booked.")
                    return
        print("Room number not found.")

    def cancel_booking(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.is_booked:
                    room.is_booked = False
                    print(f"Booking for Room {room_number} canceled.")
                    return
                else:
                    print("Room is not currently booked.")
                    return
        print("Room number not found.")


def main():
    hotel = Hotel("Sunset Inn")
    hotel.add_room(Room(101, "Single", 10000))
    hotel.add_room(Room(102, "Double", 15000))
    hotel.add_room(Room(103, "Suite", 25000))

    while True:
        print("\n--- Hotel Booking System ---")
        print("1. View Rooms")
        print("2. Book Room")
        print("3. Cancel Booking")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            hotel.display_rooms()
        elif choice == '2':
            room_no = int(input("Enter room number to book: "))
            hotel.book_room(room_no)
        elif choice == '3':
            room_no = int(input("Enter room number to cancel booking: "))
            hotel.cancel_booking(room_no)
        elif choice == '4':
            print("Thank you for using the booking system.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
