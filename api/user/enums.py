from enum import Enum


class UserRole(Enum):
    shop = 'shop'
    admin = 'admin'

    @classmethod
    def choices(cls):
        return [
            (key.value, key.name) 
            for key in cls
        ]

