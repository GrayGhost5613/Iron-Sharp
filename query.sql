CREATE TABLE products (
    productid INT PRIMARY KEY,
    image TEXT,
    title VARCHAR(255),
    product_description TEXT,
    quantity INT,
    price DECIMAL(10, 2)
);
INSERT INTO products (productid, image, title, product_description, quantity, price) VALUES
(1, 'static/Product Images/1.png', 'IronSharp Striker Jersey', 'High-performance jersey for the attacking player.', 50, 29.99),
(2, 'static/Product Images/2.png', 'IronSharp Defender Jersey', 'Robust and comfortable, perfect for the defensive line.', 50, 28.99),
(3, 'static/Product Images/3.png', 'IronSharp Midfield Master', 'Specially designed for the playmakers in the midfield.', 50, 30.99),
(4, 'static/Product Images/4.png', 'IronSharp Goalkeeper Gear', 'Durable and agile jersey for the goalkeepers.', 50, 31.99),
(5, 'static/Product Images/5.png', 'IronSharp Classic Home Kit', 'Traditional home colors with a modern twist.', 50, 27.99),
(6, 'static/Product Images/6.png', 'IronSharp Away Attire', 'Bold and striking design for away matches.', 50, 26.99),
(7, 'static/Product Images/7.png', 'IronSharp Training Top', 'Lightweight and breathable for training sessions.', 50, 24.99),
(8, 'static/Product Images/8.png', 'IronSharp Youth Jersey', 'Specially sized for younger fans and players.', 50, 22.99),
(9, 'static/Product Images/9.png', 'IronSharp Vintage Vibe', 'Retro design inspired by the club’s history.', 50, 29.99),
(10, 'static/Product Images/10.png', 'IronSharp Champion Edition', 'Special edition celebrating recent victories.', 50, 32.99),
(11, 'static/Product Images/11.png', 'IronSharp Wing Wizard', 'For the fast and agile wingers.', 50, 28.99),
(12, 'static/Product Images/12.png', 'IronSharp Captain’s Choice', 'Inspired by the team’s leaders on the field.', 50, 31.49),
(13, 'static/Product Images/13.png', 'IronSharp Fan Favorite', 'Most loved design by the fan community.', 50, 25.99),
(14, 'static/Product Images/14.png', 'IronSharp Limited Edition', 'Exclusive design with limited availability.', 50, 33.99),
(15, 'static/Product Images/15.png', 'IronSharp Winter Warmer', 'Extra insulation for colder match days.', 50, 29.99),
(16, 'static/Product Images/16.png', 'IronSharp Summer Special', 'Ultra-light for warmer days.', 50, 24.99),
(17, 'static/Product Images/17.png', 'IronSharp Elite Pro', 'Top-tier jersey for the most demanding players.', 50, 34.99),
(18, 'static/Product Images/18.png', 'IronSharp Heritage Honor', 'Paying homage to the club’s origins.', 50, 28.49),
(19, 'static/Product Images/19.png', 'IronSharp Future Star', 'Futuristic design for the next generation.', 50, 27.99),
(20, 'static/Product Images/20.png', 'IronSharp Global Game', 'Celebrating the global love for the sport.', 50, 26.99);