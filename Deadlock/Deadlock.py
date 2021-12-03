import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time

class KakaoBank:
    # 공유 변수(value)
    def __init__(self):
        self.money = 0

    def deposit_1000won(self, user_name):
        print("Thread {}: 입금 시작합니다.".format(user_name))

        # 공유변수(money)에 스래드가 동시에 읽고 쓸 수 있다.
        local_data = self.money
        local_data += 1000
        time.sleep(0.1)
        self.money = local_data
        print("Thread {}: 입금 종료합니다.".format(user_name))


if __name__ == "__main__":
    bank = KakaoBank()

    print("카카오뱅크 계좌를 생성하였습니다. 현재 잔액: {}원".format(bank.money))

    with ThreadPoolExecutor(max_workers=2) as executor:
        for user_name in ['라이언', '무지', '어파치', 'test']:
            executor.submit(bank.deposit_1000won, user_name)

    print("카카오뱅크 계좌 현재 잔액: {}원".format(bank.money))