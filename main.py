import json
with open('clients.json', 'r', encoding='utf-8') as clients:
    data_clients = json.load(clients)
# Dodawanie faktury:
data_invoices = {}
data_invoices['Faktury'] = []
data_invoices['Faktury'].append({
    'id': 1,
    'data': "2020-09-04 14:53:43",
    'name': f"data_clients['Indywidualni'][0]['nazwa']",
    'city': f"data_clients['Indywidualni'][0]['adres']['miasto']",
    'zip': f"data_clients['Indywidualni'][0]['adres']['kod pocztowy']",
    'street': f"data_clients['Indywidualni'][0]['adres']['ulica']",
    'building no': f"data_clients['Indywidualni'][0]['adres']['numer budynku']",
    'e-mail': f"data_clients['Indywidualni'][0]['adres']['e-mail']",
    'NIP': f"data_clients['Indywidualni'][0]['adres']['NIP']",
    'gross': 5000,
    'net': 3622.73
})
# jesli chcesz zapisywac do tego samego pliku, to musisz podmienic nazwe pliku na invoices.json
with open('invoices_new.json', 'w', encoding='utf-8') as f:
    json.dump(data_invoices, f, indent=4)

# usuwanie faktury z pliku
with open('invoices.json', 'r', encoding='utf-8') as invoices:
    data = json.load(invoices)

for element in data['Faktury']:
    if element['id'] == 1:
        del element['id']
        del element['data']
        del element['name']
        del element['city']
        del element['zip']
        del element['street']
        del element['building no']
        del element['e-mail']
        del element['NIP']
        del element['gross']
        del element['net']

with open('invoices.json', 'w', encoding='utf-8') as invoices:
    data = json.dump(data, invoices, indent=4)