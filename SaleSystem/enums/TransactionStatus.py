from enum import Enum



class TransactionStatus(Enum):
    REQUESTED               =   "Requested"
    WAITING_FOR_PAYMENT     =   "Waiting for payment"
    CANCELED                =   "Canceled"
    PAID                    =   "Paid"
    FINALIZED               =   "Finalized"


