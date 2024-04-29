import imaplib
import email
import os
import datetime
import time

def download_attachments(username, password, save_dir):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")

    # Get the current time
    current_time = datetime.datetime.now()

    # Construct the expected subject format based on the current time
    expected_subject = current_time.strftime("%d-%m-%H-%M")  # Format: day-month-hour-minute

    # Search for emails with subjects matching the expected format
    result, data = mail.search(None, f'(SUBJECT "{expected_subject}")')
    ids = data[0]
    id_list = ids.split()

    print("Found emails:", id_list)  # Debugging output to verify the list of found emails

    for num in id_list:
        result, data = mail.fetch(num, "(RFC822)")
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        subject = msg['subject']
        print("Subject:", subject)  # Print the subject of the email

        for part in msg.walk():
            if part.get_content_maintype() == "multipart":
                continue
            if part.get("Content-Disposition") is None:
                continue

            filename = part.get_filename()
            if filename:
                filepath = os.path.join(save_dir, filename)
                if os.path.isfile(filepath):
                    os.remove(filepath)  # Remove the existing file before downloading the new one
                with open(filepath, "wb") as fp:
                    fp.write(part.get_payload(decode=True))
                print("Attachment downloaded:", filename)
                print("Saved to:", filepath)  # Debugging output to verify filepath


    mail.close()
    mail.logout()

def main():
    username = "accessoriesserenata@gmail.com"
    password = "fkcd fzbe ixtd epog"
    save_dir = r"C:\Users\User\store_manager\downloads\\"

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Set the download time to 8:00 AM

    while True:
        # Get the current time
        current_time = datetime.datetime.now()

        # If the current time matches the download time, download the attachments
        download_attachments(username, password, save_dir)
        print("Attachments downloaded successfully at:", current_time)


        # Sleep for 1 minute before checking the time again
        time.sleep(60)

if __name__ == "__main__":
    main()
