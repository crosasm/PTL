The list of data has been generated with the following commands:

- List of pdfs per URL:

zgrep -c "\%PDF" /var/lib/mongo/downloads/20190522093017/*.warc.gz > pdfs_in_warcs.txt

- List of docsx per URL:

zgrep -c "\.docx" /var/lib/mongo/downloads/20190522093017/*.warc.gz > docx_in_warcs.txt

- List of total responses per URL:

zgrep -c "WARC\-Type\:\ response" /var/lib/mongo/downloads/20190522093017/*.warc.gz > responses_in_warcs.txt
