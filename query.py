import os
import google.generativeai as genai
import dotenv

dotenv.load_dotenv()

# Configure the Generative AI client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")


def build_advanced_query(metadata):
    """
    Builds a query dynamically using metadata.
    Args:
        metadata (dict): A dictionary of metadata key-value pairs.
    Returns:
        str: Constructed query string for the Gemini API.
    """
    query = "Generate an advanced SQL query using the following metadata:\n"
    query += f"- Columns: {metadata.get('Columns', 'ALL')}\n"
    query += f"- Table: {metadata.get('Table', 'UNKNOWN')}\n"

    # Add condition if provided
    condition = metadata.get("Condition")
    if condition:
        query += f"- Condition: {condition}\n"

    # Add CASE WHEN if specified
    if "CaseWhen" in metadata:
        query += f"- Case When: {metadata['CaseWhen']}\n"

    # Add Window Function if specified
    if "WindowFunction" in metadata:
        query += f"- Window Function: {metadata['WindowFunction']}\n"

    # Add Subquery if specified
    if "Subquery" in metadata:
        query += f"- Subquery: {metadata['Subquery']}\n"

    # Add Aggregation Functions if specified
    if "Aggregation" in metadata:
        query += f"- Aggregation: {metadata['Aggregation']}\n"

    # Add Join Type if specified
    if "JoinType" in metadata:
        query += f"- Join Type: {metadata['JoinType']}\n"

    # Add advanced options
    for key in ["Join", "GroupBy", "Having", "OrderBy"]:
        if key in metadata:
            query += f"- {key}: {metadata[key]}\n"

    return query


def main():
    print("🔍 Advanced Query Builder with SQL Features")

    try:
        # Collect metadata from the user
        metadata = {}
        print("\nEnter metadata in the following order:")
        print("1. Columns (e.g., column1, column2, ...)")
        print("2. Table (e.g., table_name)")
        print("3. Condition (optional, e.g., column1 > 100)")
        print("4. Case When (optional, e.g., country_name to numbers)")
        print("5. Window Function (optional, e.g., ROW_NUMBER() OVER(PARTITION BY column1 ORDER BY column2))")
        print("6. Subquery (optional, e.g., SELECT * FROM table2 WHERE column2 > 50)")
        print("7. Aggregation (optional, e.g., SUM(sales), COUNT(column1))")
        print("8. Join Type (optional, e.g., INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN)")
        print("9. Advanced options: Join, GroupBy, Having, OrderBy")
        print("Type 'done' when finished.")

        # Collect Columns
        metadata["Columns"] = input("Columns: ").strip()

        # Collect Table
        metadata["Table"] = input("Table: ").strip()

        # Collect Condition
        condition = input("Condition (optional): ").strip()
        if condition:
            metadata["Condition"] = condition

        # Collect CASE WHEN
        case_when = input("Case When (optional): ").strip()
        if case_when:
            metadata["CaseWhen"] = case_when

        # Collect Window Function
        window_function = input("Window Function (optional): ").strip()
        if window_function:
            metadata["WindowFunction"] = window_function

        # Collect Subquery
        subquery = input("Subquery (optional): ").strip()
        if subquery:
            metadata["Subquery"] = subquery

        # Collect Aggregation Functions
        aggregation = input("Aggregation (optional): ").strip()
        if aggregation:
            metadata["Aggregation"] = aggregation

        # Collect Join Type
        join_type = input("Join Type (optional): ").strip()
        if join_type:
            metadata["JoinType"] = join_type

        # Collect advanced options
        for key in ["Join", "GroupBy", "Having", "OrderBy"]:
            value = input(f"{key} (optional): ").strip()
            if value:
                metadata[key] = value

        # Ensure mandatory fields are provided
        if not metadata.get("Columns") or not metadata.get("Table"):
            print("Columns and Table are required. Exiting...")
            return

        # Build the query
        query = build_advanced_query(metadata)
        print("\nGenerated Query Prompt:\n", query)

        # Generate a response using the Gemini API
        response = model.generate_content([query])
        print("\nGemini API Response:\n", response.text)

    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
