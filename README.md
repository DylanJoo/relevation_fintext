
1. Rebuild the schema and database
```
rm db/relevation.db
python manage.py migrate --run-syncdb
```
2. Prepare collections (for retrieved documents)
For efficiency, this system would read the file once a time.
Thus, only one line of document should be stored in a file; 
the filename refers to document identified.

- Regarding the collection (references), we use parsed 10K corpus. 
Please download [here](#) or cfda server:``/home/ythsiao/output``. 
Then, you can use `split_corpus.py` to pool the corpus, to meet the reference/document format.
- The documents will output in the `documents` folder.
```
for file in raw_data/*/10-K/*jsonl;do
    python3 preprocess/split_data.py \
        --input_jsonl $file \   # the jsonl with entire document.
        --output_dir documents/ # all documents would output here.
done
```

3. Prepare queries (for empirical evaluation)
All the evauation query are from the paragraphs of MD&A section.
Please download [here](#) or cfda server: ``/home/ythsiao/mda``.

4. Start server
```
python manage.py runserver
```

5. Upload queries and results and Start server
See the example query and qresults in this repo: 
[query.jsonl](example/query.jsonl) and [qresult.txt](testing/qresult.txt).

You are good to go now. Once the judgements are done, you can download the judged queries and judged reference-to-target relevance.

