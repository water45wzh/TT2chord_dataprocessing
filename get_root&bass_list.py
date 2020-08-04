import utils
import json

flist = eval(open('nokey_list.json').read())
count = 0
rt_dict = {}
bs_dict = {}
for f in flist:
    dirlist = f.split('/')
    save_name = dirlist[-2] + '_' + dirlist[-1][:-18]
    file = open(f).read()
    events = json.loads(file)
    roots, basss = utils.get_rootnbass_list(events['tracks']['chord'])
    rt_dict[save_name] = str(roots)
    bs_dict[save_name] = str(basss)
    if count%1000 == 0:
        print(count)
    count += 1

json_str = json.dumps(rt_dict, indent=4)

with open('rootp_list.json', 'w') as json_file:
    json_file.write(json_str)

json_str = json.dumps(bs_dict, indent=4)

with open('bassp_list.json', 'w') as json_file:
    json_file.write(json_str)