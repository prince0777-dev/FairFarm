# app/routes/product_routes.py (updated)

from app.ml_model.price_prediction import predict_price

@router.post("/products")
def create_product(product: Product, db: Session = Depends(get_db)):
    # Price prediction logic
    predicted_price = predict_price([product.quantity, product.category])
    product.price = predicted_price  # Use predicted price for product listing
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
