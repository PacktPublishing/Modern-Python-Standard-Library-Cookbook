import csv

with open('/tmp/table.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(("ID","Name","Surname","Language"))
    writer.writerow((1,"Alessandro","Molina","Italian"))
    writer.writerow((2,"Mika","Häkkinen","Suomi"))
    writer.writerow((3,"Sebastian","Vettel","Deutsch"))

with open('/tmp/table.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
