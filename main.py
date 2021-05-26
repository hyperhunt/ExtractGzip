import glob
import zipfile
import tarfile
import shutil
import os

# my_dir =
#

counter = 0


def func_un_zip(my_dir, my_zip):
    with zipfile.ZipFile(f'{my_dir}/{my_zip}') as zf:
        for zip_info in zf.infolist():
            if zip_info.filename[-1] == '/':
                continue
            zip_info.filename = os.path.basename(zip_info.filename)
            print("ZIP", zip_info.filename)
            zf.extract(zip_info, my_dir)

            if (zip_info.filename.split('.')[1] == 'zip') or (zip_info.filename.split('.')[1] == 'tar'):
                new_zip: str = zip_info.filename

                if zip_info.filename.split('.')[1] == f'{my_dir}/{my_zip}':
                    os.remove(f'{my_dir}/{my_zip}')

                if zip_info.filename.split('.')[0] == f'{my_dir}/empty.txt':
                    os.remove(f'{my_dir}/empty.txt')

                return new_zip


my_dir = "executed"
my_zip = "447509d6ee8b4cbaa96e3153ddddd7ba.zip"

while my_zip:
    counter += 1
    print(f'[ {counter} ]')
    # with  as zf:
    #     print(my_zip)
    #     print(f'{my_dir}/{my_zip}')

    if (my_zip.split('.')[1] == 'zip'):
        res = func_un_zip(my_dir, my_zip)
        print('[RESULT]', res)
        my_zip = res
    else:
        print('[END] ->', my_zip)

    if (my_zip.split('.')[1] == 'tar'):
        res = func_un_tar(my_dir, my_zip)
        print('[RESULT]', res)
        my_zip = res
    else:
        print('[END] ->', my_zip)

#     my_zip = my_zip_src

# func_un_zip(my_dir, my_zip)

# with zipfile.ZipFile(my_zip) as zip:
#     for zip_info in zip.infolist():
#         if zip_info.filename[-1] == '/':
#             continue
#         zip_info.filename = os.path.basename(zip_info.filename)
#         zip.extract(zip_info, my_dir)

# zip_file = zipfile.ZipFile(my_zip, 'r')
# for files in zip_file.namelist():
#     zip_file.extract(files, my_dir)
# zip_file.close()

# f_zip = zipfile.is_zipfile('447509d6ee8b4cbaa96e3153ddddd7ba.zip', 'r')

# src = "executed"
# ziptar = zipfile.ZipFile('447509d6ee8b4cbaa96e3153ddddd7ba.zip', 'r')
# print(f_zip)
# f_zip.printdir()
# print(type(f_zip.namelist()))

# nextZip = ziptar.namelist()[2].split("/")[1]
# print(nextZip)

# ziptar.printdir()
# ziptar.extract(ziptar.filename, 'ext')
# ziptar.extractall()

# ziptar = zipfile.ZipFile('447509d6ee8b4cbaa96e3153ddddd7ba/$nextZip', 'r')
# ziptar.extractall()

# f_zip = zipfile.ZipFile(nextZip, 'r')
# f_zip.extract()

# nextZip = f_zip.namelist()[2].split("/")[1]
# print(nextZip)

# f_zip.extract()
# f_zip.close()


#
# stories_zip = zipfile.ZipFile('447509d6ee8b4cbaa96e3153ddddd7ba.zip')
#
#
# def unzip_files(stories, counter=0):
#     fileSelect = stories.namelist()[2]
#
#     newFile = "empty"
#     while fileSelect.split("/")[1]:
#         newFile = fileSelect.split("/")[1]
#         print("->", newFile)
#         stories = zipfile.ZipFile(newFile)
#         # unzip_files(zipfile.ZipFile(newFile))
#         # unzip_files(zipfile.ZipFile(newFile.extract(newFile, 'ext')))
#         # stories.extract(newFile, 'ext')
#         counter += 1
#         print("[counter] ->", counter)
#
#         unzip_files(stories)
#
#     else:
#         print("NOT", newFile)
#
#
#     # stories.extract(newFile, 'ext')
#
#
# unzip_files(stories_zip)

# stories_zip.getinfo(file)
# stories_zip.extract(file, 'ext')

# for file in stories_zip.filename:
# data = file.split(',')
# print(file)
# print("[~]" + data[1])
# zipExt = data[1].split(".")
#
# if zipExt[0] != "" and zipExt[1] != "txt":
#     print("->", zipExt[1])
#     print("[~]" + data[1])
#
#     stories_zip.extract(file, 'ext')
