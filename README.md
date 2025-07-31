## Resources

+ <b><a href="">src</a></b> (code itself)
+ <b><a href="https://github.com/scraptechguy/tvet/blob/main/docs/CONCEPTS.md">Key concepts</a></b> (explains all key concepts used in tvet)
+ <b><a href="https://sirrah.troja.mff.cuni.cz/~mira/tmp/diplomky/Broz_2024.pdf">Dokumentace v češtině</a></b> 

## Project structure

```bash
tvet/           ← root of your repo
├── tvet/       ← your package
│   ├── __init__.py
│   ├── cli.py             ← your `main()` moved here
│   ├── core.py            ← `Asteroid` class + helpers
│   ├── photometry.py      ← `f_lambert`/`f_lommel`/`f_hapke`
│   ├── geometry.py        ← loading, normals, cosines, fluxes
│   ├── io.py              ← OBJ loading, file dialogs
│   └── _shadowing.py      ← your fmodpy import wrapper
├── tests/                 ← pytest tests
│   ├── test_core.py
│   └── test_photometry.py
├── README.md
├── LICENSE
├── pyproject.toml         ← build system + metadata
├── setup.cfg              ← optional metadata
└── MANIFEST.in            ← include meshes, data files, FORTRAN sources
```
