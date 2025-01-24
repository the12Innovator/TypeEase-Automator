import pyautogui
import time

def perform_actions(chat_coordinates):
    for _ in range(2):  # Repeat the actions 2 times
        for coordinates in chat_coordinates:
            # Step 1: Click on the chat group coordinates
            pyautogui.click(coordinates)

            # Step 2: Right-click on (524, 728) and left-click on (586, 750)
            pyautogui.click(524, 728, button='right')
            time.sleep(2)  # Optional delay between clicks
            pyautogui.click(586, 750)
            time.sleep(4)  # Optional delay between clicks

            # Step 3: Type the message and send
            message = "Can You Gift me Twinkle.\n https://gpay.app.goo.gl/yUsXA7"
            pyautogui.typewrite(message)
            pyautogui.press('enter')
            time.sleep(10)  # Optional delay between sending messages

def main():
    chat_coordinates = [
        (197, 136),  # Coordinates of chat group 1
        (180, 215),  # Coordinates of chat group 2
        (209, 302),  # Coordinates of chat group 3
        (225, 367),  # Coordinates of chat group 4
        (210, 436)
        #(311, 515),
        #(309, 586),
        #(323, 683)
        ]


    perform_actions(chat_coordinates)


if __name__ == "__main__":
    main()
""" 

import time

import pyautogui

def send_message_to_telegram(chat_coordinates, message):
    # Open Telegram (assuming it's already installed and logged in)
    pyautogui.hotkey('command', 'space')  # Adjust this for Windows users
    time.sleep(1)  # Wait for the spotlight/search to open
    
    # Click on the search bar
    pyautogui.click(100, 100)  # Adjust coordinates according to your screen resolution
    
    # Click on the chat group
    pyautogui.click(chat_coordinates[0], chat_coordinates[1])
    
    # Type and send the message
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    time.sleep(1)  # Ad d delay to ensure message is sent

def main():
    chat_coordinates = [
        (197, 136),  # Coordinates of chat group 1
        (180, 215),  # Coordinates of chat group 2
        (209, 302),  # Coordinates of chat group 3
        (225, 367)   # Coordinates of chat group 4
        #(210, 436),
        #(311, 515), 
        #(309, 586),
        #(323, 683)   
    ]  
    message = "Can Anyone Gift me Twinkle.✨I Have 3 Trendy We can exchange.🤝🤝  https://gpay.app.goo.gl/yUsXA7" 
    num_iterations = 1     # Repeat the process 3 times
     
    for _ in range(num_iterations):
        for coordinates in chat_coordinates:
            print(f"Sending message to chat group at coordinates: {coordinates}")
            send_message_to_telegram(coordinates, message)
            time.sleep(1)  # Add delay between sending messages
        print("Waiting before next iteration...")
        time.sleep(10)  # Wait for 60 seconds before next iteration

if __name__ == "__main__":
    main()
              """