def write_and_read():
    # 写文件
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("Hello Python!\nThis is a test file.")

    # 读文件
    with open("example.txt", "r", encoding="utf-8") as f:
        content = f.read()

    return content

print(write_and_read())
