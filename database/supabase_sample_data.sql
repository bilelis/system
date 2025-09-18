-- Sample Data for Hotel Management System in Supabase
-- بيانات تجريبية لنظام إدارة الفنادق في Supabase
-- 
-- Instructions: Run after creating the schema
-- تعليمات: قم بالتشغيل بعد إنشاء المخطط

-- === SAMPLE OUTLETS ===
INSERT INTO outlets (id, name, description) VALUES 
('550e8400-e29b-41d4-a716-446655440001', 'Restaurant', 'Main hotel restaurant'),
('550e8400-e29b-41d4-a716-446655440002', 'Bar & Lounge', 'Hotel bar and lounge area'),
('550e8400-e29b-41d4-a716-446655440003', 'Room Service', 'In-room dining service'),
('550e8400-e29b-41d4-a716-446655440004', 'Spa & Wellness', 'Spa treatments and wellness');

-- === SAMPLE ROOMS ===
INSERT INTO rooms (id, room_number, room_type, floor, rate_per_night, capacity, features) VALUES 
('660e8400-e29b-41d4-a716-446655440001', '101', 'Standard Single', 1, 120.00, 1, '{"wifi": true, "tv": true, "ac": true}'),
('660e8400-e29b-41d4-a716-446655440002', '102', 'Standard Double', 1, 180.00, 2, '{"wifi": true, "tv": true, "ac": true, "minibar": true}'),
('660e8400-e29b-41d4-a716-446655440003', '103', 'Standard Twin', 1, 180.00, 2, '{"wifi": true, "tv": true, "ac": true}'),
('660e8400-e29b-41d4-a716-446655440004', '201', 'Deluxe Suite', 2, 350.00, 3, '{"wifi": true, "tv": true, "ac": true, "minibar": true, "balcony": true, "jacuzzi": true}'),
('660e8400-e29b-41d4-a716-446655440005', '202', 'Executive Suite', 2, 450.00, 4, '{"wifi": true, "tv": true, "ac": true, "minibar": true, "balcony": true, "jacuzzi": true, "kitchen": true}'),
('660e8400-e29b-41d4-a716-446655440006', '301', 'Presidential Suite', 3, 800.00, 6, '{"wifi": true, "tv": true, "ac": true, "minibar": true, "balcony": true, "jacuzzi": true, "kitchen": true, "office": true}');

-- === SAMPLE GUESTS ===
INSERT INTO guests (id, first_name, last_name, email, phone, nationality, passport_no) VALUES 
('770e8400-e29b-41d4-a716-446655440001', 'Ahmed', 'Ben Ali', 'ahmed.benali@email.com', '+216-98-123-456', 'Tunisia', 'TN1234567'),
('770e8400-e29b-41d4-a716-446655440002', 'Sarah', 'Johnson', 'sarah.johnson@email.com', '+1-555-123-4567', 'USA', 'US7654321'),
('770e8400-e29b-41d4-a716-446655440003', 'Mohamed', 'Trabelsi', 'mohamed.trabelsi@email.com', '+216-22-987-654', 'Tunisia', 'TN9876543'),
('770e8400-e29b-41d4-a716-446655440004', 'Emma', 'Wilson', 'emma.wilson@email.com', '+44-20-1234-5678', 'UK', 'GB1357924');

-- === SAMPLE ITEMS ===
INSERT INTO items (outlet_id, name, description, price, category) VALUES 
-- Restaurant items
('550e8400-e29b-41d4-a716-446655440001', 'Grilled Fish', 'Fresh grilled fish with vegetables', 28.50, 'Main Course'),
('550e8400-e29b-41d4-a716-446655440001', 'Couscous Royal', 'Traditional Tunisian couscous', 22.00, 'Main Course'),
('550e8400-e29b-41d4-a716-446655440001', 'Caesar Salad', 'Fresh caesar salad with croutons', 15.00, 'Appetizer'),
('550e8400-e29b-41d4-a716-446655440001', 'Makloubeh', 'Traditional rice dish with lamb', 32.00, 'Main Course'),

-- Bar items
('550e8400-e29b-41d4-a716-446655440002', 'Local Beer', 'Tunisian Celtia beer', 5.50, 'Beverage'),
('550e8400-e29b-41d4-a716-446655440002', 'Mojito', 'Fresh mint mojito cocktail', 12.00, 'Cocktail'),
('550e8400-e29b-41d4-a716-446655440002', 'Coffee', 'Espresso coffee', 3.50, 'Hot Beverage'),
('550e8400-e29b-41d4-a716-446655440002', 'Fresh Orange Juice', 'Freshly squeezed orange juice', 6.00, 'Beverage'),

-- Room Service items
('550e8400-e29b-41d4-a716-446655440003', 'Continental Breakfast', 'Breakfast served in room', 18.00, 'Breakfast'),
('550e8400-e29b-41d4-a716-446655440003', 'Club Sandwich', 'Classic club sandwich with fries', 16.50, 'Light Meal'),
('550e8400-e29b-41d4-a716-446655440003', 'Fruit Platter', 'Fresh seasonal fruits', 12.00, 'Healthy'),

-- Spa items
('550e8400-e29b-41d4-a716-446655440004', 'Relaxing Massage', '60-minute full body massage', 85.00, 'Treatment'),
('550e8400-e29b-41d4-a716-446655440004', 'Facial Treatment', 'Deep cleansing facial', 65.00, 'Treatment'),
('550e8400-e29b-41d4-a716-446655440004', 'Hammam Session', 'Traditional Tunisian hammam', 45.00, 'Treatment');

