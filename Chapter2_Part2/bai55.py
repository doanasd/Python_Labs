# Nén và giải nén tệp bằng shutil và zipfile
# Lưu ý: cần có tệp để nén/giải nén

import shutil
import zipfile

def compress_file(file_path, output_path):
    shutil.make_archive(output_path, 'zip', file_path)
    print(f"File {file_path} đã được nén thành {output_path}.zip")

def decompress_file(file_path, output_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(output_path)
    print(f"File {file_path} đã được giải nén vào thư mục {output_path}")
