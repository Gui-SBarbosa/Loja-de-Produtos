from app.models.product import Product
from app.extension import db


def create_product_service(data, seller_id):
    name = data.get('name_product')
    value = data.get('value')
    description = data.get('description')
    quantity = data.get('quantity')

    if not all ([name, value, description, quantity]):
        print('Campos obrigatórios ausentes')
        return False, {'error': 'Campos obrigatórios ausentes'}, 400

    product = Product(
        name_product=name,
        value=value,
        description=description,
        quantity=quantity,
        id_seller=seller_id
    )

    db.session.add(product)
    db.session.commit()
    print('Produto cadastrado com sucesso')
    return product


def list_seller_product_by_id(seller_id):
    return Product.query.filter_by(id_seller=seller_id).all()


def update_product_service(product, data):
    product.name_product = data.get('name_product', product.name_product)
    product.value = data.get('value', product.value)
    product.description = data.get('description', product.description)
    product.quantity = data.get('quantity', product.quantity)
    db.session.commit()
    print('Produto atualizado com sucesso')
    return product


def delete_product_service(product):
    db.session.delete(product)
    db.session.commit()


def list_all_product():
    products = Product.query.all()
    return products

def get_product_by_id(product_id):
    return Product.query.get(product_id)