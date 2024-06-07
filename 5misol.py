import os
import glob
from multiprocessing import Process
import string

def remove_punctuation_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)
    output_file_path = f"cleaned_{os.path.basename(file_path)}"
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(cleaned_text)

def main():
    txt_files = glob.glob("*.txt")
    processes = []
    
    for file_path in txt_files:
        process = Process(target=remove_punctuation_from_file, args=(file_path,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    print(" txt fayllarni ichidan shart belilarni tozalandi.")

if __name__ == "__main__":
    main()
