import os
from pathlib import Path
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        if not raw_data:
            return 'utf-8'  # Порожній файл
    result = chardet.detect(raw_data)
    return result['encoding']

def convert_to_utf8_bom(file_path):
    encoding = detect_encoding(file_path)
    if encoding is None:
        print(f"[!] Не вдалося визначити кодування: {file_path}")
        return
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            content = f.read()
        with open(file_path, 'w', encoding='utf-8-sig') as f:
            f.write(content)
        print(f"[✔] Конвертовано: {file_path} ({encoding} → utf-8-sig)")
    except Exception as e:
        print(f"[✘] Помилка з файлом {file_path}: {e}")

def delete_all_bak_files(root_dir):
    for path in Path(root_dir).rglob('*.bak'):
        try:
            path.unlink()
            print(f"[🗑] Видалено резервну копію: {path}")
        except Exception as e:
            print(f"[✘] Помилка при видаленні {path}: {e}")

def process_all_md_files(root_dir):
    delete_all_bak_files(root_dir)
    for path in Path(root_dir).rglob('*.md'):
        convert_to_utf8_bom(path)

# Запуск
if __name__ == "__main__":
    process_all_md_files(".")
