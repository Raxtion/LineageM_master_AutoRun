import datetime
import time

class Timer:
    def __init__(self):
        self.tmToTimePoint = 0.0
        self.tmGoTimePoint = 0.0

    def timeup(self):
        bIsTimeUp = False
        if time.time() >= self.tmToTimePoint:
            bIsTimeUp = True
        return bIsTimeUp

    def timestart(self, millisecond=0):
        tdInput = datetime.timedelta(0, 0, 0, millisecond, 0, 0)
        self.tmToTimePoint = time.time() + tdInput.total_seconds()
        self.tmGoTimePoint = time.time()

    def timepass(self):
        return (time.time() - self.tmGoTimePoint) * 1000


if __name__ == '__main__':
    ct = Timer()
    ct.timestart(10000)
    while True:
        if ct.timeup():
            break
        print('Time Now:  ', time.time())
        print('Time Pass: ', ct.timepass())
        time.sleep(1)
    print('process end')
