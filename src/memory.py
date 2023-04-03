import psutil
def get_memory(driver):
    driver_pid = driver.service.process.pid
    process = psutil.Process(driver_pid)
    memory_info = process.memory_info()
    return memory_info.rss / 1048576