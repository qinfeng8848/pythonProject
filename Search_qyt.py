import os
os.mkdir('test')
os.chdir('test')
qytang1 = open('qytang1','w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()
qytang2 = open('qytang2','w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()
qytang3 = open('qytang3','w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()
os.mkdir('qytang4')
os.mkdir('qytang5')

print('文件中包含"qytang"关键字的文件为：')
print('方案一')

# 获取当前工作目录
current_directory = os.getcwd()
# 设置要搜索的目录
search_directory = 'test'
# 定义关键字
keyword = 'qytang'

# 循环遍历当前工作目录下的文件和目录
for file_or_dir in os.listdir(current_directory):
    # 拼接文件或目录的完整路径
    item_path = os.path.join(current_directory, file_or_dir)
    # 检查是否为文件并且在名为'test'的目录中
    if os.path.isfile(item_path) and search_directory in item_path:
        try:
            with open(item_path, 'r') as f:
                content = f.read()
                if keyword in content:
                    print(item_path)
        except Exception as e:
            pass


print('方案二')

# 设置要搜索的目录
search_directory = 'test'
# 定义关键字
keyword = 'qytang'
# 循环遍历当前工作目录及其子目录中的文件和目录
for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.isfile(file_path) and search_directory in file_path:
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    if keyword in content:
                        print(file_path)
            except Exception as e:
                pass

# 完成清理
os.chdir('..')
for root,dirs,files in os.walk('test',topdown=False):
    for name in files:
        os.remove(os.path.join(root,name))
    for name in dirs:
        os.rmdir(os.path.join(root,name))
os.removedirs('test')