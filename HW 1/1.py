import multiprocessing
from multiprocessing import shared_memory
import time


def producer(shm, msg):
    msg_bytes = msg.encode('utf-8')
    shm.buf[:len(msg_bytes)] = msg_bytes
    print(f"[Производитель] Отправлено: {msg}")


def consumer(shm, size):
    time.sleep(0.1)
    data = bytes(shm.buf[:size])
    if data:
        text = data.decode('utf-8')
        null_pos = text.find('\x00')
        if null_pos != -1:
            text = text[:null_pos]
        print(f"[Потребитель] Получено: {text}")


if __name__ == '__main__':
    message = "Привет от производителя"
    BUFFER_SIZE = len(message.encode('utf-8')) + 1
    shm = shared_memory.SharedMemory(create=True, size=BUFFER_SIZE)

    prod_process = multiprocessing.Process(target=producer, args=(shm, message))
    cons_process = multiprocessing.Process(target=consumer, args=(shm, BUFFER_SIZE))

    prod_process.start()
    cons_process.start()

    prod_process.join()
    cons_process.join()

    shm.close()
    shm.unlink()
