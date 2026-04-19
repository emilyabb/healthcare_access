import re
from pyspark.sql.functions import col, lit
from collections import Counter


def clean_columns_bronze(df):
    """
    Minimal cleaning for bronze layer:
    - Trim whitespace
    - Replace spaces with underscores
    - Remove characters not supported in Databricks column names
    - Preserve original casing as much as possible
    """
    cleaned_cols = []
    
    for c in df.columns:
        new_col = c.strip()
        new_col = new_col.replace(" ", "_")
        
        # Remove problematic characters (keep letters, numbers, underscore)
        new_col = re.sub(r"[^\w]", "", new_col)
        
        cleaned_cols.append(new_col)
    
    return df.toDF(*cleaned_cols)


def clean_columns_silver(df):
    """
    Standardized cleaning for silver layer:
    - Lowercase
    - Convert to snake_case
    - Remove punctuation
    - Collapse multiple underscores
    """
    cleaned_cols = []
    
    def standardize_column_names_silver(col_name: str) -> str:
        # Step 1: insert underscore before capital letters (camelCase / PascalCase)
        col_name = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', col_name)
        
        # Step 2: split acronym boundaries (e.g., FIPSCode → FIPS_Code)
        col_name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', col_name)
        
        # Step 3: split letters and numbers (FIPS23 → FIPS_23)
        col_name = re.sub(r'([a-zA-Z])(\d)', r'\1_\2', col_name)
        
        # Step 4: normalize
        col_name = col_name.lower()
        col_name = re.sub(r"[^\w]", "_", col_name)   # replace non-alphanumeric with _
        col_name = re.sub(r"_+", "_", col_name)      # collapse multiple _
        col_name = col_name.strip("_")              # trim
        
        return col_name

    for c in df.columns:
        new_col = standardize_column_names_silver(c)
        cleaned_cols.append(new_col)
    
    return df.toDF(*cleaned_cols)

def prep_bronze_df(df):

    # Cast void type columns to string
        
    # Find all void columns
    void_columns = [field.name for field in df.schema.fields if str(field.dataType) == 'NullType()']
    print(f"Found {len(void_columns)} void columns: {void_columns}")

    # Cast void columns to string
    for col_name in void_columns:
        df = df.withColumn(col_name, col(col_name).cast("string"))


    columns = [c.strip() for c in df.columns]
    dups = [k for k, v in Counter(columns).items() if v > 1]
    print("Warning: Duplicate Columns: ", dups)

    
    return clean_columns_bronze(df)



def prep_silver_df(df):

    return clean_columns_silver(df)