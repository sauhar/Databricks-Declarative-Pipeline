# import dlt


# # Creating and End-To-End Basic Pipeline

# #Staging Area

# @dlt.table(
#     name = 'staging_orders'
# )
# def staging_orders():
#     df = spark.readStream.table('dltsauhar.source.orders')
#     return df


# #Creating Transformed Area
# from pyspark.sql.functions import *

# @dlt.view(
#     name = 'transformed_orders'
# )
# def transformed_orders():
#     df = spark.readStream.table("staging_orders")
#     df = df.withColumn(
#     "order_status",
#     regexp_replace("order_status", r"^complete$", "completed")
# )
#     return df


# # Creating Aggregated Area
# @dlt.table(
#     name = 'aggregated_orders'
# )
# def aggregated_orders():
#     df = spark.readStream.table('transformed_orders')
#     df = df.groupBy('order_status').count()
#     return df
