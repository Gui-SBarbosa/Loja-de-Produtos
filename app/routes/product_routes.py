from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils.auth import role_required
from app.services.product_service import (
    create_product_service,
    list_all_product,
    list_seller_product_by_id,
    update_product_service,
    delete_product_service,
    get_product_by_id
)
from app.schemas.product_schema import (
    ProductCreateSchema,
    ProductCreateResponse,
    ProductUpdateSchema,
    ProductUpdateResponse,
    ProductDetailSchema
)

product_bp = Blueprint('products', __name__)

# Rotas para gerenciamento de produtos criados por 'SELLER'

#Create
@product_bp.route('/create', methods=['POST'])
@jwt_required()
@role_required('SELLER')
def create_product():
    data = request.get_json()
    errors = ProductCreateSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    seller_id = get_jwt_identity()
    success, result, status = create_product_service(data, seller_id)
    if not success:
        return jsonify(result), status

    return jsonify({
        "success": True,
        "message": "Produto criado com sucesso",
        "product": ProductCreateResponse().dump(result)
    }), status

# Listar produtos
@product_bp.route('/my',methods=['GET'])
@jwt_required()
@role_required('SELLER')
def list_my_products():
    seller_id = get_jwt_identity()
    success, result, status = list_seller_product_by_id(seller_id)

    if not success:
        return jsonify(result), status

    if isinstance(result, list):
        return jsonify(ProductCreateResponse(many=True).dump(result)), status

    return jsonify(result), status

# Update
@product_bp.route('/<int:product_id>', methods=['PUT'])
@jwt_required()
@role_required('SELLER')
def update_product(product_id):
    data = request.get_json()
    errors = ProductUpdateSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    seller_id = get_jwt_identity()
    product = get_product_by_id(product_id)

    if not product or product.id_seller != int(seller_id):
        return jsonify({'error': 'Produto não encontrado ou sem permissão'}), 404

    success, result, status = update_product_service(product, data)
    if not success:
        return jsonify(result), status

    return jsonify({
        "success": True,
        "message": "Produto atualizado com sucesso",
        "product": ProductUpdateResponse().dump(result)
    }), status


# Delete
@product_bp.route('/<int:product_id>', methods=['DELETE'])
@jwt_required()
@role_required('SELLER')
def delete_product(product_id):
    seller_id = get_jwt_identity()
    success, result, status = delete_product_service(product_id, int(seller_id))
    return jsonify(result), status


# Rota ABERTA para listagem de produtos

@product_bp.route('/all', methods=['GET'])
def list_products():
    products = list_all_product()
    return jsonify(ProductDetailSchema(many=True).dump(products)), 200


@product_bp.route('/details/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = get_product_by_id(product_id)

    if not product:
        print("Produto não encontrado")
        return jsonify({'error': 'Produto não encontrado'}), 404

    return jsonify(ProductDetailSchema().dump(product)), 200