# coding: UTF-8 
import sys
import time
from logging import getLogger, StreamHandler, DEBUG,FileHandler
import traceback

import tkinter
from tkinter import messagebox
import datetime,time

logger = getLogger(__name__)
file_handler = FileHandler('reminder.log', encoding='utf-8')
file_handler.setLevel(DEBUG)
logger.addHandler(file_handler)
logger.setLevel(DEBUG)
logger.propagate = False

st_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
logger.debug(f"[info] start {st_time}")

def main(tg_time,message,margin_minute = "5"):
    """reminder main program

    Args:
        tg_time (str): alarm time ex)"5:20"
        message (str): remind message
        margin_minute (str, optional): margin time . Defaults to "5".
    """
    wait_sec = cal_wait_sec(tg_time,margin_minute)
    if wait_sec > 0:
        logger.debug(f"[info] create reminder  message:{message},time:{tg_time},margin_minute{margin_minute}")
        # time.sleep(wait_sec)
        popup(message)
        logger.debug("[info] finish")
    else:
        logger.debug(f"[error] wait sec < 0 f{wait_sec}")
        sys.exit()

def popup(message):
    root = tkinter.Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    root.lift()
    root.focus_force()

    messagebox.showinfo("info",message)

def cal_wait_sec(tg_time,margin_minute = "5"):
    dt_now = datetime.datetime.now()
    dt_tg_temp = datetime.datetime.strptime(tg_time, '%H:%M')
    dt_tg = datetime.datetime(dt_now.year,dt_now.month,dt_now.day,dt_tg_temp.hour,dt_tg_temp.minute,0)
    wait_sec = (dt_tg-dt_now).total_seconds() + int(margin_minute)*60
    return wait_sec

if __name__ == "__main__":

    try:


        param = sys.argv

        if len(param) < 3:
            logger.debug("[erroe] you must input message(str) and time(**:**)")
            sys.exit()

        elif len(param) == 3:
            message = param[1]
            tg_time = param[2]
            margin_minute =  "5"
        else:
            message = param[1]
            tg_time = param[2]
            margin_minute = param[3]


        main(tg_time,message,margin_minute)
    except:
        logger.debug("error!")
        logger.info("bar", stack_info=True)
        logger.info("hmm", exc_info=True)