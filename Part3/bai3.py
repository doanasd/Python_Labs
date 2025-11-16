# Part3 - Bài 3: Đếm số từ trong nhiều file
def count_words(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print("File", filename, "không tồn tại.")
        return
    print("File", filename, "có", len(contents.split()), "từ.")
if __name__=='__main__':
    files = input("Enter filenames separated by comma: ").split(',')
    files = [f.strip() for f in files if f.strip()!='']
    for fn in files:
        count_words(fn)
