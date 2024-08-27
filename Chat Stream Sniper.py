import pytchat
from youtubesearchpython import VideosSearch
import asyncio
import os
import psutil
import keyboard
import pyautogui
import time
import re as regex
import array
import random
import ctypes
# import threading
import multiprocessing
import signal


# Replace with the video ID of the YouTube live stream
# VIDEO_ID = 'tSG2fb3aQwg'

repetitionComment = "#pubgdaddy"

totalAccount = 15  # Define the number of accounts

tabChangeInterval = 1  # Define the interval for tab change

repetitionStart = 0
repetitionEnd = 250

randomizeState = True   # Variable indicating whether to randomize the array

windowChangeInterval = 8  # Define the (interval or number of tabs) for window change



def show_message_box(message, duration):
    def run_powershell_script():
        # Define the PowerShell script with placeholders for the message and duration
        powershell_script = f"""
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$form = New-Object System.Windows.Forms.Form
$form.StartPosition = "CenterScreen"
$form.Size = New-Object System.Drawing.Size(300, 100)
$form.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::None
$form.TopMost = $true

$label = New-Object System.Windows.Forms.Label
$label.Text = "{message}"
$label.Font = New-Object System.Drawing.Font("Arial", 12, [System.Drawing.FontStyle]::Bold)
$label.TextAlign = [System.Drawing.ContentAlignment]::MiddleCenter
$label.AutoSize = $false
$label.Size = New-Object System.Drawing.Size(300, 100)
$label.Dock = [System.Windows.Forms.DockStyle]::Fill

$form.Controls.Add($label)

$timer = New-Object System.Windows.Forms.Timer
$timer.Interval = {duration}  # Duration in milliseconds

$timer.Add_Tick({{
    $timer.Stop()
    $form.Close()
    $form.Dispose()
    [System.Windows.Forms.Application]::Exit()
}})

$timer.Start()
[System.Windows.Forms.Application]::Run($form)
"""



def isProcessRunning(exe_name):
    # Iterate over all running processes
    for process in psutil.process_iter(['name']):
        # Check if process name matches
        if process.info['name'] == exe_name:
            return True
    return False


exe_file = 'Disable-Function-Keys.exe'  # Specify the path to the executable file

if not os.path.exists(exe_file):  # Check if the executable file doesn't exists
    print(f"{exe_file} Not Found.")
    exit(0)  # Exit the script if file doesn't exist

if not isProcessRunning(exe_file):  # Check if the executable file is not running
    process = psutil.Popen(exe_file)  # Launch the executable file
    print(f"{exe_file} File Launch")
else:
    print(f"{exe_file} File is Running...")


LiveChatArrayLogFile = "LiveChatArrayLogFile.txt"  # Specify the path to the LiveChatArrayLogFile file

# load the array from LiveChatArrayLogFile.txt file
def logFileArrayLoad():
    if os.path.exists(LiveChatArrayLogFile): # Check if the LiveChatArrayLogFile is exists
        with open(LiveChatArrayLogFile, "r") as file:
            try:
                data = file.read().strip()

                if not data: return []  # Check if the read data is empty; if so, return an empty list
                
                # Display the popup message box and capture the return value
                # response = ctypes.windll.user32.MessageBoxW(0, "Are you want to use Previous data!", "Data Usage Confirmation", 0x20 | 0x4 | 0x100)

                # Return evaluated data if user chooses to use it, otherwise return an empty list
                # return eval(data) if response == 6 else []

                response = input("\033[38;2;255;0;0m" + "Do you want to use previous data? (yes/no): " + "\033[0m").strip().lower()
                if response in ['yes', 'y']:
                    return eval(data)
                elif response in ['no', 'n', '']:
                    return []  # Returns a new empty list
                else:
                    return []  # Returns a new empty list
            except Exception as error:
                return []  # Returns a new empty list
    return []  # Returns a new empty list


# Save the array in exact format to LiveChatArrayLogFile.text file
def logFileArraySave(array):
    if not array: return  # Check if the array is empty; if so, Exit the function
    with open(LiveChatArrayLogFile, "w") as file:
        file.write(str(array))  # Save the list as a string


def is_valid_number(data):
    # Regular expression to match the entire string if it contains only valid numbers (positive or negative)
    pattern = r'^-?\b(?:[1-9]\d*|0)\b$'

    # Check if the entire string matches the pattern (True if match found, False otherwise)
    return regex.match(pattern, str(data)) is not None


# Handle the SIGINT signal (Ctrl+C) Pressed
def signal_handler(sig, frame):
    logFileArraySave(sharedArray)  # save the sharedArray in the log file (Ctrl+C) Pressed
    exit(0)


def fetchYoutubeLiveTitle(videoId):
    search = VideosSearch(videoId, limit = 1)
    result = search.result()
    if result['result']:
        title = result['result'][0]['title']
        print(f"\033[38;2;255;0;0m YouTube Live Title \033[38;5;226m ==>: \033[38;2;255;0;0m {title} \033[38;5;33m\033[0m")
    else:
        print(f"\033[38;2;255;0;0m Live Stream Not Found \033[0m")


