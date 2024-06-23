import pytchat
import re as regex

def contains_valid_numbers(data):
    # Regular expression to match the entire string if it contains only valid numbers (positive or negative)
    pattern = r'^-?\b(?:[1-9]\d*|0)\b$'

    # Check if the entire string matches the pattern for each number
    matches = regex.findall(pattern, data)

    # Convert match object to boolean (True if match found, False otherwise)
    return matches and ''.join(matches) == data


# Replace with the video ID of the YouTube live stream
VIDEO_ID = 'tSG2fb3aQwg'

chat = pytchat.create(video_id=VIDEO_ID)

while chat.is_alive():
    for data in chat.get().sync_items():
        message = data.message
        if contains_valid_numbers(message) and 0 <= int(message) <= 250 and message != "-0":
            print(f"Message is a number within the range 0 to 250: {message}")
        else:
            print(f"Result is False: {message}")

