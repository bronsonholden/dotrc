from os.path import expanduser
import yaml
import simplejson as json

def load_yaml(path):
    try:
        return yaml.load(file(path, 'r'))
    except:
        return None

def load_json(path):
    try:
        return json.load(file(path, 'r'))
    except:
        return None

def load(app):
    # Result
    config = {}
    # Get user dir path
    home = expanduser('~')

    # Generate a list of files to check
    locations = [
        home + '/.config/' + app,
        '.' + app + 'rc'
    ]

    # Try to parse file contents as YAML
    for loc in locations:
        cfg = load_yaml(loc) or load_json(loc)
        config.update(cfg)

    return config
