import tkinter
import win32gui
import time
import threading

win = tkinter.Tk()
label = tkinter.Label(win)
hwnd_title = dict()
window_yes = False


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
    # print({hwnd: win32gui.GetWindowText(hwnd)})


# 开始检查窗口是否创建
def if_Genshin_window():
    global window_yes
    while not window_yes:
        win32gui.EnumWindows(get_all_hwnd, 0)
        for pida in hwnd_title:
            if hwnd_title[pida] == "原神":
                window_yes = True
                print("原神，完全启动！ -> pid =", pida)
                time.sleep(3)
                win.quit()


def timer():
    global window_yes
    sec = 0
    while not window_yes:
        time.sleep(0.1)
        sec = sec + 1
        label["text"] = "请稍候\n原神，正在启动!"
        match int(sec/10) % 4:
            case 1: label["text"] = label["text"] + "\n"
            case 2: label["text"] = label["text"] + ".\n"
            case 3: label["text"] = label["text"] + "..\n"
            case 0: label["text"] = label["text"] + "...\n"
        label["text"] = label["text"] + str(sec/10)


def draw_window():
    win.title("Wait for Genshin...")
    win.geometry("1920x1080")  # 改？
    win.overrideredirect(True)
    win.configure(background='white')
    label["text"] = "请稍候\n原神，正在启动!\n0.0"
    label.pack()
    # 参考 https://zhuanlan.zhihu.com/p/342354790
    task1 = threading.Thread(target=if_Genshin_window)
    task1.start()
    task2 = threading.Thread(target=timer)
    task2.start()
    print("画窗口")
    win.mainloop()

