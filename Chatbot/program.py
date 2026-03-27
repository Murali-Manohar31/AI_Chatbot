import pyautogui
import pyperclip
import time

# Small delay so you can switch to the target window
time.sleep(3)

# Step 1: Click on the whatsapp icon
pyautogui.click(1127, 1051)

# Small delay to ensure UI responds
time.sleep(1)

# Step 2: Drag to select text
pyautogui.moveTo(696, 200)
pyautogui.click()
pyautogui.dragTo(1850, 900, duration=2,button='left')  # smooth drag


# Step 3: Copy selected text
pyautogui.hotkey('ctrl', 'c')

# Wait for clipboard to update
time.sleep(1)

# Step 4: Get clipboard content
copied_text = pyperclip.paste()

# Print or use it
print("Copied Text:\n", copied_text)