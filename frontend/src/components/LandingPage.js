import React, {Component} from 'react';
import ProductFilter from "./landingPage/ProductFilter";
import ProductList from "./landingPage/ProductList";

class ProductPage extends Component {
    render() {
        return<div className="box">
            <ProductFilter/>
            <ProductList/>
        </div>


    }
}

export default ProductPage;