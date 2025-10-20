# Bài 4: Nén và giải nén file bằng Python

import zipfile
import os

def nen_file(ten_zip, danh_sach_file):
    with zipfile.ZipFile(ten_zip, 'w') as zipf:
        for file in danh_sach_file:
            if os.path.exists(file):
                zipf.write(file)
                print(f"Đã nén: {file}")
            else:
                print(f"Tệp {file} không tồn tại.")

def giai_nen(ten_zip, thu_muc_dich):
    with zipfile.ZipFile(ten_zip, 'r') as zipf:
        zipf.extractall(thu_muc_dich)
        print(f"Đã giải nén vào: {thu_muc_dich}")

# Ví dụ sử dụng
if __name__ == "__main__":
    danh_sach_file = ['f1.txt', 'f2.txt']
    ten_zip = 'files.zip'
    thu_muc_dich = 'output_folder'

    nen_file(ten_zip, danh_sach_file)
    giai_nen(ten_zip, thu_muc_dich)
