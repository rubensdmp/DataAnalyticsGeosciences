# Mod 3: Búsqueda de controles geológicos.

En este módulo aprenderás a determinar los atributos geológicos (Alteración, Zona Mineral, Dominio) que tengan algún control sobre la variable de interés (Bornita).

Tópicos:

- Importación librerías: pandas, plotly, probscale, matplotlib.
- Estadísticas básicas (globales).
- Estadísticas básicas por categoría con groupby.
- Gráficos de distribución acumulada por categoría (Probplot).
- Exportación de gráficos 2D con matplotlib.
- Visualización espacial por población de variables.

Duración : 10:55 min.

Tiempo aprox a emplear : 30 min.

Complejidad : Media

## Instalación

Para visualizar los datos espacialmente se necesita instalar la librería externa [plotly](https://plotly.com/python)
```
conda install -c plotly plotly
```

Para crear Probability Plots se necesita instalar la librería externa [mpl-probscale](https://matplotlib.org/mpl-probscale/tutorial/getting_started.html)
```
conda install -c conda-forge mpl-probscale
```

## Ejecución

Puedes replicar el contenido del curso a través de [Jupyter Notebook](https://jupyter.org/):

```
jupyter notebook Mod3.ipynb
```

o a través del siguiente Script python modularizado:

```
python Mod3.py --filename \path\to\your\file --coord [coordx coordy coordz] --cont [var_1 .. var_n] --cat [var_1 .. var_n]
```

Ejemplo:

```
python Mod3.py --filename .\db_mineralogia.csv --coord 'East' 'North' 'Elevation' --cont 'bo' 'py' --cat 'dom' 'mine'
```

o a través del siguiente ejecutable [link download](https://drive.google.com/file/d/1HrKeW8EsYq5GjG_SKRQrPBHkwYjbED3J/view?usp=sharing):

```
./Mod3.exe --filename .\db_mineralogia.csv --coord 'East' 'North' 'Elevation' --cont 'bo' 'py' --cat 'dom' 'mine'
```

## Distribución

Este módulo utiliza pandas y una libería externa mpl-probscale incluida. Se recomienda utilizar [Mod3.spec](https://pyinstaller.readthedocs.io/en/stable/spec-files.html) para incluir todas las dependecias al generar su propio Ejecutable.

```
pyinstaller --onefile Mod3.spec
```

```
# Mod3.spec
# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000)
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

a = Analysis(['Mod3.py'],
             pathex=['TU_RUTA_COMPLETA\\intro-a-data-analytics-en-geociencias-con-python\\Mod3'],
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
          name='Mod3',
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