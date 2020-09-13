import os
import sys
import glob
import shutil

def bulk_merge(source_folder,dest_folder,new_file_name):
    print(f'{source_folder} and {dest_folder}')

    if os.path.exists(dest_folder):
        return f'dest folder {dest_folder} already exists'
    else: 
        os.makedirs(dest_folder)
    path=source_folder + '/*.txt'
    print(path)
    for fname in glob.glob(path):
        shutil.copy(fname,dest_folder)
    
    counter=0
    path=dest_folder + '/*.txt'
    for fname in glob.glob(path):
        os.rename(fname,dest_folder+'/'+new_file_name+str(counter)+'.txt')
        print('hi')
        counter+=1

if __name__ == '__main__':
    source_folder=sys.argv[1]
    dest_folder=sys.argv[2]
    bulk_merge(source_folder,dest_folder,'test')
    print('Task completed!')