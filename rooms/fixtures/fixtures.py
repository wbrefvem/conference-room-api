import json
import inflection

f = open('fixtures.json', 'r')

fixtures = json.load(f)

f.close()

for fixture in fixtures:

    model_f = open('%s.json' % fixture['model'], 'w+')
    new_fixtures = []

    for item in fixture['items']:
        new_items = {}
        for key, value in item.items():
            new_items.update({inflection.underscore(key): value})

        model = 'rooms.%s' % fixture['model']
        pk = new_items['id']
        del new_items['id']
        fields = new_items

        new_fixtures.append({'model': model, 'pk': pk, 'fields': fields})

    json.dump(new_fixtures, model_f)

    model_f.close()
