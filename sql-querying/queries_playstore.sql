-- Comments in SQL Start with dash-dash --

-- 1. Find the app with an ID of 1880. --
SELECT * FROM analytics WHERE id - 1880;

-- 2. Find the ID and app name for all apps that were last updated on August 01, 2018. --
SELECT id, name FROM analytics WHERE last_updated > '2018-08-01';

-- 3. Count the number of apps in each category, e.g. “Family | 1972”. --
SELECT category, COUNT(*) FROM analytics GROUP BY category;

-- 4. Find the top 5 most-reviewed apps and the number of reviews for each. rating, reviews --
SELECT app_name, rating, reviews FROM analytics WHERE rating <= 5 ORDER BY rating desc LIMIT 5;

-- 5. Find the app that has the most reviews with a rating greater than equal to 4.8. --
SELECT app_name, reviews, rating FROM analytics WHERE rating >= 4.8 ORDER BY reviews desc LIMIT 1;

-- 6. Find the average rating for each category ordered by the highest rated to lowest rated. --
