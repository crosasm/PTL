import sys
import os
import numpy as np

def count_ocurrences(filename):
    total_ocurrences = 0
    total_urls = 0

    url_ocurrences = {}
    f = open(filename, 'r')
    fo = open(filename[:-3]+'csv', 'w')
    for line in f:
        url = (line.split(':')[0]).split('/')[6]
        counter = line.split(':')[1]
        url_ocurrences[url] = counter
        fo.write("%s,%s" % (url,counter))
    fo.close()
    f.close()

    total_urls = len(url_ocurrences)
    for key, value in url_ocurrences.items():
        total_ocurrences += int(value)        

    return (total_urls, total_ocurrences)

def main():
    if (len(sys.argv)) < 3:
        return
    else:
        filename_pdf = os.getcwd() + '/' + sys.argv[1]
        filename_responses = os.getcwd() + '/' + sys.argv[2]
        filename_docx = os.getcwd() + '/' + sys.argv[3]
        print ("Extracting total pdfs from: " + filename_pdf)
        print ("Extracting total responses from: " + filename_responses)
        print ("Extracting total docx from: " + filename_docx)

        (total_urls, total_responses) = count_ocurrences(filename_responses)
        print ("For: " + str(total_urls) + " urls, there are: " + str(total_responses) + " responses")
        
        (total_urls, total_pdfs) = count_ocurrences(filename_pdf)
        print ("For: " + str(total_urls) + " urls, there are: " + str(total_pdfs) + " pdfs")
        print("That represents a " + str((total_pdfs/total_responses)*100) + "% of the links")
        
        (total_urls, total_docx) = count_ocurrences(filename_docx)
        print ("For: " + str(total_urls) + " urls, there are: " + str(total_docx) + " docx")
        print("That represents a " + str((total_docx/total_responses)*100) + "% of the links")

if __name__=="__main__":
    main()
