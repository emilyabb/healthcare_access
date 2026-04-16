import importlib
import utils.helpers

importlib.reload(utils.helpers)

file_path_csv = "/Volumes/bronze_dev/cms/cms_raw/Hospital_General_Information.csv"

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(file_path_csv)

df_prepped = utils.helpers.prep_bronze_df(df)

df_prepped.write.format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("bronze_dev.cms.hospital_general_information")