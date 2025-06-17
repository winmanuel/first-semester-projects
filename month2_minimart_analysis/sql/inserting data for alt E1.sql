INSERT INTO customers (custome_name, email, join_date) VALUES
('Alice Johnson', 'alice.johnson@example.com', '2023-01-15'),
('Bob Smith', 'bob.smith@example.com', '2023-02-20'),
('Carol Lee', 'carol.lee@example.com', '2023-03-10'),
('David Kim', 'david.kim@example.com', '2023-04-05'),
('Eva Brown', 'eva.brown@example.com', '2023-05-22'),
('Frank White', 'frank.white@example.com', '2023-06-18'),
('Grace Green', 'grace.green@example.com', '2023-07-01'),
('Hannah Scott', 'hannah.scott@example.com', '2023-07-25'),
('Ian Turner', 'ian.turner@example.com', '2023-08-14'),
('Julia Adams', 'julia.adams@example.com', '2023-09-02');


INSERT INTO products (product_name, category, price) VALUES
('Wireless Mouse', 'Electronics', 25.99),
('Bluetooth Speaker', 'Electronics', 45.50),
('Coffee Mug', 'Kitchenware', 12.00),
('Yoga Mat', 'Sports', 35.75),
('Desk Lamp', 'Furniture', 28.40),
('Water Bottle', 'Sports', 15.00),
('Notebook', 'Stationery', 7.25),
('Ballpoint Pen', 'Stationery', 2.50),
('Backpack', 'Accessories', 55.00),
('USB Cable', 'Electronics', 8.99);


INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 2, 1, '2023-10-01'),
(2, 1, 2, '2023-10-02'),
(3, 5, 1, '2023-10-03'),
(4, 3, 4, '2023-10-04'),
(5, 9, 1, '2023-10-05'),
(6, 7, 3, '2023-10-06'),
(7, 4, 2, '2023-10-07'),
(8, 6, 1, '2023-10-08'),
(9, 10, 5, '2023-10-09'),
(10, 8, 6, '2023-10-10');



