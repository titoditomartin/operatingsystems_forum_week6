import threading
import random

LOWER_NUM = 1
UPPER_NUM = 10000
BUFFER_SIZE = 100
MAX_COUNT = 10000

buffer = []
buffer_lock = threading.Lock()
all_file = "all.txt"
even_file = "even.txt"
odd_file = "odd.txt"

def producer():
    with open(all_file, 'w') as f_all:
        for _ in range(MAX_COUNT):
            num = random.randint(LOWER_NUM, UPPER_NUM)
            with buffer_lock:
                buffer.append(num)
                f_all.write(str(num) + '\n')

def consumer_even():
    while True:
        with buffer_lock:
            if buffer:
                num = buffer.pop()
                if num % 2 == 0:
                    with open(even_file, 'a') as f_even:
                        f_even.write(str(num) + '\n')
            else:
                break

def consumer_odd():
    while True:
        with buffer_lock:
            if buffer:
                num = buffer.pop()
                if num % 2 != 0:
                    with open(odd_file, 'a') as f_odd:
                        f_odd.write(str(num) + '\n')
            else:
                break

if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer)
    consumer_even_thread = threading.Thread(target=consumer_even)
    consumer_odd_thread = threading.Thread(target=consumer_odd)

    producer_thread.start()
    consumer_even_thread.start()
    consumer_odd_thread.start()

    producer_thread.join()
    consumer_even_thread.join()
    consumer_odd_thread.join()