def fetchYoutubeLiveChat(videoId, sharedArray, lock):
    # show_message_box("Ready to Fetch Youtube Live Chat", 1000)  # 1000 milliseconds
    print(videoId)

    print("\033[38;5;226m" + "Fetching Youtube Live Chat Data..." + "\033[0m")
    
    chat = pytchat.create(video_id=videoId)
    while chat.is_alive():
        for data in chat.get().items:
            message = data.message
            if (
                is_valid_number(message)                    # Check if message is a valid number
                and repetitionStart <= int(message) <= repetitionEnd  # Ensure message is between 0 and 250
                and int(message) != "-0"                    # Ensure message is not "-0"
                and int(message) not in sharedArray  # Ensure message is not in sharedArray
            ):
                with lock:
                    sharedArray.append(int(message))
        time.sleep(0.01)  # 10 milliseconds


async def streamSniper(start, end):
    start_time = time.time()
    
    loopState = True  # Set loopState to True to start the loop

    randomNumbers = array.array('i', range(start, end + 1))  # Create an array of integers (numbers) from start to end

    #if randomizeState is True then Shuffle (Randomize Array) the array in place using random.shuffle()
    if randomizeState:
        random.shuffle(randomNumbers)
        
    for index, number in enumerate(randomNumbers):
        
        if loopState is False: break  # Exit the loop
        
        if number in sharedArray: continue  # Skip this iteration if number exists in sharedArray

        # print(str(number))
        keyboard.write(str(number))  # Convert number to string before typing
        await asyncio.sleep(0.01)  # 10 milliseconds delay
        keyboard.send('Enter')  # KeyPress Enter
        await asyncio.sleep(0.01)  # 10 milliseconds delay

        if index % tabChangeInterval == 0 and index <= end:  # If the current index is a multiple of tabChangeInterval
            keyboard.send("Ctrl+Tab")  # KeyPress Ctrl+Tab
            await asyncio.sleep(0.1)  # 100 milliseconds delay


        if keyboard.is_pressed('F2'):
            loopState = False
            while keyboard.is_pressed('F2'):  # Wait for F2 Key to be released
                await asyncio.sleep(0.01)
        
        while loopState is False:  # If paused
            if keyboard.is_pressed('F2'):
                loopState = True
                while keyboard.is_pressed('F2'):  # Wait for F2 Key to be released
                    await asyncio.sleep(0.01) 
                break
            await asyncio.sleep(0.01)  # Reduce CPU usage while waiting
        
        if keyboard.is_pressed('F1'):  # Check if F1 Key is pressed
            logFileArraySave(sharedArray)  # save the sharedArray in the log file
            break  # Exit the loop

    logFileArraySave(sharedArray)  # save the sharedArray in the log file
    # keyboard.send("ctrl+tab")  # KeyPress Ctrl+Tab
    print(f"Elapsed time: {time.time() - start_time} Seconds")


async def neutralizeElement():
    start_time = time.time()

    loopState = True  # Set loopState to True to start the loop

    for _ in range(totalAccount):   # Loop through the range of totalAccount

        if loopState is False: break  # Exit the loop
        
        keyboard.send('Ctrl+Shift+Y')  # KeyPress Ctrl+Shift+Y
        await asyncio.sleep(0.1)
        keyboard.send("ctrl+tab")  # KeyPress Ctrl+Tab
        await asyncio.sleep(0.4)

        
        if keyboard.is_pressed('F2'):
            loopState = False
            while keyboard.is_pressed('F2'):
                await asyncio.sleep(0.01)
        
        while loopState is False:  # If paused
            if keyboard.is_pressed('F2'):
                loopState = True
                while keyboard.is_pressed('F2'):
                    await asyncio.sleep(0.01) 
                break
            await asyncio.sleep(0.01)  # Reduce CPU usage while waiting
        
        if keyboard.is_pressed('F1'): break  # if F1 Key is pressed exit the loop
        
    print(f"neutralizeElement() => Elapsed time: {time.time() - start_time} Seconds")


async def commentRepeater(comment=None, rawValue=None, typeComments=False, sendComments=False, delayTime="0.01"):
    start_time = time.time()
    
    loopState = True  # Set loopState to True to start the loop

    delay = float(delayTime)

    for _ in range(totalAccount):

        if loopState is False: break  # Exit the loop

        if typeComments == True:

            if rawValue == True:
                keyboard.write(comment)  # Typing Raw Value
            elif rawValue == False:
                keyboard.send(comment)  # KeyPress
                
            await asyncio.sleep(delay)
        
        if sendComments == True:
            keyboard.send("Enter")  # KeyPress Enter
            await asyncio.sleep(delay)
            
        keyboard.send("Ctrl+Tab")  # KeyPress Ctrl+Tab
        await asyncio.sleep(delay)


        if keyboard.is_pressed('F2'):
            loopState = False
            while keyboard.is_pressed('F2'):  # Wait for F2 Key to be released
                await asyncio.sleep(0.01)
        
        while loopState is False:  # If paused
            if keyboard.is_pressed('F2'):
                loopState = True
                while keyboard.is_pressed('F2'):  # Wait for F2 Key to be released
                    await asyncio.sleep(0.01) 
                break
            await asyncio.sleep(0.01)  # Reduce CPU usage while waiting

        if keyboard.is_pressed('F1'): break  # if F1 Key is pressed exit the loop
        
    print(f"Elapsed time: {time.time() - start_time} Seconds")



