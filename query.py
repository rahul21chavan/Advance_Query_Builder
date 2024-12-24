import os
import google.generativeai as genai
import dotenv
import json

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


def load_metadata_from_file(file_path):
    """
    Load metadata from a JSON file.
    Args:
        file_path (str): Path to the metadata file.
    Returns:
        list: A list of dictionaries containing metadata.
    """
    try:
        with open(file_path, 'r') as file:
            metadata_list = json.load(file)
        return metadata_list
    except Exception as e:
        print(f"Error reading metadata file: {str(e)}")
        return []


def save_sql_queries_to_file(sql_queries, output_file_path):
    """
    Saves the generated SQL queries to a .sql file.
    Args:
        sql_queries (list): A list of generated SQL queries.
        output_file_path (str): Path to the output .sql file.
    """
    try:
        with open(output_file_path, 'w') as file:
            for idx, query in enumerate(sql_queries, start=1):
                file.write(f"-- Query {idx}:\n")
                file.write(query)
                file.write("\n" + "=" * 50 + "\n")
        print(f"SQL queries have been saved to {output_file_path}")
    except Exception as e:
        print(f"Error saving SQL queries to file: {str(e)}")


def main():
    print("🔍 Advanced Query Builder with SQL Features")

    try:
        # Ask the user to provide the path to the metadata file
        metadata_file_path = input("Please enter the path to your metadata JSON file: ").strip()

        # Check if the file exists
        if not os.path.isfile(metadata_file_path):
            print("Invalid file path. Please try again.")
            return

        # Load metadata from the provided file
        metadata_list = load_metadata_from_file(metadata_file_path)

        # Ensure at least one metadata set is provided
        if not metadata_list:
            print("No metadata found in the file. Exiting...")
            return

        # List to store the generated SQL queries
        sql_queries = []

        # Loop over the collected metadata and generate SQL queries
        for idx, metadata in enumerate(metadata_list, start=1):
            print(f"\nGenerating query for metadata set {idx}...")
            # Build the query
            query = build_advanced_query(metadata)
            print("\nGenerated Query Prompt:\n", query)

            # Generate a response using the Gemini API
            response = model.generate_content([query])
            sql_queries.append(response.text)

        # Save the generated SQL queries to a .sql file
        output_file_path = metadata_file_path.replace(".json", "_queries.sql")
        save_sql_queries_to_file(sql_queries, output_file_path)

    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
