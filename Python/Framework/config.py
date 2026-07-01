# ============================================================
# HELIX DATABASE CONFIGURATION
# ============================================================

DB_CONFIG = {

    "host": "localhost",

    "user": "root",

    "password": "Ranjith@123",

    "database": "AstraNova_OLTP"

}

# ============================================================
# DATASET PATHS
# ============================================================

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RAW_DATA = PROJECT_ROOT / "Dataset" / "Raw"

PROCESSED_DATA = PROJECT_ROOT / "Dataset" / "Processed"

STAGING_DATA = PROJECT_ROOT / "Dataset" / "Staging"

WAREHOUSE_DATA = PROJECT_ROOT / "Dataset" / "Warehouse"