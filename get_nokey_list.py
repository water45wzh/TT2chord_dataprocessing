import utils
import json
import os

path = 'datasets/event'

f_list = []

alphabet_dir = os.listdir(path)


count = 0
for ab in alphabet_dir:
    if ab!='.DS_Store':
        ab_path = path + "/" + ab
        author_dir = os.listdir(ab_path)
        for at in author_dir:
            if at != '.DS_Store':
                at_path = ab_path + "/" + at
                name_dir = os.listdir(at_path)
                for nm in name_dir:
                    if nm != '.DS_Store':
                        nm_path = at_path + "/" + nm
                        file_dir = os.listdir(nm_path)
                        for file in file_dir:
                            if file[-10:-5]=='nokey':
                                f_list.append(nm_path + "/" + file)
                                count += 1
                                if count%1000==0:
                                    print(count)

with open('nokey_list.json', 'w') as f:
    f.write(str(f_list))
    f.close()