import logging
import threading
import time


# 스레드에서 실행할 함수
def thread_func(name):
    logging.info("[Sub-Thread] %s: 시작합니다.", name)
    time.sleep(3)  # 3초간 sleep합니다.
    logging.info("[Sub-Thread] %s: 종료합니다.", name)


# 메인 영역
if __name__ == "__main__":  # main thread 흐름을 타는 시작점
    format = "%(asctime)s: %(message)s"  # Logging format 설정
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    a = threading.Thread(target=thread_func, args=('A',))

    logging.info("[Main-Thread] 쓰레드 시작 전")

    a.start()  # 서브 스레드 시작

    logging.info("[Main-Thread] 서브 쓰레드 종료를 기다립니다.")

    a.join()  # join() 추가!!!

    logging.info("[Main-Thread] 프로그램을 종료합니다.")