from time import time

import codecs
from selectolax.parser import HTMLParser
import warc
import gzip

def get_text_selectolax(html):
    tree = HTMLParser(html)

    if tree.body is None:
        return None

    for tag in tree.css('script'):
        tag.decompose()
    for tag in tree.css('style'):
        tag.decompose()

    text = tree.body.text(separator='\n')
    return text


def read_doc(record, parser=get_text_selectolax):
    url = record.url
    text = None

    if url:
        payload = record.payload.read()
        html = payload

        if len(html) > 0:
            text = parser(html)

    return url, text


def process_warc(file_name, parser):#, limit=10000):
    with gzip.open('TEXT-CONTENT.gz', 'wb') as tf:
        warc_file = warc.open(file_name, 'rb')
        t0 = time()
        n_documents = 0
        for i, record in enumerate(warc_file):
            #print(i)
            url, doc = read_doc(record, parser)
            
            if not doc or not url:
                continue
            else:
                tf.write(str(doc + "\n").encode('utf-8'))
            n_documents += 1
    
    warc_file.close()
    print('Parser: %s' % parser.__name__)
    print('Parsing took %s seconds and produced %s documents\n' % (time() - t0, n_documents))


file_name = "./autismodiario.org.warc.gz"

process_warc(file_name, get_text_selectolax)
