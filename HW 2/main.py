import os
import stat

def print_fs_info(path):
    """
    Выводит информацию о файловой системе, к которой принадлежит путь
    """
    try:
        st = os.statvfs(path)
        block_size = st.f_frsize
        total_blocks = st.f_blocks
        free_blocks = st.f_bfree
        avail_blocks = st.f_bavail
        total_inodes = st.f_files
        free_inodes = st.f_ffree
        avail_inodes = st.f_favail
        
        print("Информация о файловой системе")
        print(f"Путь: {path}")
        print(f"Базовый размер блока: {block_size} байт")
        print(f"Всего блоков: {total_blocks}")
        print(f"Свободных блоков: {free_blocks}")
        print(f"Доступно блоков для пользователя: {avail_blocks}")
        print(f"Всего inode: {total_inodes}")
        print(f"Свободных inode: {free_inodes}")
        print(f"Доступно inode для пользователя: {avail_inodes}")

    except Exception as e:
        print(f"Ошибка получения информации о ФС: {e}")

def print_file_info(filepath):
    """
    Выводит информацию о выбранном файле: inode, тип и атрибуты
    """
    try:
        st = os.stat(filepath)
        inode_number = st.st_ino
        file_type = stat.filemode(st.st_mode)
        permissions = oct(st.st_mode)[-3:]
        size = st.st_size
        mtime = st.st_mtime
        atime = st.st_atime
        ctime = st.st_ctime
        
        print("Информация о файле")
        print(f"Путь: {filepath}")
        print(f"Inode: {inode_number}")
        print(f"Тип файла: {file_type}")
        print(f"Права доступа: {permissions}")
        print(f"Размер: {size} байт")
        print(f"Время последнего изменения: {mtime}")
        print(f"Время последнего доступа: {atime}")
        print(f"Время создания метаданных: {ctime}")

    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")
    except Exception as e:
        print(f"Ошибка получения информации о файле: {e}")

if __name__ == '__main__':
    test_file = "/etc/hosts"
    print_fs_info(test_file)
    print() # разделитель для структуризации вывода
    print_file_info(test_file)
