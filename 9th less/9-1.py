import json

with open('tester.json', 'r', encoding='utf8') as file:
    data = json.load(file)



with open('tester.json', 'w', encoding='utf8') as wfile:
    json.dump(data, wfile, indent=2)


# json_string = '''
# {
#   "people": [
#     {
#       "name": "Jack Sumers",
#       "phone": "555-555-555",
#       "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
#       "has_licence": false
#     },
#     {
#       "name": "Mary Smith",
#       "phone": "777-777-777",
#       "emails": null,
#       "has_licence": true
#     }
#   ]
# }'''
#
# data = json.loads(json_string)
# for person in data['people']:
#     del person['phone']
# print(data)
#
# new_json_sting = json.dumps(data, indent=2)
# print(new_json_sting)
