from datetime import datetime
import multiprocessing

def read_info(filename):
    all_data = []
    with open(filename) as f:
        for line in f:
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]


# time_start = datetime.now()
# for filename in filenames:
#     read_info(filename)
# time_end = datetime.now()
# print(time_end-time_start)
# 0:00:02.176838 (линейный)

if __name__ == '__main__':
    time_start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    time_end = datetime.now()
    print(time_end-time_start)
#0:00:00.898916 (многопроцессный)
