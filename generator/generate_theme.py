#!/usr/bin/python

from pathlib import Path

import argparse

# Parse arguments.
parser = argparse.ArgumentParser(
    description='Generates the theme json from the template.')

parser.add_argument('--name', '-n', required=True, type=str,
                    help='Name of the generated theme.')
parser.add_argument('--accent', required=True,
                    type=str, help='Accent color.')
parser.add_argument('--number', required=True,
                    type=str, help='Number color.')

args = parser.parse_args()

# Setup constants.
outputName = args.name
parentPath = Path(__file__).parent.absolute()
templatePath = Path(parentPath, 'template_theme.json')
outputPath = Path(parentPath.parent, 'themes', f'{outputName}_theme.json')

colors = {
    "background": "#121212",
    "foreground": "#f7f1ff",
    "surface": "#121212",
    "surfaceBorder": "#181818",
    "inactiveForeground": "#525252",
    "activeForeground": "#979797",
    "highlight": "#212121",
    "divider": "#212121",
    "hint": "#6b6b6b",
    "selected": "#6b6b6b",  # Highlighted file names, paths, punctuaction.
    "comment": "#525252",
    "punctuation": "#525252",

    "red": "#525252",
    "orange": "#525252",
    "yellow": args.accent,
    "green": "#f7f1ff",
    "blue": args.accent,
    "purple": args.number,
}

theme = {
    **colors,

    'name': outputName,
    'author': 'Volskaya',
    'uuid': '0',

    'stringColor': colors['yellow'],
    'objectColor': colors['blue'],
    'irrelevantObjectColor': colors['comment'],
    'numberColor': colors['purple'],
    'variableColor': colors['foreground'],
    'argumentColor': colors['foreground'],
    'operatorColor': colors['red'],
    'methodColor': colors['green'],
    'languageConstantColor': colors['orange'],
    'lineHighlightColor': '#181818',

    'indentGuideColor': colors['divider'],
    'whitespaceColor': colors['divider'],
    'matchingBracketColor': colors['yellow'],

    'argumentStyle': 'italic',
    'languageConstantStyle': 'normal',
}

# Generate theme.
print(f'Generating a theme - "{outputPath.name}"')

template = open(templatePath, 'r')
output = open(outputPath, 'w')
i = 0

with template as line:
    for line in template:
        i += 1
        start, end = line.find('{{'), line.find('}}')
        outputLine = line

        if start >= 0 and end >= 0:
            key = line[start+2:end]
            themeValue = theme[key]

            if themeValue:
                outputLine = line.replace('{{%s}}' % key, theme[key])

        output.write(outputLine)

template.close()
output.close()

print(f'Completed {i} lines')
