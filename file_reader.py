import configparser

def read_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content

def read_config(config_file_path):
    config = configparser.ConfigParser()
    config.read(config_file_path)
    source_file = config['FILES']['source']
    destination_file = config['FILES']['destination']
    return source_file, destination_file