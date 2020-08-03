import utils
import json

flist = eval(open('nokey_list.json').read())
count = 0
cp_dict = {}
for f in flist:
    dirlist = f.split('/')
    save_name = dirlist[-2] + '_' + dirlist[-1][:-18]
    file = open(f).read()
    events = json.loads(file)
    cp_dict[save_name] = str(utils.get_chord_list(events['tracks']['chord']))
    if count%1000 == 0:
        print(count)
    count += 1

json_str = json.dumps(cp_dict, indent=4)

with open('cp_list.json', 'w') as json_file:
    json_file.write(json_str)
