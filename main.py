import zipfile
import os

zip_file_name = 'носорог.zip'


unzip_folder = 'unzip'


current_directory = os.path.dirname(os.path.abspath(__file__))


extract_to_path = os.path.join(current_directory, unzip_folder)


os.makedirs(extract_to_path, exist_ok=True)


with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
    for member in zip_ref.infolist():
        try:

            decoded_name = member.filename.encode('cp437').decode('cp866')
        except UnicodeDecodeError:
            try:
                decoded_name = member.filename.encode('cp437').decode('cp1251')
            except UnicodeDecodeError:

                decoded_name = member.filename.encode('cp437').decode('utf-8', errors='replace')
        
        extracted_path = os.path.join(extract_to_path, decoded_name)
        with open(extracted_path, 'wb') as f:
            f.write(zip_ref.read(member))

print(f"Архив распакован, путь: {extract_to_path}")
