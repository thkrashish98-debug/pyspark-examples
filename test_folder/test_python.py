from pyspark.sql.functions import col, max

df = spark.read.csv("/path_to_file")
df.show(5,0)

df1 = df.groupBy(col("country")).agg(max(col("salary")))

df1.show(5,0)
df1.write.csv("destination_path")