import psutil
import subprocess
from PIL import ImageGrab
import configparser
import time


import white_win

# 检测屏幕中间 500x500 区域是否全白
def is_screen_center_all_white(image):
    white_threshold = 200  # 阈值，用于判断颜色是否为白色
    center_width = 500
    center_height = 500
    start_x = (image.width - center_width) // 2
    start_y = (image.height - center_height) // 2

    for y in range(start_y, start_y + center_height):
        for x in range(start_x, start_x + center_width):
            pixel = image.getpixel((x, y))
            # 检查每个像素的 R、G、B 值是否都在白色阈值以上
            if pixel[0] < white_threshold or pixel[1] < white_threshold or pixel[2] < white_threshold:
                return False
    return True


# 启动原神
def start_genshinimpact(genshinimpact_path):
    subprocess.Popen(genshinimpact_path)
    return True


# 原神是否启动
def check_genshinimpect() -> bool:
    pl = psutil.pids()
    # time.sleep(0.25)
    for pid in pl:
        if psutil.Process(pid).name() == "YuanShen.exe":
            print("原神，已启动！ -> pid =", pid)
            # 绘制白屏+开始检查窗口是否创建
            white_win.draw_window()
            return True
    return False


# 主程序
def main():
    config = configparser.ConfigParser()
    config.read("config.ini", encoding="utf-8")

    # 原神路径、显示器分辨率
    genshinimpact_path = config.get("Paths", "genshinimpact_path")
    screen_width = 1920
    screen_height = 1080
    while True:
        screenshot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
        if is_screen_center_all_white(screenshot):
            if start_genshinimpact(genshinimpact_path):
                print("沃趣，白露原！")
                check_genshinimpect()
                print("完成")
            else:
                print("未能成功运行原神")
            break
        else:
            print("未检测到屏幕中间全白")
        time.sleep(0.5)


if __name__ == "__main__":
    main()