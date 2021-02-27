import telegram
from os.path import exists, join
from Sastrawi import Stemmer
from .logging import logger


def LoadTemplate(path):
    result: str
    mode: telegram.ParseMode
    fn: str = path
    loc: str = 'kosong'
    basedir: str = 'qasbot\\templates\\'
    if path is None:
        url = ''
        path = ''
    else:
        url = path[1:]

    if path.startswith('@'):
        jenis = path[1:4]
        if jenis == "loc":
            loc = 'lokasi'
        if jenis == "obj":
            loc = 'objek'
        if jenis == "tim":
            loc = 'capram'
        if jenis == "sto":
            loc = 'kisah'
    elif path.startswith('#'):
        loc = 'utama'
    else:
        return path, telegram.ParseMode.MARKDOWN

    fn = join(basedir, loc, url)
    logger.info(f'membuka berkas {fn}')

    if exists(fn + '.md'):
        mode = telegram.ParseMode.MARKDOWN
        fn = fn + '.md'
    elif exists(fn + '.html'):
        mode = telegram.ParseMode.HTML
        fn = fn + '.html'
    else:
        return "_gagal menghubungkan ke server_", telegram.ParseMode.MARKDOWN

    with open(fn, mode='r') as f:
        result = f.read()

    return result, mode
