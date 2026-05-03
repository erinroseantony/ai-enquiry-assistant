import csv

def save_lead(message):
    with open("leads.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([message])