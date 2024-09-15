import re

async def has_phone_number(text):
    # Telefon raqami uchun regex
    phone_regex = r'(\+998|998)?\d{9}'
    
    # Matn ichida regexga mos raqam bor yoki yo'qligini tekshiradi
    if re.search(phone_regex, text):
        return True
    return False
