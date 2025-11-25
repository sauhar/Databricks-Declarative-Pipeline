import dlt
from pyspark.sql.functions import *


# Creating materialized business view
@dlt.table(
    name = "business_Sales"
)
def business_Sales():
    df_fact = spark.read.table("fact_sales")
    df_dimcust = spark.read.table("dimension_customers")
    df_dimprod = spark.read.table("dimension_products")
    df_join = df_fact.join(df_dimcust, df_fact.customer_id == df_dimcust.customer_id,"inner").join(df_dimprod, df_fact.product_id == df_dimprod.product_id,"inner")

    df_prun = df_join.select("region","category","total_amount")

    df_agg = df_prun.groupBy("region", "category").agg(sum("total_amount").alias("total_sales"))

    return df_agg