import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from getpass import getpass
from email.mime.base import MIMEBase
from email import encoders

class GmailSMTP:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587  # TLS port
        self.smtp_username = None
        self.smtp_password = None

    def setup(self):
        """Setup SMTP credentials"""
        print("Gmail SMTP Setup")
        print("-" * 50)
        self.smtp_username = os.getenv("SMTP_USERNAME", "gshahrouzi@gmail.com")
        self.smtp_password = os.getenv("SMTP_PASSWORD")
        print(f"SMTP Username: {self.smtp_username}")
        
    def test_connection(self):
        """Test SMTP connection"""
        try:
            # Create SMTP connection
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Enable TLS
            
            # Login
            server.login(self.smtp_username, self.smtp_password)
            print("\n✅ SMTP Connection successful!")
            
            # Send test email
            # if input("\nWould you like to send a test email? (y/n): ").lower() == 'y':
            #     self.send_test_email(server)
            
            # Ask to send linux kernel patch
            if input("\nWould you like to send your linux kernel patch? (y/n): ").lower() == 'y':
                self.send_patch_email(server)
            
            server.quit()
            
        except Exception as e:
            print(f"\n❌ Connection failed: {str(e)}")
            print("\nCommon issues:")
            print("1. Make sure you're using an App Password if 2FA is enabled")
            print("2. Check if 'Less secure app access' is enabled (if not using App Password)")
            print("3. Verify your credentials are correct")

    def send_test_email(self, server):
        """Send a test email"""
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.smtp_username
            msg['To'] = self.smtp_username  # Sending to self for testing
            msg['Subject'] = "Gmail SMTP Test"
            
            body = "This is a test email sent using Python SMTP client."
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email
            server.send_message(msg)
            print("\n✅ Test email sent successfully!")
            
        except Exception as e:
            print(f"\n❌ Failed to send test email: {str(e)}")

    def send_patch_email(self, server):
        """Send linux kernel patch email with patch content in the email body unchanged"""
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.smtp_username
            to = "skhan@linuxfoundation.org"
            print("Is this the person to send it to?: " + to)
            check = input("Enter y/n: ")
            if check == 'n':
                to = input("Enter the email address of the recipient: ")
            msg['To'] = to

            # New: Prompt for CC recipients (comma separated)
            cc_input = input("Enter CC email addresses (comma separated) or leave blank: ")
            if cc_input.strip():
                msg['Cc'] = cc_input.strip()
            
            subject = input("Enter the subject for the patch email: ")
            msg['Subject'] = subject

            # Read the patch file content without modifying tabs/spaces
            patch_file = input("Enter the path to the patch file: ")
            with open(patch_file, "rb") as f:
                patch_bytes = f.read()
            patch_content = patch_bytes.decode("utf-8", errors="strict")
            
            msg.attach(MIMEText(patch_content, 'plain'))
            
            # New: Sanity check - print the complete email content
            print("\nSanity Check: Email Content:")
            print(msg.as_string())
            
            # New: Confirm if user wants to send the email
            send_confirm = input("\nDo you want to send the email? (y/n): ")
            if send_confirm.lower() != 'y':
                print("Email sending cancelled by user.")
                return
            
            # Send email
            server.send_message(msg)
            print("\n✅ Linux kernel patch email sent successfully!")
            
        except Exception as e:
            print(f"\n❌ Failed to send linux kernel patch: {str(e)}")

if __name__ == "__main__":
    gmail = GmailSMTP()
    gmail.setup()
    gmail.test_connection()
