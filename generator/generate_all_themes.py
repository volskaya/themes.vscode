#!/usr/bin/python

import subprocess
import pathlib

parentPath = pathlib.Path(__file__).parent
generatorPath = pathlib.Path(parentPath, 'generate_theme.py')

themes = [
    {'name': 'krone', 'accent': '#6e43e5', 'number': '#f9545e', 'bracket': '#f9545e'},
    {'name': 'ryu', 'accent': '#ff2281', 'number': '#f9545e', 'bracket': '#f9545e'},
    {'name': 'vaatu', 'accent': '#f148fb', 'number': '#FAF555', 'bracket': '#FFFF0A'},
    {'name': 'volskaya', 'accent': '#04D976', 'number': '#f9545e', 'bracket': '#f9545e'},
    {'name': 'lore', 'accent': '#e2cc9e', 'number': '#a39a89', 'bracket': '#a39a89'},
    {'name': 'po', 'accent': '#FFFF0A', 'number': '#f9545e', 'bracket': '#f9545e'},
    {'name': 'mirai', 'accent': '#f20530', 'number': '#FFFF0A', 'bracket': '#FFFF0A'},
    {'name': 'twitch', 'accent': '#9146FF', 'number': '#f9545e', 'bracket': '#f9545e'},
]

for theme in themes:
    args = [f"--{key}={value}" for key, value in theme.items()]
    print(f'Calling {generatorPath.name} with "{" ".join(args)}"')
    subprocess.call([str(generatorPath), *args])
    print('\n')
