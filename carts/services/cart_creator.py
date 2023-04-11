from dataclasses import dataclass
from ..models import Cart

@dataclass
class CartCreator:
    user: any

    def execute(self):
        Cart.objects.get_or_create(user=self.user)