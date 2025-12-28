import enum

class Languages(enum.Enum):
    EN = "en"
    DE = "de"
    ES = "es"

class InvoicesStatus(enum.Enum):
    PENDING = "pending"
    PAID = "paid"
    CANCELED = "canceled"