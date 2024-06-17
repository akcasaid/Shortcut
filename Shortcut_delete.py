import os

def delete_empty_files(directory):
    # Belirtilen dizindeki tüm dosyaları ve alt dizinleri dolaşır
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Dosya boyutu 0 KB ise siler
            if os.path.getsize(file_path) == 0:
                os.remove(file_path)
                print(f"Silindi: {file_path}")


directory_path = "klasörün yolu"
delete_empty_files(directory_path)

'''

Belirten klasörde dolaşıp 0 KB olan dosyaları siler

'''
