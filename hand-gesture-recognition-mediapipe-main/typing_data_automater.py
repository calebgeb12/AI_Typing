#the purpose of this script is to automate the data collection of different key strokes
#this script uses timed events to prompt the user to press a key and records that data point

import keyboard
import time

key_to_id = {
    # Top row
    'q': '1', 'w': '3', 'e': '5', 'r': '7', 't': '9',
    'y': '2', 'u': '4', 'i': '6', 'o': '8', 'p': '10',
    
    # Home row
    'a': '11', 's': '13', 'd': '15', 'f': '17', 'g': '19',
    'h': '12', 'j': '14', 'k': '16', 'l': '18',
    
    # Bottom row
    'z': '21', 'x': '23', 'c': '25', 'v': '27', 'b': '29',
    'n': '22', 'm': '24', 

    # # Odd special characters
    # 'space': '101', 
    # 'alt': '103', 
    # 'tab': '105',
    # 'ctrl': '107',

    # # Even special characters
    # 'comma': '102',
    # 'colon': '104'
}


test_map = {
    'q': 2, 
    'w': 4,
    'e': 6, 
    'r': 8, 
    't': 10,
}


def testing(event):
    num_to_press = key_to_id[event.name]
    if int(key_to_id[event.name]) < 10:
        keyboard.press_and_release(num_to_press)

         
def on_key_event(event):
    if event.event_type == 'down' and event.name in key_to_id:
        testing(event)
    elif event.event_type == 'up' and event.name in key_to_id:
        print("released")

def main(): 
    print("\n\n------------------")
    keyboard.hook(on_key_event)
    print("Press 'esc' to stop.")
    keyboard.wait('esc')  

main()

