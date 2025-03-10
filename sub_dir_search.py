# C:\lge\workspace_py\tryexcept\sub_dir_search.py
import os

parampath = "C:/lge/workspace_py/"

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_name = os.path.join(dirname, filename)
            if os.path.isdir(full_name):
                search(full_name)
            else:
                ext = os.path.splitext(full_name)[-1]
                if ext == '.py':
                    print(full_name)
    except PermissionError:
        pass

def search_oswalk(dirname):
    for (path, dir, files) in os.walk(dirname):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.py':
                print("oswalk: %s/%s" % (path, filename))

search(parampath)
search_oswalk(parampath)