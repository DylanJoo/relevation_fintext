
## 1. Rebuild the schema and database
```
rm db/relevation.db
python manage.py migrate --run-syncdb
```
## 2. Prepare collections (for retrieved documents)
For efficiency, this system would read the file of document once a time.
Thus, each file has only one line (a paragraph) in a file; the filename refers to document identifier (docID).

- The collection (references) we use is from 10K corpus (companies in SP 500 and available in 2018-2023.)  
Please download from [here](#) or cfda server:``/home/ythsiao/output``. 
Then, you can use `split_corpus.py` to pool the corpus, to meet the reference/document format.
- The documents will output in the `documents` folder.
```
mkdir -p documents/
for file in raw_data/*/10-K/*jsonl;do
    python3 preprocess/split_corpus.py \
        --input_jsonl $file \   # the jsonl with entire document.
        --output_dir documents/ # all documents would output here.
done
```

## 3. Prepare queries (for empirical evaluation)
The evaluation queries have already been stored in [raw_query](raw_query/): the 10K of 5 companies in 2020 and 2022.
```
AAPL/10-K/20201030_10-K_320193.jsonl
AAPL/10-K/20221028_10-K_320193.jsonl
HLT/10-K/20200211_10-K_1585689.jsonl
HLT/10-K/20220216_10-K_1585689.jsonl
....
```
All the queries are from MD&A paragraphs, the other MD&A can be downloaded from [here](#) or cfda server: ``/home/ythsiao/mda``.

## 4. Start server
```
python manage.py runserver
```

## 5. Upload queries (for task1) and results (for task2)
See the example query and qresults in this repo: 
[query.jsonl](example/query.jsonl) and [qresult.txt](testing/qresult.txt).


---
## Annotation results

You are good to go now. Once the judgements are done, you can find the download button in the first annotation page (Queries @ the navigation bar).
They include the judged queries and judged reference-to-target relevance.

Example query: 
```json
{
    "id": "20200220_10-K_1090727_part2_item7_para1",
    "text": "Management's discussion and analysis of financial condition and results of operations Overview Highlights of our annual results follow: Yea....",
    "highlight": "",
    "category": {"0": 0, "1": 0, "2": 1, "3": 0, "4": 0},
    "topic": {"1": 1, "2": 0, "3": 0, "4": 1, "5": 0, "6": 0}
}
```
Example reference judgements: 
```
20181105_10-K_320193_part2_item7_para1 Q0 20181105_10-K_320193_part1_item2_para1 1
20181105_10-K_320193_part2_item7_para1 Q0 20181105_10-K_320193_part1_item2_para2 0
20181105_10-K_320193_part2_item7_para1 Q0 20181105_10-K_320193_part1_item2_para3 2
```
