import json

import numpy as np
from farmhash import FarmHash64

# parse data into question and anwser pair


def parse_92k_data(data_path):
    with open(data_path) as f:
        data = json.load(f)

    parsed_data = []
    for d in data:
        ret = {
            'question': d['question'],
            'answer': d['answer'],
            'uuid': FarmHash64(d['question']),
        }
        parsed_data.append(ret)

    return parsed_data


def parse_52k_data(data_path):
    with open(data_path) as f:
        data = json.load(f)

    parsed_data = []
    for d in data:
        ret = {
            'question': d['input'],
            'answer': d['output'],
            'uuid': FarmHash64(d['input']),
        }
        parsed_data.append(ret)

    return parsed_data


def parse_fakao_data(data_path):
    with open(data_path) as f:
        data = json.load(f)

    parsed_data = []
    for d in data:
        ret = {
            'question': d['input'].strip('Question:'),
            'answer': d['output'],
            'uuid': FarmHash64(d['input'].strip('Question:')),
        }
        parsed_data.append(ret)

    return parsed_data


def parse_zixun_data(data_path):
    with open(data_path) as f:
        data = json.load(f)

    parsed_data = []
    for d in data:
        ret = {
            'question': d['query'],
            'answer': d['response'],
            'uuid': FarmHash64(d['query']),
        }
        parsed_data.append(ret)

    return parsed_data


parser_config = {
    '/Users/xcoder/aDrive/dataset/law_finetune/answer_with_law_92k.json':
    parse_92k_data,
    '/Users/xcoder/aDrive/dataset/law_finetune/CrimeKgAssitant_after_clean_52k.json':
    parse_52k_data,
    '/Users/xcoder/aDrive/dataset/law_finetune/fakao_gpt4.json':
    parse_fakao_data,
    '/Users/xcoder/aDrive/dataset/law_finetune/zixun_gpt4.json':
    parse_zixun_data,
}

processed_train_data_save_path = '/Users/xcoder/aDrive/dataset/law_finetune/finetune_processed_train.json'
processed_eval_data_save_path = '/Users/xcoder/aDrive/dataset/law_finetune/finetune_processed_eval.json'
eval_num = 1000

processed_data = []
for data_path, func in parser_config.items():
    print(f'processing data from {data_path}')
    parsed_data = func(data_path)
    print(f'get {len(parsed_data)} records')

    processed_data.extend(parsed_data)

print(f'total {len(processed_data)} processed records')
np.random.shuffle(processed_data)

train_data = processed_data[eval_num:]
eval_data = processed_data[:eval_num]

with open(processed_train_data_save_path, 'w', encoding='utf8') as f:
    json.dump(train_data, f, ensure_ascii=False, indent=4)
    print(
        f'processed data saved to {processed_train_data_save_path}, total {len(train_data)}'
    )

with open(processed_eval_data_save_path, 'w', encoding='utf8') as f:
    json.dump(eval_data, f, ensure_ascii=False, indent=4)
    print(
        f'processed data saved to {processed_eval_data_save_path}, total {len(eval_data)}'
    )
