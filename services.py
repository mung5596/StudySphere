from django.core.mail import EmailMessage
from django.conf import settings
import threading
import logging
logger = logging.getLogger('django')


def send_email(subject, body, recipient_list, from_email=None):
    """
    Utility function that sends email in an asynchronous way
    """
    if not from_email:
        from_email = settings.DEFAULT_FROM_EMAIL  # sets the default email address

    # Inner function that sends the email using SMTP
    def async_send():
        try:
            # create email message
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=from_email,
                to=recipient_list,
            )

            # send email
            email.send(fail_silently=False)
        except Exception as e:
            logger.info(f"Error occurred: {e}")

    # asynchronous operation using threads
    email_thread = threading.Thread(target=async_send)
    email_thread.start()
