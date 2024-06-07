import os
import glob
from multiprocessing import Process, Queue
import re

def count_numbers_in_file(file_path, queue):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    numbers = re.findall(r'\d+', text)
    number_count = len(numbers)
    queue.put(number_count)

def main():
    txt_files = glob.glob("*.txt")
    processes = []
    queue = Queue()
    
    for file_path in txt_files:
        process = Process(target=count_numbers_in_file, args=(file_path, queue))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    total_numbers = 0
    while not queue.empty():
        total_numbers += queue.get()
    
    print(f"Umumiy raqamlar soni: {total_numbers}")

if __name__ == "__main__":
    main()
