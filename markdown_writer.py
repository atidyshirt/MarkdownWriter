import os

class MarkdownWriter:
    """Write markdown output to a specified file

    Param: file: path to file to write output to
    """
    # FIXME: function signatures changes to show typing
    def __init__(self, file):
        self.output_file = file

    def write_to_file(decorated_function):
        def file_open(self, *args, **kwargs):
            self.open_file = open(self.output_file, "a")
            decorated_function(self, *args, **kwargs)
            self.open_file.writelines("\n")
            self.open_file.close()
        return file_open

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
        if string[-1] == " ":
            string = string[:-1]
        if string[0] == " ":
            string = string[0:]
        if newline:
            self.open_file.writelines(f"**{string}**\n")
        else:
            self.open_file.writelines(f"**{string}**")

    @write_to_file
    def italic(self, string: str, newline=False) -> None:
        """ italic text

        Signature: italic(str, newline)
        """
        if string[-1] == " ":
            string = string[:-1]
        if string[0] == " ":
            string = string[0:]
        if newline:
            self.open_file.writelines(f"*{string}*\n")
        else:
            self.open_file.writelines(f"*{string}*\n")

    @write_to_file
    def math(self, string: str, newline=False) -> None:
        """ Latex maths mode inline text """
        if string[-1] == " ":
            string = string[:-1]
        if string[0] == " ":
            string = string[0:]
        if newline:
            self.open_file.writelines(f"$$ {string} $$\n")
        else:
            self.open_file.writelines(f"${string}$")

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
            self.open_file.write(f"![{description}]({file_location}/resources/{file_name})")
    except ImportError:
        pass

    def clear_file(self) -> None:
        self.open_file = open(self.output_file, "w")
        self.open_file.write("")
        self.open_file.close()
