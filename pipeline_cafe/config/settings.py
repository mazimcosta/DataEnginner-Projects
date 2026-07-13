from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent
DATA_DIR=BASE_DIR/'data'
RAW_DIR=DATA_DIR/'raw'
PROCESSED_DIR=DATA_DIR/'processed'
LOG_FILE=BASE_DIR/'logs'/'pipeline.log'
ENV_FILE=BASE_DIR/'config'/'.env'
SQL_DIR=BASE_DIR/'sql'
