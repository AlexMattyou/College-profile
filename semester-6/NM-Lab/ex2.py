from datetime import datetime

def capture_input():
    while True:
        user_input = input("Please type something (type 'exit' to stop): ")
        if user_input.lower() == 'exit':
            print("Exiting input capture.")
            break
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("keylog.txt", "a") as f:
            f.write(f"[{timestamp}] {user_input}\n")
        print(f"Captured input: {user_input}")

capture_input()
'''
Please type something (type 'exit' to stop): hello
Captured input: hello
Please type something (type 'exit' to stop): world
Captured input: world
Please type something (type 'exit' to stop): exit
Exiting input capture.


'''