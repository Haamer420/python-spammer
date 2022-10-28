import pyautogui
import time

msg = input("Enter the message : ")
n = input("How many times? : ")

print("t minus")

count = 5
while(count != 0):
    print(count)
    time.sleep(1)
    count -= 1

for i in range(0,int(n)):
    pyautogui.typewrite(msg + '\n')


# def spamText(text="", times = 10, delay=0, separator="\n"):
#     count = 5
#     while(count != 0):
#         print(f"Countdown {count}/{times}")
#         time.sleep(1)
#         count -= 1
    
#     for i in range(0, times):
#         pyautogui.typewrite(f"{text}{separator}")
#         time.sleep(delay)
    
#     print(f"Completed spamming '{text}' {times} times with {delay} delay separated with '{separator}'")

