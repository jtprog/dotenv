# encoding=UTF-8
# Source from https://github.com/jtprog/ndenv

__version__ = '0.0.7'


class NDenv(dict):
    """
    Class NDenv for manage environment
    """
    def __init__(self, file_path):
        self.file_path = file_path
        super(NDenv, self).__init__(**self.__create_dict())

    def __create_dict(self):
        with open(self.file_path, 'r') as ndenv:
            variables = {}
            for line in ndenv.readlines():
                variables.update(self.__parse_line(line))
            return variables

    def __parse_line(self, line):
        if line.lstrip().startswith('#'):
            # discard and return nothing
            return {}
        if line.lstrip():
            # find the second occurence of a quote mark:
            quote_delimit = max(line.find('\'', line.find('\'') + 1),
                                line.find('"', line.rfind('"')) + 1)
            # find first comment mark after second quote mark
            comment_delimit = line.find('#', quote_delimit)
            line = line[:comment_delimit]
            key, value = map(lambda x: x.strip().strip('\'').strip('"'),
                             line.split('=', 1))
            return {key: value}
        else:
            return {}

    def __persist(self):
        with open(self.file_path, 'w') as ndenv:
            for key, value in self.items():
                ndenv.write("%s=%s\n" % (key, value))

    def __setitem__(self, key, value):
        super(NDenv, self).__setitem__(key, value)
        self.__persist()

    def __delitem__(self, key):
        super(NDenv, self).__delitem__(key)
        self.__persist()


def set_variable(file_path, key, value):
    """Set environment variable"""
    ndenv = NDenv(file_path)
    ndenv[key] = value


def get_variable(file_path, key):
    """Get single environment variable"""
    ndenv = NDenv(file_path)
    return ndenv[key]


def get_variables(file_path):
    """Get all environment variable"""
    return NDenv(file_path)

