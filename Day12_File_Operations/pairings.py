from pathlib import Path
import random

with open("courseid_4_participants.csv", encoding="utf-8") as f:
    participants = f.readlines()

emails = [p.strip().split(",")[2] for p in participants]

print(*emails, sep="\n")

paired_emails = ["address", "jekabsons","Iljasenko",
                 "lolita", "edite", "broks",
                 "regina", "julij", "mackus", "morozs",
                 "everts", "salun", "example", "aleksandra"]
unpaired_emails = [email for email in emails if not any(p.lower() in email.lower() for p in paired_emails)]
print(len(unpaired_emails))
print(*unpaired_emails, sep=    "\n")
random.seed(42)
random.shuffle(unpaired_emails)
print("Final pairing:")
print(unpaired_emails[:2], unpaired_emails[2:4], unpaired_emails[4:], sep="\n")

