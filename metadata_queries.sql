-- Query 1:
```sql
WITH RankedSales AS (
    SELECT
        column1,
        column2,
        column3,
        CASE
            WHEN country_name = 'USA' THEN 'North America'
            WHEN country_name = 'Canada' THEN 'North America'
            WHEN country_name = 'Mexico' THEN 'North America'
            WHEN country_name = 'UK' THEN 'Europe'
            WHEN country_name = 'Germany' THEN 'Europe'
            WHEN country_name = 'France' THEN 'Europe'
            WHEN country_name = 'Japan' THEN 'Asia'
            WHEN country_name = 'China' THEN 'Asia'
            WHEN country_name = 'India' THEN 'Asia'
            ELSE 'Other'  -- Catch-all for other countries
        END AS region,
        ROW_NUMBER() OVER (PARTITION BY column1 ORDER BY column2) as row_num
    FROM
        sales_data
    WHERE
        column1 > 100
)
SELECT
    column1,
    column2,
    column3,
    region
FROM
    RankedSales
WHERE 
    row_num <= 3; -- Example: Get the top 3 sales for each value of column1 based on column2 ordering.
```


This query does the following:

1. **Filters the data:**  The `WHERE column1 > 100` clause filters the `sales_data` table based on the specified condition.
2. **Applies a CASE WHEN expression:** The `CASE` statement categorizes countries into regions.  It's important to include an `ELSE` clause to handle any countries not explicitly listed. This helps avoid unexpected NULL values.
3. **Uses a Window Function:** `ROW_NUMBER() OVER (PARTITION BY column1 ORDER BY column2)` assigns a unique rank to each row within a partition defined by `column1`, ordered by `column2`. This is useful for tasks like finding top N within a group.
4. **Uses a CTE (Common Table Expression):** The `WITH RankedSales AS (...)` clause defines a CTE, which makes the query more readable and modular.  It creates a temporary named result set that can be referenced later.
5. **Filters the ranked data:**  The final `SELECT` statement queries the CTE `RankedSales` and filters the results based on the row number calculated by the window function.  In this example, it retrieves only the top 3 rows (based on `column2` ordering) within each `column1` partition.

This example filters for `row_num <= 3`. You can adjust this filter or add other filters as needed based on your specific requirements. You can also aggregate data within the regions created using the `CASE WHEN`, providing summarized information.  For instance, you could calculate the total sales per region.
==================================================
-- Query 2:
```sql
SELECT
    cd.column1,
    cd.column4,
    cd.column5,
    SUM(od.sales) AS total_sales,
    COUNT(DISTINCT cd.customer_id) AS unique_customers
FROM
    customer_data cd
INNER JOIN
    order_data od ON cd.customer_id = od.customer_id  -- Assuming a related table 'order_data' with 'customer_id' and 'sales'
GROUP BY
    cd.column1, cd.column4, cd.column5
HAVING
    COUNT(DISTINCT cd.customer_id) > 10  -- Example HAVING clause to filter groups
ORDER BY
    total_sales DESC
LIMIT 50;


```


This query demonstrates several advanced SQL concepts:

* **Joins:** It uses an `INNER JOIN` to combine data from `customer_data` and a hypothetical `order_data` table, linking them on `customer_id`.  This allows us to calculate sales aggregated by customer attributes.
* **Aggregation:** It uses `SUM(sales)` to calculate total sales and `COUNT(DISTINCT customer_id)` to count the number of unique customers within each group.  `DISTINCT` is crucial to avoid overcounting customers if they have multiple orders.
* **Grouping:**  It groups the results by `column1`, `column4`, and `column5`, enabling aggregation at the desired level of detail.
* **HAVING Clause:** It includes a `HAVING` clause to filter the groups *after* aggregation.  In this example, it only includes groups with more than 10 unique customers.
* **Ordering:** It orders the results by `total_sales` in descending order (`DESC`), showing the highest sales groups first.
* **Limiting:** It uses `LIMIT 50` to restrict the output to the top 50 rows, which is useful for managing large result sets.



**Important Considerations:**

* **`order_data` Table:**  This query assumes the existence of an `order_data` table.  You'll need to replace `order_data` and adjust the join condition if your sales data is in a different table or structured differently.
* **Column Selection:**  The query selects `column1`, `column4`, and `column5`. Choose the columns relevant to your specific analysis.
* **HAVING Clause Condition:** The `HAVING` clause condition (`COUNT(DISTINCT cd.customer_id) > 10`) is an example.  Adjust it based on your filtering needs.


This improved query provides a more realistic and useful example of advanced SQL techniques.  Remember to adapt it to your particular data and requirements.
==================================================
