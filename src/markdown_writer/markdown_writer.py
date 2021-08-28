"""
File: markdown_writer.py
Author: https://github.com/atidyshirt
Version: < 1
"""

import os
from markdown_writer.utils import *

class MarkdownWriter:
    """Write markdown output to a specified file

    Param: file: path to file to write output to
    """
    def __init__(self, file: str) -> None:
        self.output_file = file

    def write_to_file(decorated_function):
        def file_open(self, *args, **kwargs):
            self.open_file = open(self.output_file, "a")
            decorated_function(self, *args, **kwargs)
            self.open_file.writelines("\n")
            self.open_file.close()
        return file_open

    @write_to_file
    def paragraph(self, string: str) -> None:
        """ Write paragraph to markdown """
        self.open_file.writelines(f"{string}\n")

    @write_to_file
    def header1(self, string: str) -> None:
        """ First level header """
        self.open_file.writelines(f"# {string}\n")

    @write_to_file
    def header2(self, string: str) -> None:
        """ Second level header """
        self.open_file.writelines(f"## {string}\n")

    @write_to_file
    def header3(self, string: str) -> None:
        """ Third level header """
        self.open_file.writelines(f"### {string}\n")

    @write_to_file
    def header4(self, string: str) -> None:
        """ Fourth level header """
        self.open_file.writelines(f"#### {string}\n")

    @write_to_file
    def bold(self, string: str, newline=False) -> None:
        """ Bold text with newline

        Signature: italic(str, newline)
        """
        string = strip_whitespace(string)
        if newline:
            self.open_file.writelines(f"**{string}**\n")
        else:
            self.open_file.writelines(f"**{string}**")

    @write_to_file
    def italic(self, string: str, newline=False) -> None:
        """ italic text

        Signature: italic(str, newline)
        """
        string = strip_whitespace(string)
        if newline:
            self.open_file.writelines(f"*{string}*\n")
        else:
            self.open_file.writelines(f"*{string}*")

    @write_to_file
    def math(self, string: str, newline=False) -> None:
        """ Latex maths mode inline text """
        string = strip_whitespace(string)
        if newline:
            self.open_file.writelines(f"$$ {string} $$\n")
        else:
            self.open_file.writelines(f"${string}$")

    @write_to_file
    def codeblock(self, block: str, language="") -> None:
        """ Writes a code block to markdown file

        param: `language` defults to none
        """
        self.open_file.writelines(f"```\n{block}\n```\n")

    @write_to_file
    def list(self, dict_list: dict) -> None:
        """ Builds a list of bullet points from a python dictionary """
        result = ""
        for key, value in dict_list.items():
            result += f"* {key}\n"
            for ke, val in value.items():
                result += f"\t* {ke}:\n"
                for item in val:
                    result += f"\t\t* {item}\n"
        self.open_file.writelines(result)

    try:
        import matplotlib.pyplot as plt
        @write_to_file
        def plot(self, figure, file_name: str, description: str) -> None:
            """ Writing plots from matplotlib to markdown (image)

            this will only be avalible if matplotlib is found in PYTHONPATH
            """
            file_location = "".join(self.output_file.split("/")[:-1])
            if not os.path.isdir(f"{file_location}/resources"):
                os.system(f"mkdir {file_location}/resources")
            figure.savefig(f"{file_location}/resources/{file_name}", bbox_inches='tight')
            self.open_file.write(f"![{description}]({file_location}/resources/{file_name})\n")
    except ImportError:
        pass

    def clear_file(self) -> None:
        self.open_file = open(self.output_file, "w")
        self.open_file.write("")
        self.open_file.close()
