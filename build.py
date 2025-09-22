from py import cache, parser
import sys

print('===== SITE BUILDER =====')
update = False
if '-nodl' not in sys.argv:
    print('Caching data files:')
    cache.download()
    update = cache.compare()
    print('-----')
if update or '-nocache' in sys.argv:
    print(f'Building site data:\n- base dex')
    dexBase, dexListBase = parser.build_dex()
    print(f'- {cache.mod} dex')
    dexMod, dexListMod = parser.build_dex(cache.mod, dexBase)
    print(f'- {cache.mod} learnsets')
    dexMod = parser.build_learnset(dexMod, cache.mod)
    print('- base moves')
    movesBase, movesListBase = parser.build_moves()
    print(f'- {cache.mod} moves')
    movesMod, movesListMod = parser.build_moves(cache.mod, movesBase)
