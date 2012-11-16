Active4D-Sublime
================

Active4D-Sublime is a Sublime Text 2 package which provides syntax highlighting, snippets and convenience commands for use with Active4D.

## Syntax Highlighting
Full syntax highlighting is provided for the following file types:

* **Embedded scripts (.a4d, .a4p)** – Context-aware syntax highlighting is provided. Anything not within <% %> script tags is highlighted as if it were an HTML file. \<script\> and \<style\> blocks within the file are highlighted using Javascript and CSS modes respectively. Symbol matching is provided for methods defined inline.

* **Libraries (.a4l)** – In addition to syntax highlighting, symbol matching for methods is provided.

* **Config files (.ini)** – In addition to syntax highlighting, in Active4D.ini symbol matching is provided for the settings.

## Snippets
Numerous snippets are provided for control structures, commands, and fusedocs. The best way to explore the snippets is by showing the snippet list in ST2.

## Commands
Several commands are available via keyboard equivalents:

* **Insert = block** (super+shift+=) – Inserts the snippet <%= %>.

* **Build query** (super+alt+b) – If the beginning of the current selection is on a query/query selection command, a * is added if necessary to the query command and a snippet is inserted on the next line, with the table used in the previous line filled in as the default.

* **New circuit** – Available from the command palette when an Active4D file is being edited, this command prompts for a circuit name and creates a new circuit in the directory of the currently edited file. The new circuit contains a skeleton fbx_switch.a4d, fbx_layouts.a4d, fbx_settings.a4d, and fbx_switch.a4d.

* **Open include** (super+k, super+i) – If the cursor is within a string, the string is joined to the path of the current file's directory, and if the resulting path is a file, the file is opened. Typically this is used to open the target of an **include** statement.
