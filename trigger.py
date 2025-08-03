import pyautogui
import time
import keyboard
import mss
import win32api
import win32con

reds = [
    (255, 115, 117),  # ff7375
    (229, 50, 50),    # e53232
    (126, 39, 29),    # 7e271d
    (255, 95, 101),   # ff5f65
    (221, 68, 71)     # dd4447
]

def is_red(pixel, threshold=80):
    for red in reds:
        # Distancia euclidiana en RGB
        dist = ((pixel[0] - red[0]) ** 2 + (pixel[1] - red[1]) ** 2 + (pixel[2] - red[2]) ** 2) ** 0.5
        if dist < threshold:
            return True
    return False

screen_width, screen_height = pyautogui.size()
center_x = screen_width // 2
center_y = screen_height // 2

area_size = 5
half_area = area_size // 2

running = False
print("Presiona 'f' para activar/desactivar el script. Presiona 'esc' para salir.")

while not keyboard.is_pressed('esc'):
    if keyboard.is_pressed('f'):
        running = not running
        time.sleep(0.2)
        print(f"Script activado: {running}")
        if running:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            time.sleep(0.05)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            print("Clic inicial realizado – mueve el mouse ligeramente si no responde.")
    
    if running:
        with mss.mss() as sct:
            monitor = {
                "top": center_y - half_area,
                "left": center_x - half_area,
                "width": area_size,
                "height": area_size
            }
            img = sct.grab(monitor)
            
            detected_red = False
            detected_colors = []
            
            for y in range(area_size):
                for x in range(area_size):
                    color = img.pixel(x, y)
                    detected_colors.append(color)
                    if is_red(color):
                        detected_red = True
                        break
                if detected_red:
                    break
            
            print(f"Colores en área: {detected_colors}")
            
            if detected_red:
                print("Rojo detectado en área! Haciendo clic...")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(0.05)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    
    time.sleep(0.01)

print("Script terminado.")