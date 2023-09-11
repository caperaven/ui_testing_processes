from src.data import state
import asyncio
import sys
import subprocess
from api import Api
import tempfile
import os
from src.results_writer import set_results_folder


folder = tempfile.gettempdir()
set_results_folder(folder)
current_directory = os.getcwd()
chrome_path = "chrome/chromedriver.exe"
full_chrome_path = os.path.join(current_directory, chrome_path)
full_chrome_path = os.path.normpath(full_chrome_path)

try:
    crs = Api()
    asyncio.run(crs.init_driver("chrome", full_chrome_path))
    asyncio.run(crs.run_all())
except Exception as e:
    print(e)
finally:
    if crs is not None:
        crs.close()

        if "--auto-open" in sys.argv:
            path = state["folder"]
            subprocess.Popen(r'explorer /open,"{}"'.format(path))
            pass