async def asyncMainTask(videoId):
    print("\033[38;5;33m" + "Ready to Start Chat Stream Sniper" + "\033[0m")

    lock = multiprocessing.Lock()
    fetchChatProcess = None

    while True:
        if keyboard.is_pressed('ESC'):
            print("ESC Key Pressed")
            await neutralizeElement()
            while keyboard.is_pressed('ESC'):  # Wait for ESC Key to be released
                await asyncio.sleep(0.01)
        await asyncio.sleep(0.01)

        if keyboard.is_pressed('Shift+F9'):
            print("Shift+F9")
            await commentRepeater(repetitionComment, True, True, False, "0.2")  # arg: comment, rawValue, typeComments, sendComments, delayTime
            while keyboard.is_pressed('Shift+F9'):  # Wait for Shift+F9 Key to be released
                await asyncio.sleep(0.01)
        await asyncio.sleep(0.01)

        if keyboard.is_pressed('F9'):
            print("F9")
            await commentRepeater(sendComments=True)  # arg: comment, rawValue, typeComments, sendComments, delayTime
            while keyboard.is_pressed('F9'):  # Wait for F9 Key to be released
                await asyncio.sleep(0.01)
        await asyncio.sleep(0.01)

        if keyboard.is_pressed('Shift+F10'):
            print("Shift+F10")
            await commentRepeater("Ctrl+V", False, True, True, "0.2")  # arg: comment, rawValue, typeComments, sendComments, delayTime
            while keyboard.is_pressed('Shift+F10'):  # Wait for Shift+F10 Key to be released
                await asyncio.sleep(0.01)
        await asyncio.sleep(0.01)

        if keyboard.is_pressed('F10'):
            print("F10")
            await commentRepeater("Ctrl+V", False, True, False, "0.2")  # arg: comment, rawValue, typeComments, sendComments, delayTime
            while keyboard.is_pressed('F10'):  # Wait for F10 Key to be released
                await asyncio.sleep(0.01)
        await asyncio.sleep(0.01)


        if keyboard.is_pressed('F3') and (fetchChatProcess is None or not fetchChatProcess.is_alive()):
            print("F3 Key Pressed")
            fetchChatProcess = multiprocessing.Process(target=fetchYoutubeLiveChat, args=(videoId, sharedArray, lock))
            fetchChatProcess.start()
            while keyboard.is_pressed('F3'):  # Wait for F3 Key to be released
                await asyncio.sleep(0.01)
        await asyncio.sleep(0.01)

        if keyboard.is_pressed('F5'):
            print("F5")
            await asyncio.gather(
                streamSniper(0, 50),
                # streamSniper(0, 100)
            )
            while keyboard.is_pressed('F5'):  # Wait for F5 Key to be released
                await asyncio.sleep(0.01)
        await asyncio.sleep(0.01)

        if keyboard.is_pressed('F6'):
            print("F6")
            await streamSniper(51, 100)
            while keyboard.is_pressed('F6'):  # Wait for F6 Key to be released
                await asyncio.sleep(0.01)
        await asyncio.sleep(0.01)

        if keyboard.is_pressed('F7'):
            print("F7")
            await streamSniper(101, 150)
            while keyboard.is_pressed('F7'):  # Wait for F7 Key to be released
                await asyncio.sleep(0.01)
        await asyncio.sleep(0.1)

        if keyboard.is_pressed('F8'):
            print("F8")
            await streamSniper(151, 200)
            while keyboard.is_pressed('F8'):  # Wait for F8 Key to be released
                await asyncio.sleep(0.01)
        await asyncio.sleep(0.1)

        if keyboard.is_pressed('F4'):
            print("F4")
            await streamSniper(201, 250)
            while keyboard.is_pressed('F4'):  # Wait for F4 Key to be released
                await asyncio.sleep(0.01)
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    VIDEO_ID = None
    if not VIDEO_ID: VIDEO_ID = input("\033[38;2;255;0;0m" + "Please enter the YouTube video ID: " + "\033[0m")
    
    with multiprocessing.Manager() as manager:
        # Initialize the sharedArray list for share data in multiprocessing
        sharedArray = manager.list(logFileArrayLoad())  # Load initial values from the log file
        print(f"logFileArrayLoad => : {list(sharedArray)}")
        
        signal.signal(signal.SIGINT, signal_handler)  # Register the signal handler for the SIGINT signal
        
        globals()['sharedArray'] = sharedArray  # Store the sharedArray in a global variable
        
        fetchYoutubeLiveTitle(VIDEO_ID)  # get youtube live title

        asyncio.run(asyncMainTask(VIDEO_ID))  # Run the main event loop

