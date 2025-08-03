# Roblox Trigger Script

Este es un script simple en Python que detecta tonos de rojo en el centro de la pantalla y simula un clic cuando se encuentra. Fue desarrollado para propósitos de testeo y experimentación con detección de colores en entornos de juego.

## Advertencia
Este script **NO** debe usarse para hacer trampas o automatizar acciones en juegos como Project Remix de Roblox. Su uso en entornos competitivos viola los términos de servicio de Roblox y puede resultar en bans permanentes. Úsalo solo para fines educativos o de prueba en servidores privados.

## Requisitos
- Python 3.x
- Librerías: `pyautogui`, `keyboard`, `mss`, `pywin32` (instala con `pip install pyautogui keyboard mss pywin32`).
- Ejecuta como administrador en Windows para compatibilidad con fullscreen.

## Uso
1. Ejecuta el script: `python trigger.py`.
2. Presiona 'f' para activar/desactivar.
3. Presiona 'esc' para salir.
4. Apunta el cursor a un área roja para que detecte y clique (área de 5x5 píxeles en el centro).

## Notas
- Ajusta el `threshold` en `is_red` para variar la sensibilidad de colores.
- Usa con precaución; no me responsabilizo por consecuencias en juegos.