-- Note: Users will be created via Supabase Auth, but you can create some sample users for testing
-- ملاحظة: سيتم إنشاء المستخدمين عبر مصادقة Supabase، ولكن يمكنك إنشاء بعض المستخدمين التجريبيين للاختبار

-- Insert sample users (these would normally be created via Supabase Auth)
INSERT INTO users (id, username, email, full_name, role) VALUES 
('880e8400-e29b-41d4-a716-446655440001', 'admin', 'admin@hotel.com', 'Hotel Administrator', 'admin'),
('880e8400-e29b-41d4-a716-446655440002', 'receptionist1', 'reception@hotel.com', 'Front Desk Staff', 'receptionist'),
('880e8400-e29b-41d4-a716-446655440003', 'cashier1', 'cashier@hotel.com', 'Cashier Staff', 'cashier');

-- === SAMPLE BOOKINGS ===
INSERT INTO bookings (guest_id, room_id, user_id, check_in_date, check_out_date, total_amount, status) VALUES 
('770e8400-e29b-41d4-a716-446655440001', '660e8400-e29b-41d4-a716-446655440001', '880e8400-e29b-41d4-a716-446655440002', '2024-01-15', '2024-01-18', 360.00, 'confirmed'),
('770e8400-e29b-41d4-a716-446655440002', '660e8400-e29b-41d4-a716-446655440004', '880e8400-e29b-41d4-a716-446655440002', '2024-01-20', '2024-01-25', 1750.00, 'checked_in'),
('770e8400-e29b-41d4-a716-446655440003', '660e8400-e29b-41d4-a716-446655440002', '880e8400-e29b-41d4-a716-446655440002', '2024-01-22', '2024-01-24', 360.00, 'pending');

-- === SAMPLE ORDERS ===
INSERT INTO orders (id, guest_id, outlet_id, user_id, order_number, total_amount, status) VALUES 
('990e8400-e29b-41d4-a716-446655440001', '770e8400-e29b-41d4-a716-446655440001', '550e8400-e29b-41d4-a716-446655440001', '880e8400-e29b-41d4-a716-446655440003', 'ORD-2024-001', 65.50, 'completed'),
('990e8400-e29b-41d4-a716-446655440002', '770e8400-e29b-41d4-a716-446655440002', '550e8400-e29b-41d4-a716-446655440002', '880e8400-e29b-41d4-a716-446655440003', 'ORD-2024-002', 23.50, 'completed'),
('990e8400-e29b-41d4-a716-446655440003', '770e8400-e29b-41d4-a716-446655440002', '550e8400-e29b-41d4-a716-446655440004', '880e8400-e29b-41d4-a716-446655440003', 'ORD-2024-003', 150.00, 'pending');

-- === SAMPLE ORDER LINES ===
INSERT INTO order_lines (order_id, item_id, quantity, unit_price, total_price) VALUES 
-- Order 1 items
('990e8400-e29b-41d4-a716-446655440001', (SELECT id FROM items WHERE name = 'Grilled Fish' LIMIT 1), 1, 28.50, 28.50),
('990e8400-e29b-41d4-a716-446655440001', (SELECT id FROM items WHERE name = 'Caesar Salad' LIMIT 1), 1, 15.00, 15.00),
('990e8400-e29b-41d4-a716-446655440001', (SELECT id FROM items WHERE name = 'Couscous Royal' LIMIT 1), 1, 22.00, 22.00),

-- Order 2 items
('990e8400-e29b-41d4-a716-446655440002', (SELECT id FROM items WHERE name = 'Mojito' LIMIT 1), 1, 12.00, 12.00),
('990e8400-e29b-41d4-a716-446655440002', (SELECT id FROM items WHERE name = 'Coffee' LIMIT 1), 2, 3.50, 7.00),
('990e8400-e29b-41d4-a716-446655440002', (SELECT id FROM items WHERE name = 'Local Beer' LIMIT 1), 1, 5.50, 5.50),

-- Order 3 items
('990e8400-e29b-41d4-a716-446655440003', (SELECT id FROM items WHERE name = 'Relaxing Massage' LIMIT 1), 1, 85.00, 85.00),
('990e8400-e29b-41d4-a716-446655440003', (SELECT id FROM items WHERE name = 'Facial Treatment' LIMIT 1), 1, 65.00, 65.00);

-- === SAMPLE PAYMENTS ===
INSERT INTO payments (booking_id, amount, payment_method, payment_status, transaction_id) VALUES 
((SELECT id FROM bookings WHERE guest_id = '770e8400-e29b-41d4-a716-446655440001' LIMIT 1), 360.00, 'credit_card', 'completed', 'TXN-2024-001'),
((SELECT id FROM bookings WHERE guest_id = '770e8400-e29b-41d4-a716-446655440002' LIMIT 1), 875.00, 'cash', 'completed', 'TXN-2024-002');

INSERT INTO payments (order_id, amount, payment_method, payment_status, transaction_id) VALUES 
('990e8400-e29b-41d4-a716-446655440001', 65.50, 'room_charge', 'completed', 'TXN-2024-003'),
('990e8400-e29b-41d4-a716-446655440002', 23.50, 'cash', 'completed', 'TXN-2024-004');