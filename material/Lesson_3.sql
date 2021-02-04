-- NULL --

SELECT *
FROM accounts
WHERE primary_poc IS NULL;


SELECT *
FROM accounts
WHERE primary_poc IS NOT NULL;


SELECT COUNT (*)
FROM accounts;


SELECT COUNT(accounts.id)
FROM accounts;


-- SUM --


SELECT SUM(standar_qty) AS standard,
	   SUM(gloss_qty) AS gloss,
	   SUM(poster_qty) AS poster
FROM orders;


SELECT SUM(poster_qty) AS total_poster_sales
FROM orders;


SELECT SUM(standard_qty) AS total_standard_sales
FROM orders;


SELECT SUM(total_amt_usd) AS total_dollar_sales
FROM orders;


SELECT standard_amt_usd + gloss_amt_usd AS total_standard_gloss
FROM orders;


SELECT SUM(standard_amt_usd)/SUM(standard_qty) AS standard_price_per_unit
FROM orders;


-- MIN, MAX, AVG --


SELECT MIN(standard_qty) AS standard_min,
	   MAX(standard_qty) AS standard_max
FROM orders;


SELECT AVG(standard_qty) AS standard_avg
FROM orders;


SELECT occurred_at 
FROM orders
ORDER BY occurred_at DESC
LIMIT 1;


SELECT MIN(occurred_at)
FROM orders;


SELECT occurred_at
FROM web_events
ORDER BY occurred_at DESC
LIMIT 1;


SELECT MAX(occurred_at)
FROM web_events;


SELECT AVG(standard_amt_usd) AS mean_spent_standard, 
       AVG(gloss_amt_usd) AS mean_spent_gloss,
       AVG(poster_amt_usd) AS mean_spent_poster,
       AVG(standard_qty) AS mean_amount_standard,
       AVG(gloss_qty) AS mean_amount_gloss,
       AVG(poster_qty) AS mean_amount_poster
FROM orders;       


SELECT *
FROM (SELECT total_amt_usd
      FROM orders
      ORDER BY total_amt_usd
      LIMIT 3457) AS Table1
ORDER BY total_amt_usd DESC
LIMIT 2;


-- GROUP BY --


SELECT account_id,
       SUM(standard_qty) AS standard_sum,
       SUM(gloss_qty) AS gloss_sum,
       SUM(poster_qty) AS poster_sum
    FROM orders
  GROUP BY account_id
  ORDER BY account_id;


SELECT a.name, o.occurred_at
FROM accounts a
JOIN orders o
ON a.id = o.account_id
ORDER BY o.occurred_at
LIMIT 1;


SELECT a.name, SUM(o.total_amt_usd) total_sales
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.name;


SELECT w.occurred_at date, w.channel, a.name account_name
FROM accounts a
JOIN web_events w
ON w.account_id = a.id
ORDER BY w.occurred_at DESC
LIMIT 1;


SELECT channel, COUNT(*)
FROM web_events
GROUP BY channel


SELECT a.primary_poc
FROM accounts a
JOIN web_events w
ON w.account_id = a.id
ORDER BY w.occurred_at
LIMIT 1;


SELECT a.name, MIN(o.total_amt_usd) smallest order
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.name
ORDER BY MIN(o.total_amt_usd), a.name;


SELECT r.name, COUNT(*) num_reps
FROM region r
JOIN sales_reps s
ON r.id = s.region_id
GROUP BY r.name
ORDER BY num_reps;


-- GROUP BY MULTIPLE COLUMNS --

SELECT account_id,
	   channel,
	   COUNT(id) AS events 
   FROM web_events
  GROUP BY account_id, channel
  ORDER BY account_id, events DESC;


SELECT a.name, AVG(o.standard_qty) avg_stand, AVG(o.gloss_qty) avg_gloss, AVG(o.poster_qty) avg_post
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.name;


SELECT a.name, AVG(o.standard_amt_usd) avg_stand, AVG(o.gloss_amt_usd) avg_gloss, AVG(o.poster_amt_usd) avg_post
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.name;


