# Part3 - Bài 4: Nén và giải nén tệp bằng Python (ví dụ sử dụng zipfile)
import zipfile, os
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
if __name__=='__main__':
    print('Sử dụng các hàm nen_file(given_zip, files) và giai_nen(zip, outdir)')
