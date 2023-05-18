import logging

logging.basicConfig(
    level=logging.DEBUG,  # Everything will be logged
    format="%(asctime)s %(levelname)s %(message)s",
)

logger = logging.getLogger(__name__)
