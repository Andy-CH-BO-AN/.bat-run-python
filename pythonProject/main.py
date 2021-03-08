# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import datetime


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(10):
        print_hi(time.strftime('_%H_%M_%S', time.localtime(time.time())))
        with open(f"asb{time.strftime('_%H_%M_%S', time.localtime(time.time()))}.txt", 'w') as f:
            f.close()
        time.sleep(2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
