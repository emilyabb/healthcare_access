import importlib
import utils.helpers

file_path_csv = "/Volumes/bronze_dev/economic_research_service/ers_raw/Poverty2023.csv"

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(file_path_csv)

df_prepped = utils.helpers.prep_bronze_df(df)

df_prepped.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze_dev.economic_research_service.county_poverty")