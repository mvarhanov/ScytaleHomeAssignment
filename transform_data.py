from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, split, count
from pyspark.sql.window import Window


def transform_data(file_path: str) -> None:
    """
    Transforms JSON data, extracts necessary columns, calculates PR metrics,
    and saves the result as Parquet.
    """

    # Initialize SparkSession
    spark = SparkSession.builder.appName("JSON to Parquet with PySpark").getOrCreate()

    # Load JSON files into a DataFrame
    df = spark.read.json(file_path)

    # Extract Organization Name from full_name column
    df = df.withColumn("Organization Name", split(col("full_name"), '/').getItem(1))

    # Define window specification for partitioning and ordering
    window_spec = Window.partitionBy("id").orderBy("id")

    # Count PRs per id
    df = df.withColumn("num_prs", count("id").over(window_spec))

    # Count merged PRs per id
    df = df.withColumn("num_prs_merged", count(when(col("is_merged"), col("id"))).over(window_spec))

    # Extract repository owner as repository_owner
    df = df.withColumn("repository_owner", col("owner_login"))

    # Check if repository name contains "scytale"
    df = df.withColumn("num", col("name").like("%scytale%"))

    # Determine if compliant based on PR counts and repository owner
    df = df.withColumn("is_compliant",
                       (col("num_prs") == col("num_prs_merged")) & (col("repository_owner").like("%scytale%")))

    # Select relevant columns for final DataFrame
    df = df.select(
        "Organization Name",
        col("id").alias("repository_id"),
        col("name").alias("repository_name"),
        "repository_owner",
        "num_prs",
        "num_prs_merged",
        col("updated_at").alias("merged_at"),
        "is_compliant",
    )

    # Save the transformed DataFrame to Parquet
    df.write.mode("overwrite").parquet("parquet_data")

    # Stop the SparkSession
    spark.stop()
