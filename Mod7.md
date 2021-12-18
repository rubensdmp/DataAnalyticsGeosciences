# Mod 7: Exportación y generación de reporte

En este módulo haremos un énfasis a los métodos en Pandas y Matplotlib que nos permiten exportar nuestros resultados.

Tópicos:

- Exportación DataFrame a archivo: to_csv
- Exportación Gráficos a imagen (png o jpg): savefig

Duración : 04:05 min.

Tiempo aprox a emplear : 15 min.

Complejidad : baja


## Ejecución

Puedes replicar el contenido del curso a través de [Jupyter Notebook](https://jupyter.org/):

```
jupyter notebook Mod7.ipynb
```

o a través del siguiente Script python modularizado:

```
python Mod7.py --filename \path\to\your\file
```

Ejemplo:

```
python Mod7.py --filename .\output_mod6.csv
```

o a través del siguiente ejecutable [link download](https://drive.google.com/file/d/1sHEiHtwMOABchciqolz6EC5gQrpNUJ74/view?usp=sharing):

```
./Mod7.exe --filename .\output_mod6.csv
```

## Distribución

Este módulo utiliza pandas. Se recomienda utilizar [Mod7.spec](https://pyinstaller.readthedocs.io/en/stable/spec-files.html) para incluir todas las dependecias al generar su propio Ejecutable.

```
pyinstaller --onefile Mod7.spec
```

```
# Mod7.spec
# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000)
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

a = Analysis(['Mod7.py'],
             pathex=['TU_RUTA_COMPLETA\\intro-a-data-analytics-en-geociencias-con-python\\Mod7'],
             binaries=[],
             datas=[],
			 hiddenimports=['pandas._libs.tslibs.timedeltas', 'pandas._libs.tslibs.np_datetime', 'pandas._libs.tslibs.nattype', 'pandas._libs.skiplist', 'scipy._lib.messagestream'] + collect_submodules('pkg_resources._vendor') + ['pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Mod7',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )

```

## Licencia
[MIT](https://choosealicense.com/licenses/mit/)