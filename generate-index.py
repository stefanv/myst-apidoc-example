import json
import textwrap
import pathlib


packages = ['skimage'] #, 'skimage2']


with open('index.md', "w") as f:
    f.write(textwrap.dedent('''\
    ---
    title: skimage API docs
    ---

    '''))

    for pkg in packages:
        f.write(f'- [{pkg}](./{pkg})\n')


for pkg in packages:
    pathlib.Path(pkg).mkdir(exist_ok=True)

    api = json.load(open(f"{pkg}-api.json", "rb"))

    with open(f"{pkg}/index.md", "w") as f:
        f.write(textwrap.dedent(f'''\
        ---
        title: {pkg}
        ---
        '''))
        for module in api:
            f.write(f'- [{module}](./{module})\n')

    for module in api:
        with open(f"{pkg}/{module}.md", "w") as f:
           f.write(textwrap.dedent(f'''\
           ---
           title: {pkg}.{module}
           ---

           :::{{apidoc}} ./{pkg}-api.json#{module}
           :module: skimage
           :depth: 1
           :::
           '''))
