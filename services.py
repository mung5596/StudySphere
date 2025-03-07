from django.core.mail import EmailMessage
from django.conf import settings
import threading


def send_email(subject, body, recipient_list, from_email=None):
    """
    이메일을 비동기로 전송하는 유틸리티 함수
    """
    if not from_email:
        from_email = settings.DEFAULT_FROM_EMAIL  # 기본 발신 이메일 설정

    # 이메일 전송 작업을 실행하는 내부 함수
    def send():
        try:
            # 이메일 메시지 생성
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=from_email,
                to=recipient_list,
            )

            # 이메일 전송
            email.send(fail_silently=False)
            print("이메일이 성공적으로 전송되었습니다!")
        except Exception as e:
            print(f"이메일 전송 중 오류 발생: {e}")

    # threading을 사용해 비동기로 이메일 전송
    email_thread = threading.Thread(target=send)
    email_thread.start()
