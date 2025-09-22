import json

def build_dex(pack='base'):
    data_file = open(f'_cache/{pack}/pokedex.ts')
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
    bst = {}
    types = []
    abil = {}
    for line in ts_data:
        if line.find('export const') > -1:
            continue
        elif line.find(': {') > -1 and in_mon == False: # open object
            in_mon = True
            name = line.split(':')[0].strip()
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
    return dex, dexlist

