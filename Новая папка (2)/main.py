import random
import time
import os

# Списоки символов для анимации
symbols = ["0", "1", "X", "Y", "Z", "A", "B", "C", "Ø", "Æ", " ", " ", " "]

# Очистка экрана перед стартом
os.system('cls' if os.name == 'nt' else 'clear')

# Получаем размер окна терминала (по умолчанию 80x24, если не определился)
try:
    columns, rows = os.get_terminal_size()
except OSError:
    columns, rows = 80, 24

# Инициализируем текущие позиции «капель»
drops = [0] * columns

print("\033[32m") # Включаем зеленый цвет текста в терминале

while True:
    line = ""
    for i in range(columns):
        # Случайно решаем, пойдет ли капля вниз
        if drops[i] == 0 and random.random() > 0.975:
            drops[i] = random.randint(1, rows)
            
        if drops[i] > 0:
            line += random.choice(symbols)
            drops[i] -= 1
        else:
            line += " "
            
    print(line)
    time.sleep(0.05)  # Скорость падения
