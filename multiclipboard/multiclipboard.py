# Beginner automation script to save and load multiple clipboard entries

import sys
import pyperclip as clipboard  
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open (filepath, "w") as f:
        json.dump(data, f)
        
def load_data(filepath):
    try: 
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        key = input ("Enter a key to save clipboard data: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA , data)
        print(f"Data saved: {data[key]}")
                 
    elif command == "load":
        key = input ("Enter a key to load clipboard data: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data loaded to clipboard")
        else:
            print("Key does not exist")
        
        data = load_data(SAVED_DATA)
        print("Loaded file:", data)

    elif command == "list":
        if data:
            print("Saved keys:")
            for key in data:
                print("-", key)
    else: 
        print("Unknown command") 
else:
    print("Please pass exactly one command")
            
