
1. Rebuild the schema and database
```
rm db/relevation.db
python manage.py migrate --run-syncdb
```
2. Prepare collections (for retrieved documents)
For efficiency, this system would read the file once a time.
Thus, only one line of document should be stored in a file; 
the filename refers to document identified.

You can use `split_corpus.py` to pool your docs.
```
python split_corpus.py \
  --input_jsonl corpus.jsonl \ # the jsonl with entire document.
  --output_dir ../documents/   # all documents would output here.
```

3. Start server
```
python manage.py runserver
```

4. Setup and upload queries and retreived results

