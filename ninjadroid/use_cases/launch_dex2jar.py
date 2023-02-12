from logging import getLogger, Logger
import os
import os.path


default_logger = getLogger(__name__)


# pylint: disable=too-few-public-methods
class LaunchDex2Jar:
    """
    Generate a JAR file from the DEX one.
    """
    __DEX2JAR_PATH = "dex2jar.exe"

    def __init__(self, logger: Logger = default_logger):
        self.logger = logger
        self.dex2jar = LaunchDex2Jar.__DEX2JAR_PATH
        self.logger.debug("dex2jar path: %s", self.dex2jar)

    def execute(self, input_filepath: str, input_filename: str, output_directory: str):
        jarfile = input_filename + ".jar"
        self.logger.info("Executing dex2jar...")
        self.logger.info("Creating %s/%s...", output_directory, jarfile)

        command = "{} -f {} -o {}/{}".format(
            self.dex2jar,
            input_filepath,
            output_directory,
            jarfile
        )
        self.logger.debug("dex2jar command: `%s`", command)
        return os.system(command)
