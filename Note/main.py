import json

def create_note(title, content, due_date):
    pass


with open('base.json', 'r', encoding='utf8') as file:
    base = json.load(file)
    if base.get('_id'):
        _id = base.get('_id')
    else:
        _id = 1
