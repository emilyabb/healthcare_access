file_path_csv = "/Volumes/bronze_dev/ruca/ruca_raw/RUCA-codes-2020-tract.csv"

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(file_path_csv)

display(df)

df.write.format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("bronze_dev.ruca.ruca_census_tract")