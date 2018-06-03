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
    intervenants.append(str(ligne[0]))
    projet.append(ligne[1])
    description.append(ligne[2])
    date.append(ligne[3])

print date
#!/usr/bin/python
 
import time
## dd/mm/yyyy format
listeMois = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]
currDate = time.strftime("%d/%m/%Y")
print currDate
mois = currDate[3] + currDate[4]
jourTmp = currDate[0] + currDate[1]
jour = jourTmp.lstrip("0")
newDate = jour + " " + listeMois[int(mois) - 1] + " " + currDate[6] + currDate[7] + currDate[8] + currDate[9]

for aDate in date:
    if aDate == newDate:
        print "equals ! " + newDate



from datetime import datetime
date = datetime.now()
print date