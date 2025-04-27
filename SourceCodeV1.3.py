import os
import time
import ahk
from ahk import AHK
import datetime
from datetime import datetime
import pyautogui

os.system("color 5")
current_time = datetime.now().strftime("%H:%M:%S")
current_cycle = 0
collections_remaining = 25 # 25 OUTSIDE OF TESTING
initial_collections = collections_remaining
time_to_collect = 58 # 58 OUTSIDE OF TESTING

print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to AutoPrintCycleES! | VERSION: 1.3 | \n27/04/25 | USER FRIENDLINESS UPDATE\n+ OLD "POSITIONING" SYSTEM REPLACED WITH A CALIBRATION SYSTEM, ALLOWING THE PROGRAM TO FUNCTION ON ALL SIZE DISPLAYS.\n+ FIXED AN ISSUE WITH TIME BEING INCORRECTLY DISPLAYED WITH CERTAIN ACTIONS.\n+ OPTIMISED CODE.\n\nThis is a script that automatically collects printer money in Electric State for you.\nPlease follow the given instructions to ensure the program can work correctly\n\n! PLEASE CONTACT THE CREATOR INCASE OF ANY PROBLEMS WITH THE PROGRAM.\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nYOU MUST CRAFT THE 2 PRINTERS BEFORE CALIBRATING.\nYOU MUST NOT MOVE IN BETWEEN CRAFTING THE PRINTERS; THEY SHOULD STAY ON TOP OF ONE ANOTHER.\nIF THIS IS NOT CLEAR TO YOU, DM THE SELLER FOR A MORE INDEPTH GUIDE. (duduundu on discord)\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

if initial_collections != 25 or time_to_collect != 58:
    print("! VARIABLES ARE INACCURATE. IF YOU ARE TESTING SOMETHING, IGNORE THIS. CONTACT THE CREATOR OTHERWISE.")

while True:
    try:
        print_cycles = int(input("ENTER THE NUMBER OF PRINT CYCLES NEEDED. (1 CYCLE = 25 MINUTES): "))
        break 
    except ValueError:
        print("\nINPUT MUST BE A WHOLE NUMBER. PLEASE REENTER.")

if print_cycles == 0:
    print("\nwhat????????")
    time.sleep(5)
    quit()

print("\n",print_cycles,"PRINT CYCLES SELECTED.. THIS WILL TAKE APPROX", print_cycles * 25, "MINUTES TO COMPLETE.\n")

# CALIBRATION PROMPT
print("THE MOUSE POSITIONS MAY BE INCORRECTLY CALIBRATED BASED ON THE SIZE OF YOUR DISPLAY")
print("PLEASE PRESS ENTER TO BEGIN CALIBRATION")
confirmation = input("")

# CALIBRATING PRINTERS
input("CALIBRATION PROCESS SELECTED.\n\nPLEASE BUILD YOUR TWO PRINTERS BEFORE CONTINUING.")
print("PLACE YOUR MOUSE CURSOR ON THE FIRST PRINTER WITHIN 10 SECONDS.")
time.sleep(10)
print("RECORDING COORDINATES...")
printerpos1x, printerpos1y = pyautogui.position()
time.sleep(2)
print("FIRST PRINTER COORDINATES RECORDED. X:", [printerpos1x], "Y:", [printerpos1y])
time.sleep(2)
print("PLACE YOUR MOUSE CURSOR ON THE SECOND PRINTER WITHIN 10 SECONDS.")
time.sleep(10)
print("RECORDING COORDINATES...")
printerpos2x, printerpos2y = pyautogui.position()
time.sleep(2)
print("SECOND PRINTER COORDINATES RECORDED. X:", [printerpos2x], "Y:", [printerpos2y])

# CALIBRATING BUTTONS
time.sleep(2)
print("")
print("PRESS T AND PLACE YOUR CURSOR ON THE SHOP BUTTON WITHIN 10 SECONDS")
time.sleep(10)
print("RECORDING COORDINATES...")
shopbuttonx, shopbuttony = pyautogui.position()
time.sleep(2)
print("SHOP BUTTON COORDINATES RECORDED. X:", [shopbuttonx], "Y:", [shopbuttony])
time.sleep(2)
print("PLACE YOUR MOUSE CURSOR ON THE ADVANCED PRINTER BUTTON WITHIN 10 SECONDS.")
time.sleep(10)
print("RECORDING COORDINATES...")
advprinterx, advprintery = pyautogui.position()
time.sleep(2)
print("ADVANCED PRINTER BUTTON COORDINATES RECORDED. X:", [advprinterx], "Y:", [advprintery])
time.sleep(2)
print("PLACE YOUR MOUSE CURSOR ON THE CRAFT BUTTON WITHIN 10 SECONDS.")
time.sleep(10)
print("RECORDING COORDINATES...")
craftx, crafty = pyautogui.position()
time.sleep(2)
print("CRAFT BUTTON COORDINATES RECORDED. X:", [craftx], "Y:", [crafty])

