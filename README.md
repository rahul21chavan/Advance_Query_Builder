# Advance_Query_Builder
Advanced SQL Query Builder with Gemini API
Overview
This project builds a dynamic SQL query generator using Google's Gemini API. It allows users to create advanced SQL queries by inputting metadata such as table columns, join types, conditions, window functions, subqueries, and aggregation functions. The tool can generate complex SQL queries that include advanced SQL features like CASE WHEN, JOINs, GROUP BY, HAVING, and Window Functions.

By leveraging the Gemini API, the program assists users in generating optimized SQL queries that suit specific use cases, particularly for data analysis, reporting, and ETL tasks.

Features
1. Dynamic Query Building
The tool collects metadata (like columns, tables, conditions, etc.) from users and generates an SQL query using this input. It supports multiple advanced SQL features, including:

Columns: Define which columns you want to query from a given table.
Table: The table from which the columns should be selected.
Condition: Optional conditions (e.g., filters or where clauses).
CASE WHEN: Generate conditional SQL logic for transforming values (e.g., converting country names to numeric codes).
Window Functions: Apply window functions like ROW_NUMBER(), RANK(), and PARTITION BY for advanced row-level calculations.
Subqueries: Insert subqueries into the query for filtering or complex logic.
Aggregation: Use aggregation functions like COUNT(), SUM(), AVG(), etc.
Join Types: Specify different join types such as INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN to combine data from multiple tables.
Advanced SQL Options: Additional support for GROUP BY, HAVING, and ORDER BY clauses.

Inputs
Columns: Specify the columns you want to query (e.g., column1, column2, COUNT(sales)).
Table: The name of the table from which the query will retrieve data (e.g., sales_data).
Condition (optional): Filter rows based on certain conditions (e.g., region = 'North America').
CASE WHEN (optional): Define conditional logic to transform or categorize data (e.g., country_name = 'USA' THEN 1).
Window Function (optional): Use window functions such as ROW_NUMBER() to perform calculations across rows (e.g., ROW_NUMBER() OVER(PARTITION BY region ORDER BY sales DESC)).
Subquery (optional): Include subqueries for advanced filtering or complex logic (e.g., SELECT * FROM sales_data WHERE sales > 500).
Aggregation (optional): Aggregate data using functions like COUNT(), SUM(), AVG(), etc. (e.g., COUNT(column1)).
Join Type (optional): Specify the type of join to use (e.g., INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN).
Advanced Options:
Join: Define the tables to join and the join condition.
Group By: Group the query results by one or more columns.
Having: Filter grouped results.
Order By: Specify the sorting order of the query results.

How It Works
User Inputs: The user is prompted to provide input for various SQL metadata, such as columns, tables, conditions, and advanced SQL features.
Query Generation: The tool builds a query string dynamically using the provided metadata and constructs a query prompt.
Query Processing with Gemini API: The query prompt is sent to the Gemini API, which processes it and returns an optimized SQL query.
SQL Query Output: The generated SQL query is displayed to the user, which can be executed on the desired database.

Integration with Google Gemini API: Uses Google’s generative AI model to create optimized SQL queries based on the provided metadata.
Metadata from JSON File: Load multiple sets of metadata from a JSON file, making it easy to work with large datasets.
Output to SQL File: Saves the generated SQL queries into a .sql file, with clear separation between each query.

Example Usage
Here is an example of how to use the tool:

1. Input
sql
Copy code
Columns: column1, column2, COUNT(sales)
Table: sales_data
Condition: region = 'North America'
Join Type: INNER JOIN
Case When: country_name = 'USA' THEN 1, country_name = 'India' THEN 2
Window Function: ROW_NUMBER() OVER(PARTITION BY region ORDER BY sales DESC)
Subquery: SELECT * FROM sales_data WHERE sales > 500
Aggregation: COUNT(column1)
GroupBy: column2
OrderBy: sales DESC
2. Generated Query Prompt
sql
Copy code
Generate an advanced SQL query using the following metadata:
- Columns: column1, column2, COUNT(sales)
- Table: sales_data
- Condition: region = 'North America'
- Join Type: INNER JOIN
- Case When: country_name = 'USA' THEN 1, country_name = 'India' THEN 2
- Window Function: ROW_NUMBER() OVER(PARTITION BY region ORDER BY sales DESC)
- Subquery: SELECT * FROM sales_data WHERE sales > 500
- Aggregation: COUNT(column1)
- Group By: column2
- Order By: sales DESC
3. Gemini API Response
sql
Copy code
SELECT 
    column1, 
    column2, 
    COUNT(sales),
    ROW_NUMBER() OVER(PARTITION BY region ORDER BY sales DESC) AS row_num,
    CASE 
        WHEN country_name = 'USA' THEN 1 
        WHEN country_name = 'India' THEN 2 
        ELSE 0 
    END AS country_code
FROM sales_data
INNER JOIN other_table
WHERE region = 'North America'
AND sales > 500
GROUP BY column2
ORDER BY sales DESC;
