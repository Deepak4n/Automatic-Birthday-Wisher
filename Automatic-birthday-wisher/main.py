##################### Extra Hard Starting Project ######################
from datetime import datetime
import pandas
import random
import smtplib
import socket

MY_EMAIL = "sonyadada4@gmail.com"
MY_PASSWORD = "vouq njhd rzhx gmto"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

for today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    print(birthday_person)
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,  to_addrs=birthday_person['email'],
                msg=f"Subject: Happy Morning!\n\n{contents}"
            )
            connection.quit()
    except smtplib.SMTPException: # Didn't make an instance.
        print("Unsuccessful attempt")
    except socket.error:
        print("Socket error found")








