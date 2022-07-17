import pathlib
import re
from pathlib import Path
import shutil
import sys

def normalize(text):
    trans_map = {
    ord('а'): 'a', ord('А'): 'A', ord('б'): 'b', ord('Б'): 'B', 
    ord('в'): 'v', ord('В'): 'V', ord('г'): 'g', ord('Г'): 'G', 
    ord('д'): 'd', ord('Д'): 'D', ord('е'): 'e', ord('Е'): 'E', 
    ord('ё'): 'e', ord('Ë'): 'E', ord('ж'): 'j', ord('Ж'): 'J', 
    ord('з'): 'z', ord('З'): 'Z', ord('и'): 'i', ord('И'): 'I', 
    ord('й'): 'j', ord('Й'): 'J', ord('к'): 'k', ord('К'): 'K', 
    ord('л'): 'l', ord('Л'): 'L', ord('м'): 'm', ord('М'): 'M', 
    ord('н'): 'n', ord('Н'): 'N', ord('о'): 'o', ord('О'): 'O', 
    ord('п'): 'p', ord('П'): 'P', ord('р'): 'r', ord('Р'): 'R', 
    ord('с'): 's', ord('С'): 'S', ord('т'): 't', ord('Т'): 'T', 
    ord('у'): 'u', ord('У'): 'U', ord('ф'): 'f', ord('Ф'): 'F', 
    ord('х'): 'h', ord('Х'): 'H', ord('ц'): 'ts', ord('Ц'): 'TS', 
    ord('ч'): 'ch', ord('Ч'): 'CH', ord('ш'): 'sh', ord('Ш'): 'SH', 
    ord('щ'): 'sch', ord('Щ'): 'SCH', ord('ъ'): '', ord('Ъ'): '', 
    ord('ы'): 'y', ord('Ы'): 'Y', ord('ь'): '', ord('Ь'): '', 
    ord('э'): 'e', ord('Э'): 'E', ord('ю'): 'yu', ord('Ю'): 'YU', 
    ord('я'): 'ja', ord('Я'): 'JA', ord('є'): 'ye', ord('Є'): 'YE', 
    ord('ї'): 'ji', ord('Ї'): 'JI', ord('ї'): 'і', ord('І'): 'I', 
    ord('ґ'): 'g', ord('Ґ'): 'G', ord('.'): '.'
    }
    trans_text = text.translate(trans_map)
    trans_text = re.sub(r'[\.]\W', '_', trans_text)
    return trans_text

def folder_processing_logic(path_from_argv):
    video_formats = ['avi', 'mp4', 'mov', 'mkv']
    image_formats = ['jpeg', 'png', 'jpg', 'svg']
    document_formats = ['doc', 'docx', 'txt', ' rtf', 'pdf', 'xls', 'xls', 'pptx', 'csv', 'tsv']
    audio_formats = ['mp3', 'ogg', 'wav', 'amr', 'flac']
    archive_formats = ['zip', 'gz', 'tar']
    py_formats = ['py']
    ignore_list = ['archives', 'video', 'audio', 'documents', 'images', 'unknow', 'python_files']
    path = pathlib.Path(path_from_argv)
    if path.exists():
        for el in path.iterdir():                           # ітеруємось по всім файлам і папкам
            if el.is_dir():
                if el.name in ignore_list:
                    continue                                # якщо ми натрапляєм на свою створену ж папку, то пропускаєм ітерацію
                folder_processing_logic(el.absolute())      # рекурсія функції переміщення файлів по відповідним папкам (для вкладених папок)
            else:
                if el.name.split('.')[-1] in py_formats:
                    pathlib.Path(python_files_p).mkdir(parents=True, exist_ok=True)
                    el.replace(python_files_p / normalize(el.name))
                    # shutil.move(el.absolute(), python_files_p)
                elif el.name.split('.')[-1] in video_formats:
                    pathlib.Path(video_p).mkdir(parents=True, exist_ok=True)
                    el.replace(video_p / normalize(el.name))
                    # shutil.move(el.absolute(), video_p)
                elif el.name.split('.')[-1] in audio_formats:
                    pathlib.Path(audio_p).mkdir(parents=True, exist_ok=True)
                    el.replace(audio_p / normalize(el.name))
                    # shutil.move(el.absolute(), audio_p)
                elif el.name.split('.')[-1] in image_formats:
                    pathlib.Path(images_p).mkdir(parents=True, exist_ok=True)
                    el.replace(images_p / normalize(el.name))
                    # shutil.move(el.absolute(), images_p)
                elif el.name.split('.')[-1] in document_formats:
                    pathlib.Path(documents_p).mkdir(parents=True, exist_ok=True)
                    el.replace(documents_p / normalize(el.name))
                    # shutil.move(el.absolute(), documents_p)
                elif el.name.split('.')[-1] in archive_formats:
                    pathlib.Path(archives_p).mkdir(parents=True, exist_ok=True)
                    el.replace(archives_p / normalize(el.name))
                    # shutil.move(el.absolute(), archives_p)
                else:
                    pathlib.Path(unknow_p).mkdir(parents=True, exist_ok=True)
                    # el.replace(unknow_p / normalize(el.name))
                    shutil.move(el.absolute(), unknow_p)
      
    else:
        print(f"{path.absolute()} - такий шлях не існує")

