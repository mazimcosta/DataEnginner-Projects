
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent
DATA_DIR=BASE_DIR/'data'
INPUT_DIR=DATA_DIR/'input'
OUTPUT_DIR=DATA_DIR/'output'
LOG_FILE=BASE_DIR/'logs'/'pipeline.log'
ENV_FILE=BASE_DIR/'config'/'.env'
