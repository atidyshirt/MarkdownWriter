class MarkdownWriter:
    """Write markdown output to a specified file

    Param: file: path to file to write output to
    """
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
    def header1(self, str):
        """ First level header """
        self.open_file.writelines(f"# {str}\n")

    @write_to_file
    def header2(self, str):
        """ Second level header """
        self.open_file.writelines(f"## {str}\n")

    @write_to_file
    def header3(self, str):
        """ Third level header """
        self.open_file.writelines(f"### {str}\n")

    @write_to_file
    def bold(self, str):
        """ Bold text with newline """
        if str[-1] == " ":
            str = str[:-1]
        if str[0] == " ":
            str = str[0:]
        self.open_file.writelines(f"**{str}**\n")

    @write_to_file
    def bold_inline(self, str):
        """ Inline bold text """
        if str[-1] == " ":
            str = str[:-1]
        if str[0] == " ":
            str = str[0:]
        self.open_file.writelines(f"**{str}**")

    @write_to_file
    def italic(self, str):
        """ italic text """
        if str[-1] == " ":
            str = str[:-1]
        if str[0] == " ":
            str = str[0:]
        self.open_file.writelines(f"*{str}*\n")

    @write_to_file
    def italic_inline(self, str):
        """ Inline italics """
        if str[-1] == " ":
            str = str[:-1]
        if str[0] == " ":
            str = str[0:]
        self.open_file.writelines(f"*{str}*")

    @write_to_file
    def math(self, str):
        """ Latex maths mode """
        self.open_file.writelines(f"$$ {str} $$\n")

    @write_to_file
    def math_inline(self, str):
        """ Latex maths mode inline text """
        if str[-1] == " ":
            str = str[:-1]
        if str[0] == " ":
            str = str[0:]
        self.open_file.writelines(f"${str}$")

    def clear(self):
        self.open_file = open(self.output_file, "w")
        self.open_file.write("")
        self.open_file.close()
