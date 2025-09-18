-- Outlets
CREATE TABLE outlets (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    code VARCHAR(4) NOT NULL UNIQUE,
    type VARCHAR(50) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Items
CREATE TABLE items (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    outlet_id UUID NOT NULL REFERENCES outlets(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    is_available BOOLEAN DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Guests
CREATE TABLE guests (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Orders
CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    outlet_id UUID NOT NULL REFERENCES outlets(id),
    guest_id UUID REFERENCES guests(id),
    cashier_id UUID,
    total DECIMAL(10,2) NOT NULL,
    discount DECIMAL(10,2) DEFAULT 0,
    tax DECIMAL(10,2) DEFAULT 0,
    status VARCHAR(20) DEFAULT 'open',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Order Lines
CREATE TABLE order_lines (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    order_id UUID NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    item_id UUID NOT NULL REFERENCES items(id),
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    total_price DECIMAL(10,2) NOT NULL
);

-- Seed Outlets
INSERT INTO outlets (name, code, type) VALUES
('Bar', '1234', 'bar'),
('Restaurant1', '5678', 'kaftaji'),
('Restaurant2', '4321', 'chapati');

-- Seed Items
INSERT INTO items (outlet_id, name, category, price) SELECT id, 'Coca', 'Drink', 3.00 FROM outlets WHERE name='Bar';
INSERT INTO items (outlet_id, name, category, price) SELECT id, 'Whisky', 'Drink', 15.00 FROM outlets WHERE name='Bar';
INSERT INTO items (outlet_id, name, category, price) SELECT id, 'Kaftaji', 'Food', 8.00 FROM outlets WHERE name='Restaurant1';
INSERT INTO items (outlet_id, name, category, price) SELECT id, 'Ojja', 'Food', 10.00 FROM outlets WHERE name='Restaurant1';
INSERT INTO items (outlet_id, name, category, price) SELECT id, 'Chapati Poulet', 'Food', 7.00 FROM outlets WHERE name='Restaurant2';
INSERT INTO items (outlet_id, name, category, price) SELECT id, 'Chapati Viande', 'Food', 9.00 FROM outlets WHERE name='Restaurant2';

-- Seed Guests
INSERT INTO guests (first_name, last_name, phone, email) VALUES ('Bilel', 'Ben Salah', '22222222', 'bilel@hotel.com');

-- Seed Orders
-- Example: Order for Bar
INSERT INTO orders (outlet_id, guest_id, total, discount, tax, status) VALUES (
    (SELECT id FROM outlets WHERE name='Bar'),
    (SELECT id FROM guests WHERE first_name='Bilel'),
    18.00, 0, 1.80, 'closed'
);
-- Example: Order Lines for Bar Order
INSERT INTO order_lines (order_id, item_id, quantity, unit_price, total_price) VALUES (
    (SELECT id FROM orders WHERE total=18.00),
    (SELECT id FROM items WHERE name='Coca'),
    2, 3.00, 6.00
);
INSERT INTO order_lines (order_id, item_id, quantity, unit_price, total_price) VALUES (
    (SELECT id FROM orders WHERE total=18.00),
    (SELECT id FROM items WHERE name='Whisky'),
    1, 15.00, 15.00
);
