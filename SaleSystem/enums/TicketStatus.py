from enum import Enum

class TicketStatus(Enum):
    NEW                     =   "New"
    PAID                    =   "Pending"
    ACCEPTED                =   "Accepted"
    ACTIVE                  =   "Active"
    OUTDATED                =   "Outdated"
