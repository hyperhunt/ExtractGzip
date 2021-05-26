import os
import shutil
import zipfile
import tarfile

# Recursively extract files from archives.

path_dir = '/home/spark/PycharmProjects/ExtractGzip/unpack/'


# print(os.listdir(path))
#
# for i in os.listdir(path):
#     print(i, type(i))
#     print(path + i)
#     print(os.path.isfile(path + i))


def unpack_zip(path, i):
    with zipfile.ZipFile(f'{path}{i}') as zf:
        for zip_info in zf.infolist():
            new_archive = zip_info.filename

            if zip_info.filename[-1] == '/':
                # Exclude root '/' file
                continue
            # print('zip_info ->', zip_info)
            zf.extract(zip_info, path)
            print("ZIP", zip_info.filename)

            # print(f'-> {path}{zip_info.filename}')
            if os.path.isfile(path + zip_info.filename):
                if (zip_info.filename.split('.')[1] == 'zip') or (zip_info.filename.split('.')[1] == 'tar'):
                    shutil.copy2(f'{path}{zip_info.filename}', path)

    del_dir = zip_info.filename.split("/")[0]
    print("ZIP ~~~", path + del_dir)
    delete_dir(path + del_dir)
    print("ZIP i ->", i)
    delete_file(path, i)

    return new_archive


def unpack_tar(path, i):
    with tarfile.open(f'{path}{i}') as tar:
        for tarinfo in tar:
            new_archive = tarinfo.name
            print('tarinfo:', tarinfo.name)
            if tarinfo.name[-1] == '/':
                # Exclude root '/' file
                continue
            tar.extract(tarinfo, path)

            # tarinfo.name
            # 46980249b74048838629d39be9278bb7 / empty.txt
            # print('tarinfo.name', tarinfo.name)

            # print('os.path.isfile(tarinfo.name)', os.path.isfile(path + tarinfo.name))

            if os.path.isfile(path + tarinfo.name):
                print('COPY TAR:', f'{path}{tarinfo.name}', '###')

                if (tarinfo.name.split('.')[1] == 'tar') or (tarinfo.name.split('.')[1] == 'zip'):
                    shutil.copy2(f'{path}{tarinfo.name}', path)

                # print('=== tarinfo.name ===', tarinfo.name.split('/')[1])

                if tarinfo.name.split('/')[1] == 'answer.txt':
                    shutil.copy2(f'{path}{tarinfo.name}', '/home/spark/PycharmProjects/ExtractGzip/answer/')



    del_dir = tarinfo.name.split("/")[0]
    print("TAR ~~~", path + del_dir)
    delete_dir(path + del_dir)
    print("TAR i ->", i)
    delete_file(path, i)

    return new_archive


def delete_dir(f):
    print('# DELETE DIR #', f)
    # os.rmdir(path + zip_info)
    shutil.rmtree(f)


def delete_file(path, i):
    print('# DELETE FILE #', i)
    os.remove(f'{path}{i}')


def obxod(path, level=1):
    print('Level=', level, 'Content:', os.listdir(path))

    new_arch = []

    for i in os.listdir(path):

        if os.path.isfile(path + i):
            if i.split('.')[1] == 'zip':
                unpack_zip(path, i)
                print('zip res: ', os.listdir(path))

            if i.split('.')[1] == 'tar':
                unpack_tar(path, i)
                print('tar res: ', os.listdir(path))

            if i.split('.')[1] == 'txt':
                delete_file(path, i)

        # if os.path.isdir(path + i):
        #     print('Спускаемся', path + i)
        #     obxod(path + i, level + 1)
        #     print('Возвращаемся в:', path)

        for i in os.listdir(path):
            if os.path.isfile(i):
                if (i.split('.')[1] == 'zip') or (i.split('.')[1] == 'tar'):
                    print('#->#', i)
                    new_arch.append(i)

    return new_arch

    # zip_boolean = True
    #
    # while zip_boolean:


# print(os.listdir(path_dir))

if __name__ == '__main__':
    # obxod(path_dir)
    # print(os.listdir(path_dir))
    counter = 0
    while os.listdir(path_dir):
        obxod(path_dir)
        counter += 1

    print(counter)

# for i in os.listdir(path_dir):
#     if os.path.isfile(i):
#         if (i.split('.')[1] == 'zip') or (i.split('.')[1] == 'tar'):
#             obxod(path_dir)
#         else:
#             zip_boolean = False
#     else:
#         continue
