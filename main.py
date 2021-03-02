import smtplib
from email.message import EmailMessage
import datetime as dt
import pandas
import random


class BirthdayWisher:
    def __init__(self):
        self.today = (dt.datetime.now().month, dt.datetime.now().day)
        self.smtp_server = "smtp.email.com"
        self.from_email = "no_reply@email.com"
        self.password = "D1q8!7LijD$C"
        self.msg = EmailMessage()
        data = pandas.read_csv("birthdays.csv")
        self.birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

    def app(self):
        if self.today in self.birthdays_dict:
            file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
            self.send(file_path)
        else:
            print("No birthday today")

    def send(self, file_path):
        with open(file_path) as letter_file:
            content = letter_file.read()
            content = content.replace("[NAME]", self.birthdays_dict[self.today]["name"])
        self.msg.set_content(content)
        self.msg['Subject'] = "Happy Birthday"
        self.msg['From'] = self.from_email
        self.msg['To'] = self.birthdays_dict[self.today]["email"]
        with smtplib.SMTP(self.smtp_server) as connection:
            connection.starttls()
            connection.login(user=self.from_email, password=self.password)
            connection.send_message(self.msg)
        print(f"Email sent to {self.birthdays_dict[self.today]['name']}")


if __name__ == '__main__':
    birthday_wisher = BirthdayWisher()
    birthday_wisher.app()
