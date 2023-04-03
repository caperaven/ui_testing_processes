import time
import psutil
def get_memory(driver, sleep=0):
    time.sleep(sleep)
    driver_pid = driver.service.process.pid
    process = psutil.Process(driver_pid)
    memory_info = process.memory_full_info()
    return memory_info.uss / 1024 / 1024