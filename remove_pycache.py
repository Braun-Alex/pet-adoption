import subprocess
import platform

def remove_pycache():
    os_name = platform.system()
    print(f"OS: {os_name}")
    
    if os_name == "Linux" or os_name == "Darwin":  # Darwin is for macOS, which uses similar commands to Linux
        try:
            # Remove __pycache__ directories
            subprocess.run(["find", ".", "-type", "d", "-name", "__pycache__", "-exec", "rm", "-r", "{}", "+"], check=True)
            
            # Remove .pyc files
            subprocess.run(["find", ".", "-type", "f", "-name", "*.pyc", "-delete"], check=True)
            
            print("Successfully removed __pycache__ directories and .pyc files on Linux/macOS.")
        except subprocess.CalledProcessError as e:
            print(f"Error during removal on Linux/macOS: {e}")
    
    elif os_name == "Windows":
        try:
            # Remove __pycache__ directories
            subprocess.run(["powershell", "-Command", 
                            "Get-ChildItem -Path . -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force"], check=True)
            
            # Remove .pyc files
            subprocess.run(["powershell", "-Command", 
                            "Get-ChildItem -Path . -Recurse -Filter '*.pyc' | Remove-Item -Force"], check=True)
            
            print("Successfully removed __pycache__ directories and .pyc files on Windows.")
        except subprocess.CalledProcessError as e:
            print(f"Error during removal on Windows: {e}")
    else:
        print(f"Unsupported OS: {os_name}")

if __name__ == "__main__":
    remove_pycache()
