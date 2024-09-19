from prefect import flow, tags
from prefect.logging import get_run_logger
from pathlib import Path
from prefect import flow


@flow
def hello(name: str = "Marvin"):
    logger = get_run_logger()
    logger.info(f"Hello, {name}!")
    
if __name__ == "__main__":
    with tags("local"):
        hello()