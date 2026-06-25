import datetime

class Email:
    def __init__(self, sender, receiver, subject, body):
        # Initialize email attributes
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now() # Store current date and time
        self.read = False # New emails are unread by default

    def mark_as_read(self):
        # Change email status to read
        self.read = True

    def display_full_email(self):
        # Mark email as read and display its complete details
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self):
        # Return a formatted summary of the email for listing
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

class Inbox:
    def __init__(self):
        # Initialize an empty list to store emails
        self.emails = []

    def receive_email(self, email):
        # Append a newly received email to the list
        self.emails.append(email)

    def list_emails(self):
        # Display all emails in the inbox with their index number
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    def read_email(self, index):
        # Fetch and read a specific email using its 1-based index
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()

    def delete_email(self, index):
        # Remove a specific email from the inbox using its 1-based index
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')

class User:
    def __init__(self, name):
        # Initialize user details and create a dedicated inbox object
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        # Create an email and send it to the receiver's inbox
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f"Email sent from {self.name} to {receiver.name}!\n")

    def check_inbox(self):
        # Print user's inbox header and list all their emails
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        # Call inbox method to read an email
        self.inbox.read_email(index)

    def delete_email(self, index):
        # Call inbox method to delete an email
        self.inbox.delete_email(index)

def main():
    # Create two user objects: Tory and Ramy
    tory = User("Tory")
    ramy = User("Ramy")

    # 1. Tory sends an email to Ramy
    tory.send_email(ramy, "Hello", "Hi Ramy, just saying hello!")

    # 2. Ramy sends an email to Tory
    ramy.send_email(tory, "Re: Hello", "Hi Tory, hope you are fine.")

    # 3. Ramy checks his inbox for new messages
    ramy.check_inbox()

    # 4. Ramy reads the first email in his inbox
    ramy.read_email(1)

    # 5. Ramy deletes the first email
    ramy.delete_email(1)

    # 6. Ramy checks his inbox again to verify the changes
    ramy.check_inbox()

if __name__ == "__main__":
    # Execute the main simulation
    main()
