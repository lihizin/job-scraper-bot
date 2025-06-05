import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

def test_email():
    # Load environment variables
    load_dotenv()
    
    # Get email configuration
    sender_email = os.getenv('EMAIL_ADDRESS')
    password = os.getenv('EMAIL_PASSWORD')
    recipient_emails = os.getenv('TO_EMAILS').split(',')
      # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ", ".join(recipient_emails)  # Send to all recipients
    message["Subject"] = "Test Email - Job Scraper"
    
    body = "This is a test email to verify email configuration is working correctly."
    message.attach(MIMEText(body, "plain"))
    
    try:
        # Create SMTP session
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            # Login to the server
            server.login(sender_email, password)
              # Send email
            text = message.as_string()
            server.sendmail(sender_email, recipient_emails, text)
            print(f"✅ Test email sent successfully to {', '.join(recipient_emails)}!")
            return True
            
    except Exception as e:
        print(f"❌ Failed to send test email: {str(e)}")
        return False

if __name__ == "__main__":
    test_email()
