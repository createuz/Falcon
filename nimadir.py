import json
import csv

# with open('regions.csv', encoding='utf-8-sig') as f:
#     regions = csv.DictReader(f)
#     result = []
#     for region in regions:
#         result.append({
#             'model': 'apps.region',
#             'pk': region['id'],
#             'fields': {
#                 'name': region['name'],
#             }
#         })
#     with open('apps/fixtures/region.json', 'w') as f:
#         json.dump(result, f, indent=2)

with open('districts.csv', encoding='utf-8-sig') as f:
    districts = csv.DictReader(f)
    result = []
    for district in districts:
        result.append({
            'model': 'apps.district',
            'pk': district['id'],
            'fields': {
                'name': district['name'],
                'region': district['region']
            }
        })
    with open('apps/fixtures/district.json', 'w') as f:
        json.dump(result, f, indent=2)
