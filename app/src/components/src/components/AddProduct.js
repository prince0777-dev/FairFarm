// src/components/AddProduct.js

import React, { useState } from 'react';
import { createProduct } from '../services/api';

const AddProduct = () => {
    const [product, setProduct] = useState({
        name: '',
        category: '',
        quantity: 0,
    });

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newProduct = await createProduct(product);
        console.log('Product created:', newProduct);
    };

    return (
        <div>
            <h1>Add Product</h1>
            <form onSubmit={handleSubmit}>
                <input 
                    type="text" 
                    placeholder="Product Name" 
                    value={product.name} 
                    onChange={(e) => setProduct({ ...product, name: e.target.value })} 
                />
                <input 
                    type="text" 
                    placeholder="Category" 
                    value={product.category} 
                    onChange={(e) => setProduct({ ...product, category: e.target.value })} 
                />
                <input 
                    type="number" 
                    placeholder="Quantity" 
                    value={product.quantity} 
                    onChange={(e) => setProduct({ ...product, quantity: e.target.value })} 
                />
                <button type="submit">Add Product</button>
            </form>
        </div>
    );
};

export default AddProduct;