def delete_other_dir(path_from_argv):
    path = pathlib.Path(path_from_argv)
    ignore_list = ['archives', 'video', 'audio', 'documents', 'images', 'unknow', 'python_files']
    for i in path.iterdir():
            if i.is_dir():
                if i.name in ignore_list:
                    continue
                else:
                    i.rmdir()

def unp_archives(archives_p):
    path = Path(archives_p)
    
    for n in path.iterdir():
        try:
            index = n.name.index('.')
            fold_name = n.name[:index]                                                     # створили найменування папки без розширення
            # pathlib.Path(archives_p / fold_name).mkdir(parents=True, exist_ok=True)        # створили папку для архіву
            shutil.unpack_archive(n, archives_p)
        except:
            continue

def zvit(path_from_argv):

    video_list = []
    doc_list = []
    audio_list = []
    archive_list = []
    images_list = []
    py_list = []
    un_list = []
    list_k = []
    list_u = []
    path = Path(path_from_argv)
    for n in path.iterdir():
        if n.name == "video":
            for i in n.iterdir():
                video_list.append(i.name)
                list_k.append(i.name.split(".")[-1])
        elif n.name == "documents":
            for i in n.iterdir():
                doc_list.append(i.name)
                list_k.append(i.name.split(".")[-1])
        elif n.name == "archives":
            for i in n.iterdir():
                if i.is_dir():
                    continue
                archive_list.append(i.name)
                list_k.append(i.name.split(".")[-1])
        elif n.name == "images":
            for i in n.iterdir():
                images_list.append(i.name)
                list_k.append(i.name.split(".")[-1])
        elif n.name == "documents":
            for i in n.iterdir():
                doc_list.append(i.name)
                list_k.append(i.name.split(".")[-1])
        elif n.name == "python_files":
            for i in n.iterdir():
                py_list.append(i.name)
                list_k.append(i.name.split(".")[-1])
        elif n.name == "unknow":
            for i in n.iterdir():
                un_list.append(i.name)
                list_u.append(i.name.split(".")[-1])



    print("\n"+"_"*63+"\n\n"+"        welcome to homemade parser"+"\n"+"_"*63+"\n")
    print(f"Video files: {video_list}")
    print(f"Documents files: {doc_list}")
    print(f"Python files: {py_list}")
    print(f"Audio files: {audio_list}")
    print(f"Image files: {images_list}")
    print(f"Archives files: {archive_list}")
    print(f"Unknown files: {un_list}")
    print(f"\nNotable extensions: {list_k}")
    print(f"Unknown extensions: {list_u}")
    print("_"*63+"\n\n")

    


try:
    path_from_argv = sys.argv[1]
except IndexError:
    print("_"*63+"\n"+"Ви не ввели шлях до папки!\nВведіть через командну строку: python3 sort_file.py path/folder \n(path/folder - шлях до папки яку потрібно сортувати)"+"\n"+"_"*63)

path = pathlib.Path(path_from_argv)
python_files_p = path / 'python_files'                  # set static urls
video_p = path / 'video'
audio_p = path / 'audio'
images_p = path / 'images'
documents_p = path / 'documents'
archives_p = path / 'archives'
unknow_p = path / 'unknow'


folder_processing_logic(path_from_argv)                 # запуск функції сортування файлів
delete_other_dir(path_from_argv)                        # запуск функції видалення пустих зайвих папок
unp_archives(archives_p)                                # запуск функції розархівування архівів в папці з архівами
zvit(path_from_argv)                                    # формування звіту в консоль


