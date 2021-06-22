import * as React from "react";
import { Admin, Resource, ListGuesser} from 'react-admin';
import jsonServerProvider from 'ra-data-json-server';
import { OrderEdit, OrderCreate, OrderList} from './Orders';

const dataProvider = jsonServerProvider('https://jsonplaceholder.typicode.com');
const AdminComponent = () => (
    <Admin dataProvider={dataProvider}>
        <Resource name="users" list={ListGuesser} />
        <Resource name="orders" list={OrderList} create={OrderCreate} edit={OrderEdit}/>
    </Admin>
);

export default AdminComponent;