SELECT s.name name_rep, w.channel, COUNT(*) num_events 
FROM web_events w
JOIN accounts a 
ON w.account_id = a.id
JOIN sales_reps s 
ON a.sales_rep_id = s.id
GROUP BY s.name, w.channel
ORDER BY num_events DESC;


SELECT r.name, w.channel, COUNT(*) num_events
FROM web_events w 
JOIN accounts a
ON w.account_id = a.id
JOIN sales_reps s
ON s.id = a.sales_rep_id
JOIN region r
ON s.region_id = r.id
GROUP BY r.name, w.channel
ORDER BY num_events DESC;


SELECT a.id as "account id", r.id as "region id", 
a.name as "account name", r.name as "region name"
FROM accounts a
JOIN sales_reps s
ON s.id = a.sales_rep_id
JOIN region r
ON r.id = s.region_id;


SELECT DISTINCT id, name
FROM accounts;


SELECT s.id, s.name, COUNT(*) num_accounts
FROM accounts a
JOIN sales_reps s
ON s.id = a.sales_rep_id
GROUP BY s.id, s.name
ORDER BY num_accounts;


-- HAVING --


SELECT account_id
       SUM(total_amt_usd) AS sum_total_amt_usd
  FROM orders
 GROUP BY 1
 HAVING SUM(total_amt_usd) >= 250000


SELECT s.id, s.name, COUNT(*) num_accounts
FROM accounts a
JOIN sales_reps s
ON s.id = a.sales_rep_id
GROUP BY s.id, s.name
HAVING COUNT(*) > 5
ORDER BY num_accounts;


SELECT a.id, a.name, COUNT(*) num_orders
FROM accounts a 
JOIN orders o 
ON a.id = o.account_id
GROUP BY a.id, a.name
HAVING COUNT(*) > 20
ORDER BY num_orders;


SELECT a.id account_id, a.name account_name, COUNT(*) num_orders
FROM accounts a 
JOIN orders o 
ON a.id = o.account_id
GROUP BY a.id, a.name 
ORDER BY num_orders DESC
LIMIT 1;


SELECT a.id, a.name, SUM(o.total_amt_usd) total_spent
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.id, a.name
HAVING SUM(o.total_amt_usd) > 30000
ORDER BY total_spent;


SELECT a.id, a.name, SUM(o.total_amt_usd) total_spent
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.id, a.name
HAVING SUM(o.total_amt_usd) < 1000
ORDER BY total_spent;


SELECT a.id, a.name, SUM(o.total_amt_usd) total_spent
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.id, a.name
ORDER BY total_spent
LIMIT 1;


SELECT a.id, a.name, w.channel, COUNT(*) use_of_channel
FROM accounts a
JOIN web_events w
ON a.id = w.account_id
GROUP BY a.id, a.name, w.channel
HAVING COUNT(*) > 6 AND w.channel = 'facebook'
ORDER BY use_of_channel;


SELECT a.id, a.name, w.channel, COUNT(*) use_of_channel
FROM accounts a
JOIN web_events w
ON a.id = w.account_id
GROUP BY a.id, a.name, w.channel
HAVING COUNT(*) > 6 AND w.channel = 'facebook'
ORDER BY use_of_channel DESC
LIMIT 1;


SELECT a.id, a.name, w.channel, COUNT(*) use_of_channel
FROM accounts a
JOIN web_events w
ON a.id = w.account_id
GROUP BY a.id, a.name, w.channel
HAVING COUNT(*) > 6 AND w.channel = 'facebook'
ORDER BY use_of_channel DESC
LIMIT 1;


-- DATE --


SELECT DATE_TRUNC('day', occurred_at) AS day,
       SUM(standard_qty) AS standard_qty_sum
  FROM orders
 GROUP BY 1
 ORDER BY 1;


 SELECT DATE_PART('dow', occurred_at) AS day_of_week,
        SUM(total) AS total_qty
    FROM orders
  GROUP BY 1
  ORDER BY 2 DESC;


 SELECT DATE_PART('year', occurred_at) ord_year,  SUM(total_amt_usd) total_spent
 FROM orders
 GROUP BY 1
 ORDER BY 2 DESC;


