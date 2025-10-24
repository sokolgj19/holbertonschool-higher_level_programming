-- queries for users and tasks
USE task_management;
-- 1. Retrieve all users
    -- SELECT * FROM users;
-- 2. Retrieve all tasks with their associated user names
    -- SELECT users.name AS user_name, tasks.description
    -- FROM tasks
    -- JOIN users ON tasks.user_id = users.id;
-- 3. Find all pending tasks
    -- SELECT * FROM tasks WHERE status = 'pending';
-- 4. All tasks due before 7 days from now
    -- SELECT * FROM tasks WHERE due_date < '2025-10-31';
-- 5. Count of tasks per user
    SELECT users.name, COUNT(tasks.id) AS task_count
    FROM users
    LEFT JOIN tasks ON users.id = tasks.user_id
    GROUP BY users.id;