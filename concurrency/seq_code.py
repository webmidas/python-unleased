import time


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
    for i in range(6):
        sum_squares((i+1)*1000000)

    total_time =  time.time() - start_time
    print('Total time taken is ', round(total_time,2))

    sleep_start_time = time.time()

    for i in range(1,6):
        sleep_time(i)

    total_time_slept = time.time() - sleep_start_time

    print('total time slept is ', round(total_time_slept,2))



if __name__ == '__main__':
    main()