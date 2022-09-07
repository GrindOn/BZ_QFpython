import logging

logging.basicConfig(filename='log.txt', filemode='a', level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.debug("Do something")
logger.info("Start print log")
logger.warning("Something maybe fail.")
logger.error('error')
