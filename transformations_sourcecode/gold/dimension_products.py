import dlt

# Create empty string table (to create slow chaning dimension)
dlt.create_streaming_table(
    name = "dimension_products"
)

#Auto CDC Flow
dlt.create_auto_cdc_flow(
        target = "dimension_products",
        source = "products_enr_view",
        keys = ["product_id"],
        sequence_by = "last_updated",
        ignore_null_updates = False,
        apply_as_deletes = None,
        apply_as_truncates = None,
        column_list = None,
        except_column_list = None,
        stored_as_scd_type = 2, # slowing changing dimension 2
        track_history_column_list = None,
        track_history_except_column_list = None
)