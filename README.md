
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
The evaluation queries have already been stored in [raw_query](raw_query/): 
```
APL/10-K/20201030_10-K_320193.jsonl
AAPL/10-K/20221028_10-K_320193.jsonl
HLT/10-K/20200211_10-K_1585689.jsonl
HLT/10-K/20220216_10-K_1585689.jsonl
JNJ/10-K/20200218_10-K_200406.jsonl
JNJ/10-K/20220217_10-K_200406.jsonl
NVDA/10-K/20200220_10-K_1045810.jsonl
NVDA/10-K/20220318_10-K_1045810.jsonl
UPS/10-K/20200220_10-K_1090727.jsonl
UPS/10-K/20220222_10-K_1090727.jsonl
```
All the queries are from MD&A paragraphs. 
Please download [here](#) or cfda server: ``/home/ythsiao/mda``.

4. Start server
```
python manage.py runserver
```

5. Upload queries and results and Start server
See the example query and qresults in this repo: 
[query.jsonl](example/query.jsonl) and [qresult.txt](testing/qresult.txt).

You are good to go now. Once the judgements are done, you can download the judged queries and judged reference-to-target relevance.

