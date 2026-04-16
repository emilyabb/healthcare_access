import importlib
import utils.helpers

file_path_csv = "/Volumes/bronze_dev/seeds/raw/nucc_taxonomy_251.csv"

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(file_path_csv)

df_clean_columns = utils.helpers.prep_bronze_df(df)

df_clean_columns.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze_dev.seeds.nucc_provider_taxonomy_codes")