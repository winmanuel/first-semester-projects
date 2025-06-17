CREATE TABLE Customers(

    customer_id SERIAL PRIMARY KEY,

    custome_name VARCHAR(255) NOT NULL,

    email VARCHAR(255),

    join_date DATE DEFAULT CURRENT_DATE
);


 CREATE TABLE Products(

    product_id SERIAL PRIMARY KEY,

    product_name VARCHAR(255) NOT NULL,

    category VARCHAR(255),

    price DECIMAL(10, 2)
 );   
    
    
CREATE table Orders (

    order_id SERIAL PRIMARY KEY,
    
    customer_id INT,
    
    product_id INT,

    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),

    FOREIGN KEY (product_id) REFERENCES Products(product_id),

    quantity int,

    order_date DATE DEFAULT CURRENT_DATE
   );