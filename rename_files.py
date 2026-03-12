rename_files.py
import os

def rename_files(folder_path):
    files = os.listdir(folder_path)
    for index, file in enumerate(files):
        extension = file.split(".")[-1]
        new_name = f"arquivo_{index + 1}.{extension}"
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"{file} -> {new_name}")

folder = input("Digite o caminho da pasta: ")
rename_files(folder)
