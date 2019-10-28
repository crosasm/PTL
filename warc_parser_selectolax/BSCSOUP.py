''' 
   Beautiful Soup from BSC for BNE
   author: Joaquim More
   date: october 2019

   input: Gziped WARC file
   output: Json with Headers and Paragrapsh from WARC file
'''
import sys
import codecs
import warc
import gzip
import re
import json
import codecs
from selectolax.parser import HTMLParser
from time import time

def splitAtUpperCase(s):
    for i in range(len(s)-1)[::-1]:
        if s[i].isupper() and s[i+1].islower():
            s = s[:i]+' '+s[i:]
        if s[i].isupper() and s[i-1].islower():
            s = s[:i]+' '+s[i:]
    return " ".join(s.split())


#De momento no llamamos a esta función que limpia el texto.
def clean_text(text2clean):
    cleaned_text = text2clean.replace('\n', ' ')
    cleaned_text = cleaned_text.replace('\t', ' ')
    cleaned_text = re.sub(' +', ' ', cleaned_text)
    cleaned_text = splitAtUpperCase(cleaned_text) #PaísPortadaOpinión -> País Portada Opinión
    return cleaned_text
 

def parse_selectolax(html):
    tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a']
    tree = HTMLParser(html)
    paragraphs = []
    heads = []
    links = []
    for t in tags:
        selector = t
        for node in tree.css(selector):
            if selector == 'p':
                paragraphs.append(str(node.text()))
            if selector == 'h1':
                heads.append(str(node.text()))
            if selector == 'h2':
                heads.append(str(node.text()))
            if selector == 'h3':
                heads.append(str(node.text()))
            if selector == 'h4':
                heads.append(str(node.text()))
            if selector == 'h5':
                heads.append(str(node.text()))
            if selector == 'h6':
                heads.append(str(node.text()))
            if selector == 'a' and 'href' in node.attributes and 'title' in node.attributes:
                 links.append(str(node.attributes['href']) + "\|" + str(node.attributes['title'])) #url | titulo de noticia, etc. a la que la url apunta      

    return "<p>".join(paragraphs), "<h>".join(heads), "<t>".join(links)

def read_doc(record, parser=parse_selectolax):
    url = record.url
    paragraphs = None
    heads = None
    titles = None
    if url:
        payload = record.payload.read()
        html = payload
        if len(html) > 0:
            paragraphs, heads, titles = parser(html)
    return url, paragraphs, heads, titles

def process_warc(file_name, parser, file_data):
    warc_file = warc.open(file_name, 'rb')
    t0 = time()
    n_documents = 0
    for i, record in enumerate(warc_file):
        url, paragraphs, heads, titles = read_doc(record, parser)
        if not url:
            continue
        else:
            if len(paragraphs) >  3 or len(heads) > 3 or len(titles) > 3:
               n_documents += 1
               file_data[i] = {'url': url, 'p': paragraphs, 'heads': heads, 'titles': titles}


    print('Parser: %s' % parser.__name__)
    print('Parsing took %s seconds and produced %s documents' % (time() - t0, n_documents))


#Diccionario con la información
#file_data = {}    

#file_name = "./inputs/32970-10-20190730121106683-00000-HDLS011.bne.local.warc.gz"

#Proceso de limpiado
#process_warc(file_name, parse_selectolax)

#Output (formato JSON)
#output_json = '32970-10-20190730121106683-00000-HDLS011.bne.local.json'

#Escritura output
#with codecs.open(output_json, "w", encoding='utf-8') as write_file:
#    for record in file_data.values():
#        write_file.write(json.dumps(record, ensure_ascii=False))
#        write_file.write("\n")

def main():
    print("Main Program reading warcs")
    try:
          print(sys.argv[1])
    except:
          print("One WARC file expected")
    else:      
        print("Let's work with the WARC")
        
        file_data = {}
        file_name = sys.argv[1]
        output_json = file_name[:-8] + '.json'

        file_data = process_warc(file_name, parse_selectolax, file_data)
        
        with codecs.open(output_json, "w", encoding='utf-8') as write_file:
            for record in file_data.values():
                write_file.write(json.dumps(record, ensure_ascii=False))
                write_file.write("\n")

        print("File {} Processed...".format(file_name))

if __name__ == '__main__':
    main()
