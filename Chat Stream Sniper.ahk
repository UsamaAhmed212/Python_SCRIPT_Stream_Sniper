global repetitionsComment := "#pubgdaddy "

; global winComment := "SpikE | OP 5400684791"

; Multiline string containing multiple lines of text
winAccountString =
(
SpikE | OP  5400684791
BAPPY  51238048239
S8ULNOOBEDIAN  51801336333
GUNDA . 0P  5244828288
BERTO . OP  52027306851
Queen Mim  52014574581
HAF SAnur  5624665911
Hasib  51775690258
TSP AYaTO  5738871282
FBI Ridoy  51379092486
YX | RayhanYT  5575238449
TG | NIKLAUS  5198188352
Alpha  5191205958
SHABBIR 51719759313
KING Shadin 5350212840
)


global repetitions := 250 ; Define the number of repetitions

global totalAccount := 25 ; Define the number of accounts

global tabChangeInterval := 1 ; Define the interval for tab change

global randomizeArray := False ; Randomize Array Fisher-Yates Algorithm

global windowChangeInterval := 8 ; Define the (interval or number of tabs) for window change

global loopState := True ; Initialize Loop State



neutralizeElement() { ; Start/Restart Loop
    ToolTip, Start ; Display tooltip indicating loop start
    SetTimer, RemoveToolTip, 2000  ; Remove the tooltip after 2 Seconds
    
    Loop, % totalAccount {  ; Start/Restart Loop
        if (!loopState)
            break  ; Exit the loop

        Send ^+y  ; Send Ctrl + Shift + Y
        Sleep, 100
        Send, ^{tab}  ; Send Ctrl+Tab
        Sleep, 400
    }

    ToolTip, Completed ; Display tooltip indicating loop completion
    SetTimer, RemoveToolTip, 2000  ; Remove the tooltip after 2 Seconds
}
return


Esc::
   loopState := True
   neutralizeElement()
return


F1::
   loopState := False
return

F2:: ; Space bar Key press
    pause, toggle
    ToolTip, % (A_IsPaused ? "Script Paused" : "Script Resumed") ; Display tooltip indicating script state
    SetTimer, RemoveToolTip, 2000  ; Remove the tooltip after 2 Seconds
return


F3::  ; Start/Restart Loop
    loopState := True
    streamSniperUp(0, 250) ; 0 to 250
    ; streamSniperDown(250, 0) ; 250 to 0
return


F4::  ; Start/Restart Loop
    loopState := True
    streamSniper(201, 250) ; 201 to 250
return

F5::  ; Start/Restart Loop
    loopState := True
    streamSniper(0, 50) ; 0 to 50
return

F6::  ; Start/Restart Loop
    loopState := True
    streamSniper(51, 100) ; 51 to 100
return

F7::  ; Start/Restart Loop
    loopState := True
    streamSniper(100, 150) ; 100 to 150
return

F8::  ; Start/Restart Loop
    loopState := True
    streamSniper(150, 200) ; 150 to 200
return

; Function to shuffle an array using the Fisher-Yates algorithm
RandomizeArray(array) {
    Random, seed
    Random, random
    Random, random, 1, array.MaxIndex()
    Random, random, 1, array.MaxIndex()
    Random, random
    Loop, % array.MaxIndex() {
        Random, index, A_Index, array.MaxIndex()
        ; Swap array[A_Index] and array[index]
        temp := array[A_Index]
        array[A_Index] := array[index]
        array[index] := temp
    }
}

streamSniper(start, end) {
    ToolTip, Start ; Display tooltip indicating loop start
    SetTimer, RemoveToolTip, 2000  ; Remove the tooltip after 2 Seconds
    
    LoopStartTime := A_TickCount ; Record loop start time
    
    ; Create an array of numbers from start to end
    randomNumbers := []

    Loop, % (end - start + 1) {
        if (!loopState) 
            break  ; Exit the loop
    
        randomNumbers.Push(start + A_Index - 1)
    }

    ; Check if randomizeArray is set to True and shuffle the array if needed
    if (randomizeArray) {
        RandomizeArray(randomNumbers) ; Shuffle the array using Fisher-Yates algorithm
    }

    ; Iterate through the shuffled array and send each unique number
    for index, number in randomNumbers {
        if (!loopState) 
            break  ; Exit the loop
    
        Send, % number
        Sleep, 10
        Send, {Enter}
        Sleep, 10
        
        if (Mod(A_Index, tabChangeInterval) = 0 && A_Index < repetitions) { ; If the current index is a multiple of tabChangeInterval
            Send, ^{tab}  ; Send Ctrl+Tab
            Sleep, 100
        }
    }

    Sleep, 100
    Send, ^{tab}  ; Send Ctrl+Tab

    LoopEndTime := A_TickCount ; Record loop end time
    LoopDuration := (LoopEndTime - LoopStartTime) / 1000 ; Calculate loop duration in Seconds

    ToolTip, Completed - Loop took %LoopDuration% Seconds
    
    ; ToolTip, Completed ; Display tooltip indicating loop completion
    SetTimer, RemoveToolTip, 2000  ; Remove the tooltip after 2 Seconds
}

