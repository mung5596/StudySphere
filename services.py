from django.core.mail import EmailMessage
from django.conf import settings
import threading


def send_email(subject, body, recipient_list, from_email=None):
    """
    Utility function that sends email in an asynchronous way
    """
    if not from_email:
        from_email = settings.DEFAULT_FROM_EMAIL  # sets the default email address

    # Inner function that sends the email using SMTP
    def send():
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
            print("이메일이 성공적으로 전송되었습니다!")
        except Exception as e:
            print(f"이메일 전송 중 오류 발생: {e}")

    # asynchronous operation using threads
    email_thread = threading.Thread(target=send)
    email_thread.start()
