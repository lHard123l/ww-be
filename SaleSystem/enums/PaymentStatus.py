from enum import Enum


class PaymentStatus(Enum):
    NULL                    =   "Null"
    UNREGISTRED             =   "Unregistred"
    REQUESTED               =   "Requested"
    CANCELED                =   "Canceled"
    PENDING                 =   "Pending"
    ACCEPTED                =   "Accepted"
    CONFIRMED               =   "Confirmed"