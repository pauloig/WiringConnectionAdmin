# utils/email.py
from django.core.mail import EmailMessage
from django.conf import settings
import os

def send_email_with_attachment(
    subject,
    message,
    recipient_list,
    attachment_paths=None,
    html_message=None,
    from_email=None
):
    """
    Send email with optional attachments
    
    Args:
        subject (str): Email subject
        message (str): Plain text message
        recipient_list (list): List of recipient emails
        attachment_paths (list, optional): List of file paths to attach
        html_message (str, optional): HTML version of the message
        from_email (str, optional): From email address
    
    Returns:
        bool: True if email was sent successfully
    """
    try:
        from_email = from_email or settings.DEFAULT_FROM_EMAIL
        email = EmailMessage(
            subject=subject,
            body=html_message or message,
            from_email=from_email,
            to=recipient_list,
        )
        
        if html_message:
            email.content_subtype = "html"
        
        # Attach files if provided
        if attachment_paths:
            for file_path in attachment_paths:
                if os.path.exists(file_path):
                    with open(file_path, 'rb') as file:
                        file_name = os.path.basename(file_path)
                        email.attach(file_name, file.read(), 'application/octet-stream')
                else:
                    raise FileNotFoundError(f"Attachment not found: {file_path}")
        
        #email.send()
        return False, ""
    except Exception as e:
        # Log the error in production
        if settings.DEBUG:
            print(f"Email sending failed: {str(e)} - from {from_email} to {recipient_list}")
        return True, f"Email sending failed: {str(e)} - from {from_email} to {recipient_list} "