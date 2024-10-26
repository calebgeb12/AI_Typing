import keyboard
import time

def press_keys(key_press):
    keyboard.write(key_press)

def test_press_keys(key_stroke):

    if (key_stroke == 'ignore for now'):
        print('special')

    # if key_stroke == 'alt_tab':
    #     keyboard.press('alt')
    # elif key_stroke == 'tab':
    #     keyboard.press_and_release('tab')
    # elif key_stroke == 'release_alt':
    #     print("releasing")
    #     keyboard.release('alt')
    # elif key_stroke == 'escape':
    #     keyboard.press_and_release('esc')

    # else:
    #     keyboard.write(key_stroke)
 


#training data 2:
    #press alt tab
    # if gesture_id == 'right_hand_FIRST_BUMB':                                         
    #     keyboard.press('alt')
    #     time.sleep(0.1)
    #     keyboard.press_and_release('tab')

    # #press tab
    # elif gesture_id == 'left_hand_GOOD':                                          
    #     keyboard.press_and_release('tab')
    
    # #press alt
    # elif gesture_id == 'left_hand_OPEN':                                           
    #     keyboard.press_and_release('alt')

    # #press escape
    # if gesture_id == 'right_hand_OPEN':
    #     keyboard.press_and_release('esc')
    