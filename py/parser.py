import json

def build_dex(mod='base'):
    data_file = open(f'_cache/{mod}/pokedex.ts')
    ts_data = data_file.readlines()
    data_file.close()
    # parse mons
    dex = {}
    dexlist = {
        "mons": []
    }
    in_mon = False
    is_cosmetic = False
    name = ''
    dname = False
    bst = {}
    types = []
    abil = {}
    for line in ts_data:
        if line.find('export const') > -1:
            continue
        elif line.find(': {') > -1 and in_mon == False: # open object
            in_mon = True
            name = line.split(':')[0].strip()
        elif in_mon and line.find('name') > -1: # explicit name
            dname = line[line.find('"')+1:]
            dname = dname[:dname.find('"')]
        elif in_mon and line.find('baseStats') > -1: # bst
            bst_s = line[line.find('{')+1:line.find('}')].split(',')
            for i in range(len(bst_s)):
                bst_s[i] = '"' + bst_s[i]
                bst_s[i] = bst_s[i].replace(' ', '').replace(':', '":')
            bst_s = '{' + ','.join(bst_s) + '}'
            bst = json.loads(bst_s)
        elif in_mon and line.find('types') > -1: # type
            types_s = line[line.find('[')+1:line.find(']')].replace(' ', '').replace('"', '')
            types = types_s.split(',')
        elif in_mon and line.find('abilities') > -1: # abilities
            abil_s = line[line.find('{')+1:line.find('}')]
            abil_s = abil_s.replace('0:', '"0":').replace('1:', '"1":').replace('H:', '"H":')
            abil_s = abil_s.split(',')
            abil_s = '{' + ','.join(abil_s) + '}'
            abil = json.loads(abil_s)
        elif in_mon and line.find('isCosmeticForme') > -1: # special for polished formes
            is_cosmetic = True
        elif in_mon and line.find('},') > -1:
            in_mon = False
            if is_cosmetic:
                is_cosmetic = False
                continue
            dexlist['mons'].append(name)
            dex[name] = {}
            dex[name]['bst'] = bst
            dex[name]['types'] = types
            dex[name]['abilities'] = abil
            if dname:
                dex[name]['name'] = dname
                dname = False
    return dex, dexlist

def build_learnset(dex, mod='base'):
    data_file = open(f'_cache/{mod}/learnsets.ts')
    ts_data = data_file.read()
    data_file.close()
    # parse learnset
    for mon, data in dex.items():
        slice_data = ts_data[ts_data.find(mon):]
        slice_data = slice_data[slice_data.find('learnset'):]
        slice_data = slice_data[slice_data.find('{')+1:slice_data.find('},')]
        slice_data = slice_data.split('],')
        for i in range(len(slice_data)):
            slice_data[i] = slice_data[i][:slice_data[i].find(':')]
            slice_data[i] = slice_data[i].strip().replace(' ', '')
        slice_data.pop() # remove empty last element
        dex[mon]['learnset'] = slice_data
    return dex
