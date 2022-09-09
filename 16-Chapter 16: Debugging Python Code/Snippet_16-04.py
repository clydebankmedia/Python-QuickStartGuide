# Import the logging module
import logging

# Configure the module
logging.basicConfig(
    filename="test.log",
    encoding="utf-8",
    level=logging.WARNING)

# Log several messages
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error.")
logging.critical("Something major went wrong!")
