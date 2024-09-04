import time
import pyperclip
import csv  # Using CSV for a more lightweight format


# Initialize a list to store clipboard history
clipboard_history = []


def save_to_csv(history, filename="clipboard_history.csv"):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Clipboard History"])
        writer.writerows(enumerate(history, start=1))


try:
    while True:
        current_clipboard = pyperclip.paste()

        # Check if the clipboard content has changed
        if current_clipboard not in clipboard_history:
            clipboard_history.append(current_clipboard)

            # Limit the history to a certain number of entries (e.g., 10)
            if len(clipboard_history) > 10:
                clipboard_history.pop(0)

            # Print the clipboard history
            print("Clipboard History:")
            for i, entry in enumerate(clipboard_history, start=1):
                print(f"{i}. {entry}")

        # Poll the clipboard at regular intervals (e.g., every 5 seconds)
        time.sleep(5)

except KeyboardInterrupt:
    # Handle the KeyboardInterrupt (Ctrl+C) to save the clipboard history to a CSV file
    print("Saving clipboard history to clipboard_history.csv...")
    save_to_csv(clipboard_history)
    print("Clipboard history saved as clipboard_history.csv")
except Exception as e:
    print(f"An error occurred: {e}")  # Basic error handling