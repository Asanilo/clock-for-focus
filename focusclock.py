import time
import winsound

def pomodoro_timer(duration):
    # 将分钟转换为秒
    duration_seconds = duration * 60
    # 设置结束的时间戳
    end_time = time.time() + duration_seconds

    print("专注计时器已启动！")

    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        print(f"剩余时间: {remaining_seconds // 60} 分钟 {remaining_seconds % 60} 秒")
        time.sleep(1)

    print("时间到了！该休息一下了。")
    # 使用系统提示音提醒
    winsound.Beep(1000, 2000)  # 可以根据需要设置不同参数

if __name__ == '__main__':
    duration = int(input("请输入专注时长（分钟）："))  # 从用户输入获取专注时长
    pomodoro_timer(duration)
