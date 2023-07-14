import os
import socket
import time

# Function to send emails
def send_emails():
    subject = input("Enter the subject of the email: ")
    print()
    DATA = input("Enter the body of the email: ")
    print()
    MAILSERVER = input("Enter the Mail Server Name (e.g., mail.example.com): ")
    print()
    PORT = input("Enter the port number for the mail server: ")
    print()
    MAILFROM = input("Enter the email address from which you want to send the email: ")
    print()
    MAILTO = input("Enter the email address to which you want to send the email: ")
    print()
    NUM_EMAILS = int(input("Enter the number of emails to send: "))
    print()
    DELAY_TIME = int(input("Enter the delay time between each email (in seconds): "))

    # Create the logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    # Start the email sending loop
    for i in range(1, NUM_EMAILS + 1):
        print()
        print(f"Sending email {i}/{NUM_EMAILS}...")
        try:
            with socket.create_connection((MAILSERVER, PORT), timeout=10) as sock:
                sock.sendall(
                    f"HELO {MAILSERVER}\r\nMAIL FROM:<{MAILFROM}>\r\nRCPT TO:<{MAILTO}>\r\nDATA\r\nSubject: {subject}\r\n\r\n{DATA}\r\n.\r\nQUIT\r\n".encode()
                )
                print(f"Email {i}/{NUM_EMAILS} sent!")
        except Exception as e:
            print(f"Failed to send email {i}/{NUM_EMAILS}: {e}")

        time.sleep(DELAY_TIME)

    # Log the email sending activity
    log_message(f"Emails sent: {NUM_EMAILS}")


# Function to send UDP packets
def send_udp_packets():
    IP = input("Enter the IP address to which you want to send UDP packets: ")
    print()
    UDP_PORT = int(input("Enter the port number for the UDP packets: "))
    print()
    NUM_PACKETS = int(input("Enter the number of UDP packets to send: "))
    print()
    DELAY_TIME = int(input("Enter the delay time between each UDP packet (in seconds): "))

    # Start the UDP sending loop
    for i in range(1, NUM_PACKETS + 1):
        print()
        print(f"Sending UDP packet {i}/{NUM_PACKETS}...")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.sendto(b"", (IP, UDP_PORT))
                print(f"UDP packet {i}/{NUM_PACKETS} sent!")
        except Exception as e:
            print(f"Failed to send UDP packet {i}/{NUM_PACKETS}: {e}")

        time.sleep(DELAY_TIME)

    # Log the UDP packet sending activity
    log_message(f"UDP packets sent: {NUM_PACKETS}")


# Function for logging
def log_message(message):
    log_file = "logs/send_script.log"
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"[{timestamp}] {message}\n")


# Function for input validation
def validate_input(input_value, pattern):
    import re

    if not re.match(pattern, input_value):
        return False
    return True


# Function for displaying the main menu
def display_main_menu():
    print()
    print("Please choose an option:")
    print()
    print("1. Send emails")
    print("2. Send empty UDP packets")
    print("0. Exit")
    print()


# Function to clear the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Loop to display the main menu until the user chooses to exit
while True:
    clear_screen()
    display_main_menu()
    OPTION = input("Option (0-2): ")

    # Validate the input
    if not validate_input(OPTION, "^(0|1|2)$"):
        # Invalid option chosen
        clear_screen()
        print("Invalid option. Please choose a valid option.")
        time.sleep(2)
        continue

    # Valid option chosen
    if OPTION == "1":
        # Sending emails
        clear_screen()
        print("You chose to send emails.")
        send_emails()
    elif OPTION == "2":
        # Sending UDP packets
        clear_screen()
        print("You chose to send empty UDP packets.")
        send_udp_packets()
    elif OPTION == "0":
        # Exit the script
        clear_screen()
        print("Exiting...")
        time.sleep(2)
        break
