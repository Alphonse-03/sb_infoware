
CREATE TABLE Restaurants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL
);

CREATE TABLE Dishes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    restaurant_id INT REFERENCES Restaurants(id) ON DELETE CASCADE,
    price DECIMAL(10,2) NOT NULL
);

CREATE TABLE Orders (
    id SERIAL PRIMARY KEY,
    dish_id INT REFERENCES Dishes(id) ON DELETE CASCADE,
    customer_name VARCHAR(255) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'Pending' CHECK (status IN ('Pending', 'Completed', 'Cancelled'))
);

-- SQL Queries:
-- Q1)Write an optimized SQL query to find the top 5 most ordered dishes in the last 30 days.
-- Q2)Write an SQL query to get a list of restaurants that have at least 5 different dishes on their menu.






-- ans1)
Select d.name,COUNT(o.id) as order_count
From Dishes d
JOIN Orders o ON d.id = o.dish_id
Where o.order_date >= datetime('now', '-30 days')
Group by d.name
order by order_count DESC
LIMIT 5;


-- ans 2)
Select r.name
From Restaurants r
JOIN Dishes d ON r.id = d.restaurant_id
Group by r.name
Having COUNT(DISTINCT d.id) >= 5


