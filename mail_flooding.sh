#!/bin/bash
clear
# Function to send emails
send_emails() {
    echo "Enter the subject of the email:"
    read -p "Subject: " subject

    echo
    echo "Enter the body of the email:"
    read -p "Body: " DATA

    echo
    echo "Enter the Mail Server Name (e.g., mail.example.com):"
    read -p "Mail Server: " MAILSERVER

    echo
    echo "Enter the port number for the mail server (typically 25, but 587 is commonly used):"
    read -p "Port: " PORT

    echo
    echo "Enter the email address from which you want to send the email (e.g., sender@example.com):"
    read -p "Mail From: " MAILFROM

    echo
    echo "Enter the email address to which you want to send the email (e.g., recipient@example.com):"
    read -p "Mail To: " MAILTO

    echo
    echo "Enter the number of emails to send:"
    read -p "Number of Emails: " NUM_EMAILS

    echo
    echo "Enter the delay time between each email (in seconds):"
    read -p "Delay Time: " DELAY_TIME

    # Create the logs directory if it doesn't exist
    mkdir -p "$(dirname "$0")/logs"

    # Start the email sending loop
    for ((i=1; i<=$NUM_EMAILS; i++))
    do
        echo
        echo "Sending email $i/$NUM_EMAILS..."
        echo -en "HELO $MAILSERVER\r\nMAIL FROM:$MAILFROM\r\nRCPT TO:$MAILTO\r\nDATA\r\nSubject: $subject\r\n\r\n$DATA\r\n.\r\nQUIT\r\n" | nc -w 10 $MAILSERVER $PORT
        echo "Email $i/$NUM_EMAILS sent!"
        sleep $DELAY_TIME
    done

    # Log the email sending activity
    log_message "Emails sent: $NUM_EMAILS"
}

# Function to send UDP packets
send_udp_packets() {
    echo "Enter the IP address to which you want to send UDP packets:"
    read -p "IP: " IP

    echo
    echo "Enter the port number for the UDP packets:"
    read -p "UDP Port: " UDP_PORT

    echo
    echo "Enter the number of UDP packets to send:"
    read -p "Number of UDP Packets: " NUM_PACKETS

    echo
    echo "Enter the delay time between each UDP packet (in seconds):"
    read -p "Delay Time: " DELAY_TIME

    # Start the UDP sending loop
    for ((i=1; i<=$NUM_PACKETS; i++))
    do
        echo
        echo "Sending UDP packet $i/$NUM_PACKETS..."
        echo > /dev/udp/$IP/$UDP_PORT
        echo "UDP packet $i/$NUM_PACKETS sent!"
        sleep $DELAY_TIME
    done

    # Log the UDP packet sending activity
    log_message "UDP packets sent: $NUM_PACKETS"
}

# Function for logging
log_message() {
    local log_file="$(dirname "$0")/logs/send_script.log"
    local timestamp="$(date +"%Y-%m-%d %H:%M:%S")"
    echo "[$timestamp] $1" >> "$log_file"
}

# Function for input validation
validate_input() {
    local input="$1"
    local pattern="$2"

    if [[ ! $input =~ $pattern ]]; then
        return 1
    fi
}

# Function for displaying the main menu
display_main_menu() {
    echo
    echo "Please choose an option:"
    echo
    echo "1. Send emails"
    echo "2. Send empty UDP packets"
    echo "0. Exit"
    echo
}

# Loop to display the main menu until the user chooses to exit
while true; do
    display_main_menu
    read -p "Option (0-2): " OPTION

    # Validate the input
    validate_input "$OPTION" "^(0|1|2)$"

    if [[ $? -eq 0 ]]; then
        # Valid option chosen
        if [[ $OPTION == "1" ]]; then
            # Sending emails
            echo
            echo "You chose to send emails."
            send_emails
        elif [[ $OPTION == "2" ]]; then
            # Sending UDP packets
            echo
            echo "You chose to send empty UDP packets."
            send_udp_packets
        elif [[ $OPTION == "0" ]]; then
            # Exit the script
            echo
            echo "Exiting..."
            break
        fi
    else
        # Invalid option chosen
        clear
        echo "Invalid option. Please choose a valid option."
    fi
done
