import os
import subprocess

def remove_pycache(directory):
    try:
        subprocess.run(["find", directory, "-type", "d", "-name", "__pycache__", "-exec", "rm", "-r", "{}", ";"])
    except Exception as e:
        print(f"Произошла ошибка при выполнении команды: {e}")

if __name__ == "__main__":
    target_directory = "."  # Укажите целевую директорию здесь
    remove_pycache(target_directory)
