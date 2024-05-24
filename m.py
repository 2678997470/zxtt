import os
import random
import string

def generate_random_file(count, suffixes, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for i in range(count):
        filename = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        suffix = random.choice(suffixes)
        size = random.randint(filesmini, filesmax)  # 随机文件大小（根据用户输入）
        filepath = os.path.join(output_dir, f"{filename}.{suffix}")
        with open(filepath, 'wb') as f:
            f.write(os.urandom(size))
        print(f"生成文件：{filepath} ({size} 字节)")

def list_files(output_dir):
    files = os.listdir(output_dir)
    print("目录下的文件：")
    for file in files:
        print(f"  {file}")

def delete_files(output_dir, suffixes):
    files = os.listdir(output_dir)
    for file in files:
        filepath = os.path.join(output_dir, file)
        filename, fileext = os.path.splitext(file)
        if fileext[1:] in suffixes:  # Check if the file extension is in the suffixes list
            os.remove(filepath)
            print(f"删除文件：{filepath}")
        else:
            print(f"跳过删除文件：{filepath}（非生成文件）")

# 设置参数
filesmini = int(input("文件最小（B）： ")) 
filesmax = int(input("文件最大（MB）： ")) * 1048576
count = int(input("文件数量： ")) # 文件数量
suffixes = [
    # 文本文件
    'txt', 'doc', 'docx', 'pdf', 'rtf',
    # 图片文件
    'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'ico',
    # 音频文件
    'p3', 'wav', 'ogg', 'aac', '4a', 'flac',
    # 视频文件
    'p4', 'avi', 'kv', 'ov', 'wmv', 'flv', 'webm',
    # 压缩包文件
    'zip', 'rar', '7z', 'gz', 'tar', 'bz2', 'xz'
]
output_dir = os.getcwd()  # 输出文件目录
import os
import random
import string
print("\n列出文件：")
list_files(output_dir)

print("\n删除文件？")
confirm = input("输入yes删除文件： ")
if confirm.lower() == 'yes':
    delete_files(output_dir, suffixes)
    print("文件已删除。")
else:
    print("文件未删除。")

def generate_random_file(count, suffixes, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for i in range(count):
        filename = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        suffix = random.choice(suffixes)
        size = random.randint(filesmini, filesmax)  # 随机文件大小（根据用户输入）
        filepath = os.path.join(output_dir, f"{filename}.{suffix}")
        with open(filepath, 'wb') as f:
            f.write(os.urandom(size))
        print(f"生成文件：{filepath} ({size} 字节)")

def list_files(output_dir):
    files = os.listdir(output_dir)
    print("目录下的文件：")
    for file in files:
        print(f"  {file}")

def delete_files(output_dir, suffixes):
    files = os.listdir(output_dir)
    for file in files:
        filepath = os.path.join(output_dir, file)
        filename, fileext = os.path.splitext(file)
        if fileext[1:] in suffixes:  # Check if the file extension is in the suffixes list
            os.remove(filepath)
            print(f"删除文件：{filepath}")
        else:
            print(f"跳过删除文件：{filepath}（非生成文件）")

# 设置参数
filesmini = int(input("文件最小（B）： ")) 
filesmax = int(input("文件最大（MB）： ")) * 1048576
count = int(input("文件数量： ")) # 文件数量
suffixes = [
    # 文本文件
    'txt', 'doc', 'docx', 'pdf', 'rtf',
    # 图片文件
    'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'ico',
    # 音频文件
    'p3', 'wav', 'ogg', 'aac', '4a', 'flac',
    # 视频文件
    'p4', 'avi', 'kv', 'ov', 'wmv', 'flv', 'webm',
    # 压缩包文件
    'zip', 'rar', '7z', 'gz', 'tar', 'bz2', 'xz'
]
output_dir = os.getcwd()  # 输出文件目录

generate_random_file(count, suffixes, output_dir)

print("\n列出文件：")
list_files(output_dir)

print("\n删除文件？")
confirm = input("输入yes删除文件： ")
if confirm.lower() == 'yes':
    delete_files(output_dir, suffixes)
    print("文件已删除。")
else:
    print("文件未删除。")
print("\n列出文件：")
list_files(output_dir)

print("\n删除文件？")
confirm = input("输入yes删除文件： ")
if confirm.lower() == 'yes':
    delete_files(output_dir, suffixes)
    print("文件已删除。")
else:
    print("文件未删除。")

generate_random_file(count, suffixes, output_dir)

print("\n列出文件：")
list_files(output_dir)