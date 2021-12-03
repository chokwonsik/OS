import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading


class KakaoBank:
    # 공유 변수(value)
    def __init__(self):
        self.money = 0
        self._lock = threading.Lock()

    # 변수 업데이트 함수
    # 스택 영역에 저장 - 자기 자신의 영역
    def deposit_1000won(self, user_name):
        print("Thread {}: 입금 시작합니다.".format(user_name))

        self._lock.acquire()  # Lock 획득

        local_copy = self.money
        local_copy += 1000
        time.sleep(0.1)
        self.money = local_copy

        self._lock.release()  # Lock 반환

        print("Thread {}: 입금 종료합니다.".format(user_name))


if __name__ == "__main__":
    bank = KakaoBank()

    print("카카오뱅크 계좌를 생성하였습니다. 현재 잔액: {}원".format(bank.money))

    with ThreadPoolExecutor(max_workers=2) as executor:
        for user_name in ['라이언', '무지', '어파치']:
            executor.submit(bank.deposit_1000won, user_name)

    print("카카오뱅크 계좌 현재 잔액: {}원".format(bank.money))