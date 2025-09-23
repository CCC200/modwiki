import os, shutil

# config vars
site_title = 'Polished Wiki'

__header_data = False

def build_header():
    f = open('pages/site-header.html')
    _head = f.read()
    f.close()
    return _head

def build_index(dex):
    print('- index')
    f = open('pages/index.html')
    html = f.read()
    f.close()
    # insert headers
    html = __insert_header(html)
    html = __insert_title(html)
    html = html.replace('SITE_INDEX', '')
    # parse mon list
    buf = '<div class="link-head"><h2 id="left">Pokemon</h2><h2 id="right">Tier</h2></div>'
    buf += '<div class="link-list" align="center">'
    for mon, data in dex.items():
        buf += f'<a href="dex/{mon}"><h4>{data['name']}</h4></a>'
    buf += "</div>"
    html = html.replace(__comment_tag('PAGE_BODY'), buf)
    __save(html, 'index.html')

def copy_assets():
    print('- assets')
    shutil.copytree('pages/style', '_site/style', dirs_exist_ok=True)


def __comment_tag(n):
    return f'<!-- {n} -->'

def __insert_header(html):
    html = html.replace(__comment_tag('SITE_HEADER'), __header_data)
    return html

def __insert_title(html):
    html = html.replace('SITE_TITLE', site_title)
    return html

def __save(data, n, path=''):
    if not os.path.isdir('_site'):
        os.mkdir('_site')
    html = open(f'_site/{path}/{n}', 'w')
    html.write(data)
    html.close()