streamSniperUp(start, end) {
    ToolTip, Start ; Display tooltip indicating loop start
    SetTimer, RemoveToolTip, 2000  ; Remove the tooltip after 2 Seconds
    
    LoopStartTime := A_TickCount ; Record loop start time

    Loop, % (end - start + 1) {
        if (!loopState) 
            break  ; Exit the loop
        
        Send % (start + A_Index - 1)
        Sleep, 10
        Send, {Enter}
        Sleep, 10
        
        if (Mod(A_Index, tabChangeInterval) = 0 && A_Index < repetitions) { ; If the current index is a multiple of tabChangeInterval
            Send, ^{tab}  ; Send Ctrl+Tab
            Sleep, 100
        }
    }
    
    LoopEndTime := A_TickCount ; Record loop end time
    LoopDuration := (LoopEndTime - LoopStartTime) / 1000 ; Calculate loop duration in Seconds

    ToolTip, Completed - Loop took %LoopDuration% Seconds
    
    ; ToolTip, Completed ; Display tooltip indicating loop completion
    SetTimer, RemoveToolTip, 2000  ; Remove the tooltip after 2 Seconds
}

streamSniperDown(start, end) {
    ToolTip, Start ; Display tooltip indicating loop start
    SetTimer, RemoveToolTip, 2000  ; Remove the tooltip after 2 Seconds
    
    LoopStartTime := A_TickCount ; Record loop start time

    Loop, % (start - end + 1) {
        if (!loopState) 
            break  ; Exit the loop
        
        Send % (start - A_Index + 1)
        Sleep, 10
        Send, {Enter}
        Sleep, 50
        
        if (Mod(A_Index, tabChangeInterval) = 0 && A_Index < repetitions) { ; If the current index is a multiple of tabChangeInterval
            Send, ^{tab}  ; Send Ctrl+Tab
            Sleep, 200
        }
    }
        
    LoopEndTime := A_TickCount ; Record loop end time
    LoopDuration := (LoopEndTime - LoopStartTime) / 1000 ; Calculate loop duration in Seconds

    ToolTip, Completed - Loop took %LoopDuration% Seconds
    
    ; ToolTip, Completed ; Display tooltip indicating loop completion
    SetTimer, RemoveToolTip, 2000  ; Remove the tooltip after 2 Seconds
}

F9::
    loopState := True
    commentFunction(repetitionsComment)
return

F10::
    loopState := True
    commentFunction("^v", False)
return


F11::
    loopState := True
    findComment()
return


F12:: ; Start
    ; Define your array of winAccounts
    winAccounts := []

    ; Split the string by (new line)
    winAccountStringArray := StrSplit(winAccountString, "`n")

    ; Loop through each value in winAccountStringArray and push it into winAccounts
    for index, value in winAccountStringArray
        winAccounts.Push(value)

    ; Concatenate all winAccounts into a single string
    winAccountsString := ""
    Loop % winAccounts.MaxIndex()
        winAccountsString .= winAccounts[A_Index] "`r`n"  ; Append each comment with a new line

    ; Define the filename for the temporary text file
    tempFile := "temp_chat_stream_sniper.txt"

    ; Save the concatenated comments to the temporary text file
    FileDelete, %tempFile%  ; Delete any existing temp file
    FileAppend, %winAccountsString%, %tempFile%  ; Append all comments to the temp file

    ; Open the temporary file using the default program (usually Notepad)
    Run, %tempFile%

    ; Read the contents of the temporary file
    FileRead, fileContents, %tempFile%

    ; Display the concatenated comments from the file in a message box
    MsgBox, % fileContents

    ; Copy the concatenated comments to the clipboard
    Clipboard := fileContents

    ; Delete the temporary file
    FileDelete, %tempFile%
return


commentFunction(comment, rawValue := true) { ; Start/Restart Loop
    ToolTip, Start ; Display tooltip indicating loop start
    SetTimer, RemoveToolTip, 2000  ; Remove the tooltip after 2 Seconds
    
    Loop, % totalAccount {  ; Start/Restart Loop
        if (!loopState)
            break  ; Exit the loop

        if (rawValue) {
            Send, {Raw}%comment%  ; Send the raw text if rawValue is true
        } else {
            Send, %comment%  ; Send the interpreted text if rawValue is false
        }
        Sleep, 250
        send, {enter}
        Sleep, 250
        send,{enter}
        Sleep, 250
        Send, ^{tab}  ; Send Ctrl+Tab
        Sleep, 250
    }

    ToolTip, Completed ; Display tooltip indicating loop completion
    SetTimer, RemoveToolTip, 2000  ; Remove the tooltip after 2 Seconds
}

findComment() { ; Start/Restart Loop
    ToolTip, Start ; Display tooltip indicating loop start
    SetTimer, RemoveToolTip, 2000  ; Remove the tooltip after 2 Seconds
    
    Loop, % totalAccount {  ; Start/Restart Loop
        if (!loopState)
            break  ; Exit the loop

        Send, ^f ; Send Ctrl+F
        Sleep, 100
        Send, ^v ; Send Ctrl+V
        Sleep, 100
        Send, {Enter}  ; Send Enter
        Sleep, 500
        Send, ^{tab}  ; Send Ctrl+Tab
        Sleep, 250
    }

    ToolTip, Completed ; Display tooltip indicating loop completion
    SetTimer, RemoveToolTip, 2000  ; Remove the tooltip after 2 Seconds
}

RemoveToolTip:
    ToolTip  ; Clear the tooltip
return
