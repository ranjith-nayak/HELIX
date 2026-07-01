from etl_logger import ETLLogger

logger = ETLLogger("Customer ETL")

logger.success(
    records_read=100,
    records_loaded=100
)