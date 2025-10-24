-- insert data into tables
USE task_management;

-- Insert 5 users
INSERT INTO users (name, email)
VALUES
('Sokol', 'sokol@example.com'),
('Alba', 'alba@example.com'),
('Enea', 'enea@example.com'),
('Antonela', 'antonela@example.com'),
('Renis', 'renis@example.com');

-- Insert 20 simple tasks
INSERT INTO tasks (user_id, description, status, due_date)
VALUES
-- Tasks for Sokol (user_id = 1)
(1, 'Buy groceries', 'pending', '2025-11-01'),
(1, 'Call the client', 'completed', '2025-10-20'),
(1, 'Clean desk', 'pending', '2025-11-02'),
(1, 'Send report', 'in progress', '2025-11-03'),

-- Tasks for Alba (user_id = 2)
(2, 'Check emails', 'completed', '2025-10-22'),
(2, 'Update document', 'pending', '2025-11-04'),
(2, 'Print invoice', 'in progress', '2025-11-05'),
(2, 'Plan meeting', 'pending', '2025-11-06'),

-- Tasks for Enea (user_id = 3)
(3, 'Fix typo in code', 'completed', '2025-10-18'),
(3, 'Push commits', 'pending', '2025-11-07'),
(3, 'Read feedback', 'in progress', '2025-11-08'),
(3, 'Test feature', 'pending', '2025-11-09'),

-- Tasks for Antonela (user_id = 4)
(4, 'Write notes', 'completed', '2025-10-19'),
(4, 'Check messages', 'pending', '2025-11-10'),
(4, 'Book meeting room', 'in progress', '2025-11-11'),
(4, 'Update profile', 'pending', '2025-11-12'),

-- Tasks for Renis (user_id = 5)
(5, 'Water plants', 'pending', '2025-11-01'),
(5, 'Backup files', 'in progress', '2025-11-13'),
(5, 'Clean keyboard', 'completed', '2025-10-21'),
(5, 'Pay bills', 'pending', '2025-11-14');