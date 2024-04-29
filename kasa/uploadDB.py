import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import datetime
import os
import shutil

def send_email(subject, message, to_email, attachment_path):
    from_email = "accessoriesserenata@gmail.com"
    password = "fkcd fzbe ixtd epog"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))


    filename = r"C:\Users\User\store_manager\d1.sqlite3"

    attachment_path_with_new_name = os.path.join(os.path.dirname(attachment_path), filename)
    shutil.copy(attachment_path, attachment_path_with_new_name)

    # Attach the copied file with the new filename
    attachment = open(attachment_path_with_new_name, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")
    msg.attach(part)

    # Connect to SMTP server and send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

def main():
    to_email = "accessoriesserenata@gmail.com"
    attachment_path = r"C:\Users\User\store_manager\db.sqlite3"
    message = "Please find the attached file."

    # Set the initial upload time to 7:55 AM
    upload_time = datetime.datetime.now().replace(hour=7, minute=55, second=0, microsecond=0)

    while True:
        # Get the current time
        current_time = datetime.datetime.now()

        # If the current time is past the upload time, send the email
        if current_time >= upload_time:
            # Generate the subject with timestamp
            subject = current_time.strftime("%d-%m-%H-%M")  # Format: day-month-hour-minute
            send_email(subject, message, to_email, attachment_path)
            print("Email sent successfully with subject:", subject)

            # Increment the upload time by 30 minutes
            upload_time += datetime.timedelta(minutes=30)

        # Sleep for 1 minute before checking the time again
        time.sleep(60)

if __name__ == "__main__":
    main()
