import os
import glob
from multiprocessing import Process, Queue

def count_words_in_file(file_path, queue):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    word_count = len(text.split())
    queue.put(word_count)

def main():
    txt_files = glob.glob("*.txt")
    processes = []
    queue = Queue()
    
    for file_path in txt_files:
        process = Process(target=count_words_in_file, args=(file_path, queue))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    total_words = 0
    while not queue.empty():
        total_words += queue.get()
    
    print(f"Umumiy so'zlar soni: {total_words}")

if __name__ == "__main__":
    main()
