# Usage

- Install required packages
```sh
pip install pelican Markdown pygments typogrify python-markdown-math
```

- Clone this repository somewhere
```sh
git clone git@github.com:jampp/research.git
```

- To develop, run inside the cloned repository:
```sh
make devserver
```
and open your browser at https://127.0.0.1:8000. This will live-reload any changes done to the `content/` folder. Put your posts there.

- To publish, run inside the cloned repository:
```sh
make publish
```
and push your changes to master. Don't forget to add new files, always check `docs/`, run `git status`!
