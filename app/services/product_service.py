from flask_jwt_extended import get_jwt_identity

from app.models.product import Product
from app.extension import db


def create_product_service(data, seller_id):
    name = data.get('name_product')
    value = data.get('value')
    description = data.get('description')
    quantity = data.get('quantity')

    if not all ([name, value, description, quantity]):
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
    return True, product, 201


def list_seller_product_by_id(seller_id):
    products = Product.query.filter_by(id_seller=seller_id).all()

    if not products:
        return True, {"message": "Nenhum produto foi criado por essa loja"}, 200

    return True, products, 200


def update_product_service(product, data):
    if not product:
        return False, {'error': 'Produto não encontrado ou sem permissão'}, 404

    product.name_product = data.get('name_product', product.name_product)
    product.value = data.get('value', product.value)
    product.description = data.get('description', product.description)
    product.quantity = data.get('quantity', product.quantity)

    db.session.commit()
    return True, product, 201


def delete_product_service(product_id, seller_id):
    product = Product.query.filter_by(id=product_id, id_seller=seller_id).first()

    if not product:
        return False, {'error': 'Produto não encontrado ou sem permissão'}, 404


    db.session.delete(product)
    db.session.commit()
    return True, {'message': 'Produto deletado com sucesso'}, 200


def list_all_product():
    return Product.query.all()


def get_product_by_id(product_id):
    return Product.query.get(product_id)