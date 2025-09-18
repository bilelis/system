-- Insert sample users
INSERT INTO users (username, password_hash, role, full_name, email) VALUES
('admin', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewKyBAWjR3Ud6Z3K', 'admin', 'Admin User', 'admin@hotel.com'),
('reception1', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewKyBAWjR3Ud6Z3K', 'receptionist', 'John Smith', 'john@hotel.com'),
('cashier1', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewKyBAWjR3Ud6Z3K', 'cashier', 'Sarah Johnson', 'sarah@hotel.com');

-- Insert sample rooms
INSERT INTO rooms (room_number, room_type, floor, status, rate_per_night, capacity, features) VALUES
('101', 'Standard', 1, 'available', 100.00, 2, '{"wifi": true, "tv": true, "minibar": true}'),
('102', 'Standard', 1, 'available', 100.00, 2, '{"wifi": true, "tv": true, "minibar": true}'),
('201', 'Deluxe', 2, 'available', 150.00, 2, '{"wifi": true, "tv": true, "minibar": true, "balcony": true}'),
('202', 'Deluxe', 2, 'available', 150.00, 2, '{"wifi": true, "tv": true, "minibar": true, "balcony": true}'),
('301', 'Suite', 3, 'available', 250.00, 4, '{"wifi": true, "tv": true, "minibar": true, "balcony": true, "kitchen": true}');

-- Insert sample outlets
INSERT INTO outlets (name, type, location, opening_hours, is_active) VALUES
('Main Restaurant', 'restaurant', 'Ground Floor', '{"monday": "07:00-22:00", "tuesday": "07:00-22:00", "wednesday": "07:00-22:00", "thursday": "07:00-22:00", "friday": "07:00-23:00", "saturday": "07:00-23:00", "sunday": "07:00-22:00"}', true),
('Lobby Bar', 'bar', 'Ground Floor', '{"monday": "12:00-00:00", "tuesday": "12:00-00:00", "wednesday": "12:00-00:00", "thursday": "12:00-00:00", "friday": "12:00-02:00", "saturday": "12:00-02:00", "sunday": "12:00-00:00"}', true),
('Pool Bar', 'bar', 'Pool Area', '{"monday": "10:00-18:00", "tuesday": "10:00-18:00", "wednesday": "10:00-18:00", "thursday": "10:00-18:00", "friday": "10:00-19:00", "saturday": "10:00-19:00", "sunday": "10:00-18:00"}', true);

-- Insert sample items for Main Restaurant
INSERT INTO items (outlet_id, name, description, category, price, is_available) 
SELECT 
    o.id,
    name,
    description,
    category,
    price,
    true
FROM outlets o,
(VALUES 
    ('Grilled Salmon', 'Fresh salmon with seasonal vegetables', 'Main Course', 25.00),
    ('Caesar Salad', 'Classic caesar salad with chicken', 'Starter', 12.00),
    ('Beef Steak', 'Grilled beef steak with mashed potatoes', 'Main Course', 30.00),
    ('Chocolate Cake', 'Rich chocolate cake with vanilla ice cream', 'Dessert', 8.00)
) AS items(name, description, category, price)
WHERE o.name = 'Main Restaurant';

-- Insert sample items for Lobby Bar
INSERT INTO items (outlet_id, name, description, category, price, is_available)
SELECT 
    o.id,
    name,
    description,
    category,
    price,
    true
FROM outlets o,
(VALUES 
    ('Mojito', 'Classic Cuban cocktail', 'Cocktails', 12.00),
    ('Wine by Glass', 'Selection of red and white wines', 'Wine', 10.00),
    ('Club Sandwich', 'Triple-decker sandwich with fries', 'Snacks', 15.00),
    ('Cheese Plate', 'Selection of international cheeses', 'Snacks', 18.00)
) AS items(name, description, category, price)
WHERE o.name = 'Lobby Bar';