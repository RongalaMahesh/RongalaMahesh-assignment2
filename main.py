from file_reader import read_file, read_config

config_file_path = 'config.ini'
source_file_path, destination_file_path = read_config(config_file_path)

source_content = read_file(source_file_path)

lines = source_content.strip().split('\n')
keys = [line.split(',')[0] for line in lines]
values = [line.split(',')[1] for line in lines]
data_dict = dict(zip(keys, values))

with open(destination_file_path, 'w') as f:
    f.write(','.join(data_dict.keys()) + '\n')
    f.write(','.join(data_dict.values()))