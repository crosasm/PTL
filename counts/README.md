The list of data has been generated with the following commands:

- List of pdfs per URL:

```
zgrep -c "\%PDF" /var/lib/mongo/downloads/20190522093017/*.warc.gz > pdfs_in_warcs.txt
```
- List of docsx per URL:
```
zgrep -c "\.docx" /var/lib/mongo/downloads/20190522093017/*.warc.gz > docx_in_warcs.txt
```
- List of total responses per URL:
```
zgrep -c "WARC\-Type\:\ response" /var/lib/mongo/downloads/20190522093017/*.warc.gz > responses_in_warcs.txt
```
### The script to count the appearances of each type of document can be executed as follows:
```
python3 ./extract_total_pdfs.py pdfs_in_warcs.txt responses_in_warcs.txt docx_in_warcs.txt
```
The output would look like follows:
```
$ python3 ./extract_total_pdfs.py pdfs_in_warcs.txt responses_in_warcs.txt docxs_in_warcs.txt

Extracting total pdfs from: ./pdfs_in_warcs.txt
Extracting total responses from: ./responses_in_warcs.txt
Extracting total docx from: ./docxs_in_warcs.txt
For: 2335 urls, there are: 18361337 responses
For: 2335 urls, there are: 18294 pdfs
That represents a 0.09963326744670065% of the links
For: 2335 urls, there are: 30177 docx
That represents a 0.16435077685246993% of the links
```
