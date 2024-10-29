import re

def filter_valid_emails(emails_string):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$"

    try:
        emails = emails_string.split()
        valid_emails = [email for email in emails if re.fullmatch(email_pattern, email)]
        return valid_emails
    except Exception as e:
        print(f"Ошибка обработки email-адресов: {e}")
        return []

emails_input = "@test@example.com wrong_email.com another.correct@domain.com"
print(filter_valid_emails(emails_input))
