# get chord only with quality

import utils
import json

VAL_TO_NAME = {
    0:  ['C', 'C'],
    1:  ['Db', 'C#'],
    2:  ['D', 'D'],
    3:  ['Eb', 'D#'],
    4:  ['E', 'E'],
    5:  ['F', 'F'],
    6:  ['Gb', 'F#'],
    7:  ['G', 'G'],
    8:  ['Ab', 'G#'],
    9:  ['A', 'A'],
    10: ['Bb', 'A#'],
    11: ['B', 'B']
}

def get_chord_with_quality(data):
    triad_symbol = ['', 'm', 'o', 'ø', 'maj']

    if data['quality'] == triad_symbol[0] or data['quality'] == triad_symbol[4]:
        interval = [4, 3]
        str = to_name(data['root']) + triad_symbol[0]
    elif data['quality'] == triad_symbol[1]:
        interval = [3, 4]
        str = to_name(data['root']) + triad_symbol[1]
    elif data['quality'] == triad_symbol[2] or data['quality'] == triad_symbol[3]:
        interval = [3, 3]
        str = to_name(data['root']) + triad_symbol[2]
    else:
        print(data['quality'])
    comp = [data['root']]
    for i in interval:
        comp.append(i+comp[-1])
    return str, comp

def to_name(input_, sys=0):
    output = VAL_TO_NAME[(input_+120) % 12][sys]
    return output


def purify_events(events):
    # get chord only with quality
    for i in range(len(events['tracks']['chord'])):
        if events['tracks']['chord'][i] != None:
            str, comp = get_chord_with_quality(events['tracks']['chord'][i])
            events['tracks']['chord'][i]['composition'] = comp
            events['tracks']['chord'][i]['symbol'] = str
    return


flist = eval(open('nokey_list.json').read())
count = 0
for f in flist:
    dirlist = f.split('/')
    save_name = dirlist[-2] + '_' + dirlist[-1][:-18]
    file = open(f).read()
    events = json.loads(file)
    purify_events(events)
    utils.proc_event_to_chord(events, save_path='chord_with_quality_set/', name=save_name)
    if count%1000 == 0:
        print(count)
    count += 1
