mkdir -p documents/

for file in raw_data/*/10-K/*jsonl;do
    python3 preprocess/split_corpus.py \
        --input_jsonl $file \
        --output_dir documents/
done
