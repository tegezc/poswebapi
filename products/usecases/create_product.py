# usecases/create_product.py

from domain.models import Product

class CreateProduct:
    def execute(self, data):
        product = Product(
            name=data.get('name'),
            nip=data.get('nip'),
            stock=data.get('stock')
        )
        product.save()
        return product
