import utils
import json

flist = eval(open('nokey_list.json').read())
count = 0
for f in flist:
    dirlist = f.split('/')
    save_name = dirlist[-2] + '_' + dirlist[-1][:-18]
    file = open(f).read()
    events = json.loads(file)
    utils.proc_event_to_chord(events, save_path='chord_set/', name=save_name)
    if count%1000 == 0:
        print(count)
    count += 1