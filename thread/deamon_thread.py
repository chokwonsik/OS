import logging
import threading
import time


# 스레드 실행 함수
def work(name, d):
    logging.info("[Sub-Thread] %s: 시작합니다.", name)

    for i in d:
        print(name,i)

    logging.info("[Sub-Thread %s: 종료합니다.", name)


# 메인 영역
if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # daemon을 True로 줍니다.
    x = threading.Thread(target=work, args=('A', range(100)), daemon=True)
    y = threading.Thread(target=work, args=('B', range(100)), daemon=True)

    logging.info("[Main-Thread] 쓰레드 실행 전")

    # 서브 스레드 시작
    x.start()
    y.start()

    logging.info("[Main-Thread] 프로그램을 종료합니다.")