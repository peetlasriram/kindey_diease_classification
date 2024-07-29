import logging
import os
import sys

logg_dtr="[%(asctime)s - %(levelname)s - %(module)s - %(message)s]"

log_dir="logs"

logg_filepath=os.path.join(logg_dtr,"runnings.log")
os.makedirs(logg_dtr, exist_ok=True)


logging.basicConfig(
    level=logging.INFO, 
    format=logg_dtr,
    handlers=[
        logging.FileHandler(logg_filepath),
        logging.StreamHandler(sys.stdout)
    ]
    )

logger=logging.getLogger("cnnclassierlog")