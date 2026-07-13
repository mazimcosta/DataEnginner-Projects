
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent
DATA_DIR=BASE_DIR/'data'
INPUT_DIR=DATA_DIR/'input'
OUTPUT_DIR=DATA_DIR/'output'
ENV_FILE=BASE_DIR/'config'/'.env'
LOG_FILE=BASE_DIR/'logs'/'pipeline.log'
SQL_DIR=BASE_DIR/'sql'
