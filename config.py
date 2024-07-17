import os
from typing import Final

from dotenv import load_dotenv

load_dotenv()

TOKEN_UKR_NET: Final = os.getenv('TOKEN_UKR_NET')
MAIL_USER: Final = os.getenv('MAIL_USER')
SMTP_SERVER: Final = os.getenv('SMTP_SERVER')
