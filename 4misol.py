import os
import glob
from multiprocessing import Process, Queue
import re

def find_longest_sentence_in_file(file_path, queue):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    sentences = re.split(r'[.!?]+', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    if sentences:
        longest_sentence = max(sentences, key=len)
        queue.put(longest_sentence)
    else:
        queue.put("")

def main():
    txt_files = glob.glob("*.txt")
    processes = []
    queue = Queue()
    
    for file_path in txt_files:
        process = Process(target=find_longest_sentence_in_file, args=(file_path, queue))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    longest_sentences = []
    while not queue.empty():
        longest_sentences.append(queue.get())
    
    if longest_sentences:
        overall_longest_sentence = max(longest_sentences, key=len)
        print(f"Eng uzun gap: {overall_longest_sentence}")
    else:
        print("Hech qanday gap topilmadi.")

if __name__ == "__main__":
    main()
