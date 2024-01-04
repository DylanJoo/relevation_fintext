import os
import argparse
import json
from tqdm import tqdm

def save_document(dir, docid, contents, metadata=None):
    path = os.path.join(dir, docid)
    with open(path, 'w') as f:
        outputs = {'contents': contents}
        if metadata:
            outputs.update({'metadata': metadata})
        f.write(json.dumps(outputs)+'\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_jsonl", type=str, default=None)
    parser.add_argument("--output_dir", default='../documents/', type=str)
    args = parser.parse_args()

    with open(args.input_jsonl, 'r') as f:
        for line in tqdm(f):
            data = json.loads(line.strip())
            docid = data['id']
            contents = data['contents']
            metadata = "{} {} {}-{}".format(
                    data['name'], data['form'],
                    data['filing_year'], data['filing_month']
            )

            # save
            save_document(args.output_dir, docid, contents, metadata)

