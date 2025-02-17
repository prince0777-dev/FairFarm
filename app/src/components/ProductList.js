// src/components/ProductList.js

import React, { useState, useEffect } from 'react';
import { getProducts } from '../services/api';

const ProductList = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const fetchProducts = async () => {
            const data = await getProducts();
            setProducts(data);
        };
        fetchProducts();
    }, []);

    return (
        <div>
            <h1>Product Listings</h1>
            <ul>
                {products.map(product => (
                    <li key={product.id}>
                        <h3>{product.name}</h3>
                        <p>Price: ${product.price}</p>
                        <p>Category: {product.category}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ProductList;