time.sleep(2)
print("\nPROGRAM WILL START IN 15 SECONDS.\n\nTAB OUT OF ALL OTHER WINDOWS EXCEPT FOR THE ROBLOX CLIENT.\nDO NOT MOVE YOUR CAMERA OR CHARACTER WHILE THE PROGRAM IS RUNNING\nDO NOT TAB OUT OF THE ROBLOX CLIENT OR INTO ANY OTHER TABS.\nTO STOP THE PROGRAM, SIMPLY CLOSE THIS CONSOLE WINDOW.\nMADE A MISTAKE? CLOSE THIS WINDOW AND REOPEN THE PROGRAM.")

time.sleep(15)
current_time = datetime.now().strftime("%H:%M:%S")
print([current_time], "PROGRAM STARTED.")

while print_cycles > 1:
    for i in range(initial_collections): # CHANGE TO 25 | 25 minutes to run printer down
        time.sleep(time_to_collect) # CHANGE TO 58
        ahk.mouse_move(x=printerpos1x, y=printerpos1y) # Moves samouse to the first printer
        time.sleep(0.1)
        ahk.mouse_move(x=printerpos1x + 10, y=printerpos1y) # "Humaniser", ensures the collection GUI appears
        ahk.send_input('e')
        time.sleep(1)
        ahk.mouse_move(x=printerpos1x + 200, y=printerpos1y) # Moves mouse away from the first printer to remove collection GUI
        time.sleep(1)
        ahk.mouse_move(x=printerpos2x, y=printerpos2y) # Moves mouse to the second printer
        time.sleep(0.1)
        ahk.mouse_move(x=printerpos2x + 10, y=printerpos2y) # "Humaniser", ensures the collection GUI appears
        ahk.send_input('e')
        collections_remaining -= 1
        current_time = datetime.now().strftime("%H:%M:%S")
        print([current_time], collections_remaining, "COLLECTIONS REMAINING.")
    if print_cycles > 1 and collections_remaining == 0:
        print([current_time], "NEW CYCLE STARTING, CRAFTING NEW PRINTERS.")
        ahk.send_input('t')
        time.sleep(0.2)
        ahk.mouse_move(x=shopbuttonx, y=shopbuttony) # Shop button
        ahk.click(button='left')
        time.sleep(0.2)
        ahk.mouse_move(x=advprinterx, y=shopbuttony) # Adv Printer
        ahk.click(button='left')
        time.sleep(0.2)
        ahk.mouse_move(x=craftx, y=crafty) # Craft
        ahk.click(button='left')
        time.sleep(11) # Time taken to craft printer + 1 second
        print([current_time], "FIRST PRINTER CRAFTED.")
        ahk.send_input('t')
        ahk.mouse_move(x=advprinterx, y=advprintery) # Adv Printer
        ahk.click(button='left')
        time.sleep(0.2)
        ahk.mouse_move(x=craftx, y=crafty) # Craft
        ahk.click(button='left')
        time.sleep(11)
        current_time = datetime.now().strftime("%H:%M:%S")
        print([current_time], "SECOND PRINTER CRAFTED.")
        current_cycle += 1
        collections_remaining += initial_collections # Resets number of collections for the next cycle
        current_time = datetime.now().strftime("%H:%M:%S")
        print([current_time], "PRINT CYCLE", current_cycle, "FINISHED.")
        print([current_time], "CURRENT PRINT CYCLE:", print_cycles)
        print_cycles -= 1
    if print_cycles == 1:
        collections_remaining += initial_collections
        current_time = datetime.now().strftime("%H:%M:%S")
        print([current_time], "FINAL PRINT CYCLE UNDERWAY")
        for i in range(initial_collections):
            ahk.mouse_move(x=printerpos1x, y=printerpos1y) # Moves mouse to the first printer
            time.sleep(0.1)
            ahk.mouse_move(x=printerpos1x + 10, y=printerpos1y) # "Humaniser", ensures the collection GUI appears
            ahk.send_input('e')
            time.sleep(1)
            ahk.mouse_move(x=printerpos1x + 200, y=printerpos1y) # Moves mouse away from the first printer to remove collection GUI
            time.sleep(1)
            ahk.mouse_move(x=printerpos2x, y=printerpos2y) # Moves mouse to the second printer
            time.sleep(0.1)
            ahk.mouse_move(x=printerpos2x + 10, y=printerpos2y) # "Humaniser", ensures the collection GUI appears
            ahk.send_input('e')
            current_time = datetime.now().strftime("%H:%M:%S")
            print([current_time], "ALL PRINT CYCLES FINISHED.")
            break

current_time = datetime.now().strftime("%H:%M:%S")
print([current_time], "SCRIPT FINISHED. THIS TAB WILL STAY OPEN.")
input("")
