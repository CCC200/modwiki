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
    print(f'Building site data:\n- {cache.mod} dex')
    dexMod, dexlist = parser.build_dex(cache.mod)
    
    
