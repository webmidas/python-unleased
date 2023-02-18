import time
import threading


def sum_squares(n):
    final_sum = 0
    for i in range(n):
        final_sum += i**2

    print(final_sum)


def sleep_time(n):
    time.sleep(n)

def main():
    start_time = time.time()
    print('Started here')
    current_threads = []

    for i in range(6):
        num = (i+1)*1000000
        t = threading.Thread(target=sum_squares, args=(num,))
        t.start()
        current_threads.append(t)
        #sum_squares(num)

    for i in range(len(current_threads)):
        current_threads[i].join()

    total_time =  time.time() - start_time
    print('Total time taken is ', round(total_time,2))

    sleep_start_time = time.time()
    current_threads = []

    for i in range(1,6):
        t = threading.Thread(target=sleep_time, args=(i,))
        t.start()
        current_threads.append(t)
        #sleep_time(i)

    for i in range(len(current_threads)):
        current_threads[i].join()
    total_time_slept = time.time() - sleep_start_time

    print('total time slept is ', round(total_time_slept,2))



if __name__ == '__main__':
    main()