import sys
import os
from colorama import Fore

def visualize_directory_structure(path, indent=0):
    # Перевірка, чи існує директорія
    if not os.path.isdir(path):
        print(f"{path} не є дійсною директорією.")
        return
    # Використовуємо менеджер контексту with для роботи з файлом чи директорією
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(" " * indent +Fore.BLUE + f"[Директорія] {entry.name}")
                    # Рекурсивно викликаємо функцію для підкаталогів
                    visualize_directory_structure(entry.path, indent + 4)
                else:
                    print(" " * indent +Fore.GREEN + f"[Файл] {entry.name}")
    except PermissionError:
        print(f"Немає доступу до директорії: {path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до директорії як аргумент.")
    else:
        directory_path = sys.argv[1]
        visualize_directory_structure(directory_path)