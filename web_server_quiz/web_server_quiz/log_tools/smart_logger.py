import sys
import traceback
from datetime import datetime
from typing import Union


class Levels:
    def __init__(self):
        pass

    sys = 'sys'
    warning = 'warning'
    failure = 'failure'
    success = 'success'


class SmartLogger(object):
    def __init__(self, class_name: str, parameter: Union[str, None], emitter=None) -> None:
        self.class_name = class_name
        self.parameter = parameter
        self.emitter = emitter

        self._format_bold = '\033[1m'
        self._format_underline = '\033[4m'

        self._format_color_grey = '\033[90m'
        self._format_color_red = '\033[91m'
        self._format_color_green = '\033[92m'
        self._format_color_yellow = '\033[93m'
        self._format_color_azure = '\033[94m'
        self._format_color_pink = '\033[95m'
        self._format_color_teal = '\033[96m'
        self._format_color_black = '\033[97m'

        self._format_end = '\033[0m'

        pass

    def write(self, message: str, level: Levels = Levels.sys, log_traceback: bool = False) -> None:
        """
        Writes down logged line.
        :param message: Message it self.
        :param level: Level of logging.
        :param log_traceback: boolean flag, if set - traceback will be extracted and printed as well.
        :return: Nothing.
        """
        format_prefix = ''
        level_prefix = ''

        if level == Levels.sys:
            format_prefix += self._format_color_yellow
        elif level == Levels.warning:
            format_prefix += self._format_color_azure
            level_prefix = '[WARNING] '
        elif level == Levels.failure:
            format_prefix += self._format_color_red
            level_prefix = '[FAILURE] '
        elif level == Levels.success:
            format_prefix += self._format_color_green
            level_prefix = '[SUCCESS] '
        else:
            pass

        message = '%s [%s|%s] >>> %s' % (
            datetime.now().replace(microsecond=0), self.class_name, self.parameter, (level_prefix + message))

        if log_traceback is True:
            error_type, error_value, error_traceback = sys.exc_info()
            error_traceback = traceback.extract_tb(error_traceback)
            message += (' Error Value: %s; TraceBack: %s' % (error_value, error_traceback[len(error_traceback) - 1]))

        print(format_prefix + message + self._format_end)

        if self.emitter is not None:
            self.emitter.write(message)
