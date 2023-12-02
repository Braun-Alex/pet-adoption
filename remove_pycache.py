import subprocess

def delete_pycache():
    try:
        # Используем subprocess для выполнения команды в терминале
        subprocess.run(["find", ".", "-type", "d", "-name", "__pycache__", "-exec", "rm", "-r", "{}", "+"])
        print("Папки __pycache__ успешно удалены.")
    except Exception as e:
        print(f"Произошла ошибка при удалении папок __pycache__: {str(e)}")

if __name__ == "__main__":
    delete_pycache()
