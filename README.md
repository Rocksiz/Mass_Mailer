# Email and UDP Packet Sender

This repository contains a Bash script and a Python script that allow you to send emails and UDP packets using the command line interface. You can choose the script based on your preference.

## Python Script

### Prerequisites
- Python 3.x

### Usage
1. Open a terminal.
2. Navigate to the directory where the script is located.
3. Run the Python script:
    ```bash
    python script.py
    ```
4. Follow the prompts to select the desired option and provide the necessary information.

## Bash Script

### Prerequisites
- Bash shell environment
- `nc` (netcat) command-line tool for sending emails
- Permission to send emails and UDP packets from your network

### Usage
1. Open a terminal.
2. Navigate to the directory where the script is located.
3. Make the script executable by running the following command:
    ```bash
    chmod +x script.sh
    ```
4. Run the script:
    ```bash
    ./script.sh
    ```
5. Follow the prompts to select the desired option and provide the necessary information.

### Options
The Python script and Bash script provides the same options:

1. Send emails: Send multiple emails with customizable subject, body, sender, recipient, number of emails, and delay time between each email.

2. Send empty UDP packets: Send multiple empty UDP packets to a specific IP address and port, specifying the number of packets and the delay time between each packet.

0. Exit: Terminate the script and exit.

### Logging
The Python script and Bash script logs the email and UDP packet sending activity in the `logs/send_script.log` file. Each log entry includes a timestamp and a message describing the activity.

## Note
- Ensure that you have the necessary permissions and valid network configurations to send emails and UDP packets.

**Caution**: Sending emails or UDP packets to unauthorized recipients or systems without permission may violate the terms of service of your network or internet service provider. Use these scripts responsibly and adhere to applicable laws and regulations.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
These scripts were created for educational purposes and inspired by similar utilities available in various programming languages.
