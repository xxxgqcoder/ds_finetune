import json

# parse data into question and anwser pair


def parse_92k_data(data_path):
    with open(data_path) as f:
        data = json.load(f)

    parsed_data = []
    for d in data:
        ret = {
            'question': d['question'],
            'anwser': d['answer'],
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
            'anwser': d['output'],
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
            'anwser': d['output'],
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
            'anwser': d['response'],
        }
        parsed_data.append(ret)

    return parsed_data


# data path - parser function mapping
# # train
# parser_config = {
#     '/Users/xcoder/aDrive/dataset/law_finetune/CrimeKgAssitant_after_clean_52k.json': parse_52k_data,
#     '/Users/xcoder/aDrive/dataset/law_finetune/answer_with_law_92k.json': parse_92k_data,
# }
# processed_data_save_path = '/Users/xcoder/aDrive/dataset/law_finetune/finetune_processed_train.json'

# eval
parser_config = {
    '/Users/xcoder/aDrive/dataset/law_finetune/fakao_gpt4.json':
    parse_fakao_data,
    '/Users/xcoder/aDrive/dataset/law_finetune/zixun_gpt4.json':
    parse_zixun_data,
}
processed_data_save_path = '/Users/xcoder/aDrive/dataset/law_finetune/finetune_processed_eval.json'

processed_data = []
for data_path, func in parser_config.items():
    print(f'processing data from {data_path}')
    parsed_data = func(data_path)
    print(f'get {len(parsed_data)} records')

    processed_data.extend(parsed_data)

print(f'total {len(processed_data)} processed records')
with open(processed_data_save_path, 'w', encoding='utf8') as f:
    json.dump(processed_data, f, ensure_ascii=False, indent=4)
    print(f'processed data saved to {processed_data_save_path}')
