######### Importing libraries #########
import csv
from time import sleep
######### Welcome message #########
print("Welcome.. Hope you are having a good day :)")
sleep(2)
######### Getting names #########
print("Getting names...")
nfile = open('names.txt', 'r')
reader = csv.reader(nfile)
names = [row for row in reader]
nfile.close()
sleep(2)
######### Getting suffixes #########
print("Getting suffixes...")
sfile = open('suffixes.txt', 'r')
reader = csv.reader(sfile)
suffixes = [row for row in reader]
sfile.close()
sleep(2)
######### Getting domain name #########
domain = input("Please enter the domain name")
######### Generating emails #########
print("Generating emails, just relax...")
emails = []
for name in names:
    for suffix in suffixes:
        email = name[0] + suffix[0] + "@" + domain
        emails.append(email)
        email = name[0] + '.' + suffix[0] + "@" + domain
        emails.append(email)
        email = name[0] + '-' + suffix[0] + "@" + domain
        emails.append(email)
        email = name[0] + '_' + suffix[0] + "@" + domain
        emails.append(email)
        email = "its" + name[0]+ suffix[0] + "@" + domain
        emails.append(email)
sleep(2)
######### Saving #########
print("Saving.. Just a moment :)")
save = open('emails.txt' , 'w')
for email in emails:
    save.write(email)
    save.write('\n')
save.close()
sleep(2)
print("Done :)\n See you soon. Take care.")
