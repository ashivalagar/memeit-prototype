def give_path(path):
    import os
    paths=[]
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if (filename.endswith('.jpg') or filename.endswith('.png')):
                paths.append(os.sep.join([dirpath, filename]))

    return(paths)
