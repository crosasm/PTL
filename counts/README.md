The list of data has been generated with the following commands:

- List of pdfs per URL:

zgrep -c "\%PDF" /var/lib/mongo/downloads/20190522093017/*.warc.gz > pdfs_in_warcs.txt

- List of docsx per URL:

zgrep -c "\.docx" /var/lib/mongo/downloads/20190522093017/*.warc.gz > docx_in_warcs.txt

- List of total responses per URL:

zgrep -c "WARC\-Type\:\ response" /var/lib/mongo/downloads/20190522093017/*.warc.gz > responses_in_warcs.txt

### The script to count the appearances of each type of document can be executed as follows:

python3 ./extract_total_pdfs.py pdfs_in_warcs.txt responses_in_warcs.txt docx_in_warcs.txt

The output would look like:

Extracting total pdfs from: /home/crosas/tmp/NLP/encomienda/counts/pdfs_in_warcs.txt
Extracting total responses from: /home/crosas/tmp/NLP/encomienda/counts/responses_in_warcs.txt
Extracting total docx from: /home/crosas/tmp/NLP/encomienda/counts/docxs_in_warcs.txt
For: 818 urls, there are: 3120624 responses
For: 818 urls, there are: 7069 pdfs
That represents a 0.22652520777895702% of the links
For: 818 urls, there are: 8667 docx
That represents a 0.2777329149554704% of the links
