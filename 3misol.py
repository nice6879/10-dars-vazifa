import os
import glob
from multiprocessing import Process, Queue
import re

def count_sentences_in_file(file_path, queue):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    sentences = re.split(r'[.!?]+', text)
    sentences = [sentence for sentence in sentences if sentence.strip()]
    sentence_count = len(sentences)
    queue.put(sentence_count)

def main():
    txt_files = glob.glob("*.txt")
    processes = []
    queue = Queue()
    
    for file_path in txt_files:
        process = Process(target=count_sentences_in_file, args=(file_path, queue))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    total_sentences = 0
    while not queue.empty():
        total_sentences += queue.get()
    
    print(f"Umumiy gaplar soni: {total_sentences}")

if __name__ == "__main__":
    main()
