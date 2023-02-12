from logging import getLogger, Logger
import os
import os.path


default_logger = getLogger(__name__)


# pylint: disable=too-few-public-methods
class LaunchApkTool:
    """
    Extract the (decrypted) AndroidManifest.xml, the resources and generate the disassembled smali files.
    """

    __APKTOOL_PATH = "apktool.exe"

    def __init__(self, logger: Logger = default_logger):
        self.logger = logger
        self.apktool = LaunchApkTool.__APKTOOL_PATH
        self.logger.debug("apktool path: %s", self.apktool)

    def execute(self, input_filepath: str, output_directory: str):
        self.logger.info("Executing apktool...")
        self.logger.info("Creating %s/smali/...", output_directory)
        self.logger.info("Creating %s/AndroidManifest.xml...", output_directory)
        self.logger.info("Creating %s/res/...", output_directory)
        self.logger.info("Creating %s/assets/...", output_directory)

        command = "{} -q decode -f -o {} {}".format(
            self.apktool,
            output_directory,
            input_filepath
        )
        self.logger.debug("apktool command: `%s`", command)
        return os.system(command)
