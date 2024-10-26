#the purpose of this script is to automate the data collection of different key strokes
#this script uses timed events to prompt the user to press a key and records that data point

import keyboard
import time

key_to_id = {
    # Top row
    'q': 1, 'w': 3, 'e': 5, 'r': 7, 't': 9,
    'y': 2, 'u': 4, 'i': 6, 'o': 8, 'p': 10,
    
    # Home row
    'a': 11, 's': 13, 'd': 15, 'f': 17, 'g': 19,
    'h': 12, 'j': 14, 'k': 16, 'l': 18,
    
    # Bottom row
    'z': 21, 'x': 23, 'c': 25, 'v': 27, 'b': 29,
    'n': 22, 'm': 24, 

    #odd special characters
    'space': 101, 
    'alt': 103, 
    'tab': 105,
    'ctrl': 107,

    #even special characters
    'comma': 102,
    'colon': 104,

}

def on_key_event(event):
    # print(f"Key {event.name} {'pressed' if event.event_type == 'down' else 'released'}")
    # print(key_to_id[event.name])
    # keyboard.press_and_release(key_to_id[event.name])
    keyboard.press_and_release(event.name)
    print(key_to_id[event.name])



def main(): 
    print("\n\n------------------")
    keyboard.hook(on_key_event)
    print("Press 'esc' to stop.")
    keyboard.wait('esc')  # Stop listening when 'esc' is pressed

main()

# start_automation = False

# time_before_start = 2
# points_to_collect = 5
# keys_to_press = ['q', 'w', 'e', 'r']
# press_time = .3
# let_go_time = .2
# next_round_time = .2



# def main():
#     print("\n\n------------------")

#     time.sleep(time_before_start)
#     print("starting in....")
#     time.sleep(1)
#     print(3)
#     time.sleep(1)
#     print(2)
#     time.sleep(1)
#     print(1)
#     time.sleep(1)
#     print("\n------------------\n")


#     #tasks: auto press key, tell what key to press, 
#     for i in range (0, points_to_collect): 
#         for key in  keys_to_press:
#             #tell what key to press
#             print(key)
#             time.sleep(press_time)

#             #auto press key
#             print("----LET GO---\n")
#             keyboard.press_and_release(keys_to_press[key])

#             #register none
#             time.sleep(let_go_time)
#             keyboard.press_and_release(keys_to_press['none'])
#             time.sleep(next_round_time)