SELECT DATE_PART('month', occurred_at) ord_month,  SUM(total_amt_usd) total_spent
 FROM orders
 GROUP BY 1
 ORDER BY 2 DESC;


SELECT DATE_PART('month', occurred_at) ord_month,  COUNT(*) total_sales
FROM orders
GROUP BY 1
ORDER BY 2 DESC;


SELECT DATE_PART('month', o.occurred_at) month_occ, 
       DATE_PART('year', o.occurred_at) year_occ,
       SUM(o.gloss_amt_usd) total_gloss_amt_used 
FROM orders o
JOIN accounts a 
ON o.account_id = a.id
WHERE a.name = 'Walmart'
GROUP BY 1, 2
ORDER BY total_gloss_amt_used DESC;


-- CASE --


SELECT id,
       account_id,
       occurred_at,
       channel,
       CASE WHEN channel = 'facebook' THEN 'yes' ELSE 'no' END AS is_facebook
    FROM web_events
  ORDER BY occurred_at;


  SELECT account_id,
         occurred_at,
         total,
         CASE WHEN total > 500 THEN 'Over 500'
              WHEN total > 300 AND total <= 500 THEN '301 - 500'
              WHEN total > 100 AND total <= 300 THEN '101 - 300'
              ELSE '100 or under' END AS total_group
    FROM orders;


SELECT account_id, CASE WHEN standard_qty = 0 OR standard_qty IS NULL THEN 0
                        ELSE standard_amt_usd/standard_qty END AS unit_price
FROM orders
LIMIT 10;


SELECT id order_id, account_id, total_amt_usd total_amount_order, 
       CASE WHEN total_amt_usd >= 3000 THEN 'Large'
       ELSE 'Small' END AS level_of_order
FROM orders;


SELECT CASE WHEN total >= 2000 THEN 'At Least 2000'
   WHEN total >= 1000 AND total < 2000 THEN 'Between 1000 and 2000'
   ELSE 'Less than 1000' END AS order_category,
COUNT(*) AS order_count
FROM orders
GROUP BY 1;


SELECT a.name, SUM(total_amt_usd) total_spent, 
     CASE WHEN SUM(total_amt_usd) > 200000 THEN 'top'
     WHEN  SUM(total_amt_usd) > 100000 THEN 'middle'
     ELSE 'low' END AS customer_level
FROM orders o
JOIN accounts a
ON o.account_id = a.id 
GROUP BY a.name
ORDER BY 2 DESC;


SELECT a.name, SUM(total_amt_usd) total_spent, 
     CASE WHEN SUM(total_amt_usd) > 200000 THEN 'top'
     WHEN  SUM(total_amt_usd) > 100000 THEN 'middle'
     ELSE 'low' END AS customer_level
FROM orders o
JOIN accounts a
ON o.account_id = a.id
WHERE occurred_at > '2015-12-31' 
GROUP BY 1
ORDER BY 2 DESC;


SELECT s.name, COUNT(*) num_ords,
     CASE WHEN COUNT(*) > 200 THEN 'top'
     ELSE 'not' END AS sales_rep_level
FROM orders o
JOIN accounts a
ON o.account_id = a.id 
JOIN sales_reps s
ON s.id = a.sales_rep_id
GROUP BY s.name
ORDER BY 2 DESC;


SELECT s.name, COUNT(*), SUM(o.total_amt_usd) total_spent, 
     CASE WHEN COUNT(*) > 200 OR SUM(o.total_amt_usd) > 750000 THEN 'top'
     WHEN COUNT(*) > 150 OR SUM(o.total_amt_usd) > 500000 THEN 'middle'
     ELSE 'low' END AS sales_rep_level
FROM orders o
JOIN accounts a
ON o.account_id = a.id 
JOIN sales_reps s
ON s.id = a.sales_rep_id
GROUP BY s.name
ORDER BY 3 DESC;


