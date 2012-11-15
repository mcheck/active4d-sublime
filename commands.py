import os
import os.path
import re
import shutil
import sublime
import sublime_plugin

LANGUAGE_RE = re.compile(ur'^.+/Active4D.*\.tmLanguage')


def usingActive4DSyntax(view):
    return LANGUAGE_RE.match(view.settings().get("syntax")) is not None


class NewCircuitCommand(sublime_plugin.TextCommand):
    def is_enabled(self):
        return usingActive4DSyntax(self.view)

    def run(self, edit):
        path = os.path.dirname(self.view.file_name())

        if path:
            self.view.window().show_input_panel('Circuit name:', '', self.make_circuit, None, None)

    def make_circuit(self, circuitName):
        if circuitName:
            circuitPath = os.path.join(os.path.dirname(os.path.abspath(self.view.file_name())), circuitName)

            if not os.path.exists(circuitPath):
                src = os.path.join(sublime.packages_path(), 'Active4D', 'Support', 'circuit')
                shutil.copytree(src, circuitPath)
            else:
                sublime.message_dialog('A file or directory already exists at %s' % circuitPath)


class BuildQueryCommand(sublime_plugin.TextCommand):
    QUERY_RE = re.compile(ur'^(\s*)(query(?: selection)?\s*)\(\[([^\]]+)\]', re.IGNORECASE)
    ASTERISK_RE = re.compile(ur'(^.*);\s*\*\s*\)\s*(`.*|//.*|.*)$')
    ADD_ASTERISK_RE = re.compile(ur'(^.*)(\s*\))(\s*(`.*|//.*|.*)$)')

    def is_enabled(self):
        return usingActive4DSyntax(self.view)

    def run(self, edit):
        line_region = self.view.line(self.view.sel()[0])
        line = self.view.substr(line_region)

        # See if the current line is a query. If it is, process it.
        m = self.QUERY_RE.match(line)

        if m:
            ws = m.group(1)
            command = m.group(2)
            table = m.group(3)

            # See if ;* has been added to the end of the query. If not, add it.
            if not self.ASTERISK_RE.match(line):
                m = self.ADD_ASTERISK_RE.match(line)
                line = '%s; *%s%s\n' % (m.group(1), m.group(2), m.group(3))
            else:
                line = line + '\n'

            edit = self.view.begin_edit()
            self.view.replace(edit, line_region, line)
            self.view.end_edit(edit)
            self.view.run_command('insert_snippet', {'contents': '%s%s([${1:%s}]; ${2:conjunction}; [$1]${3:field})' % (ws, command, table)})
