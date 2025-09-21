import os
import sys

def start_screen_session():
    session_name = "my_python_session"
    command = f"screen -dmS {session_name} python3 {os.path.abspath(__file__)}"
    os.system(command)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "child":
        # Your main script logic here
        print("Executing Python code in screen session...")
        input("Hello")
        # Add your code here
    else:
        start_screen_session()
