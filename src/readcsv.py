def read_csv(csv_file):
    data = []
    with open(csv_file, 'r') as f:

        # create a list of rows in the CSV file
        rows = f.readlines()

        # strip white-space and newlines
        rows = list(map(lambda x:x.strip(), rows))

        for row in rows:

            # further split each row into columns assuming delimiter is comma 
            row = row.split(',')

            # append to data-frame our new row-object with columns
            data.append(row)

    return data

csvFile = '../resources/evenements.csv'

# invoke our function 
data = read_csv(csvFile)
entete = data[0][0].split(';')
intervenants = []
projet = []
description = []
date = []
for row in data[1:]:
    ligne = row[0].split(';')
    intervenants.append(ligne[0])
    projet.append(ligne[1])
    description.append(ligne[2])
    date.append(ligne[3])

print intervenants
print projet
print description
print date