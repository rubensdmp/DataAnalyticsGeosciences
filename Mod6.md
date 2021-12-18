# Mod 6: Análisis Multivariable

En este módulo aprenderás a realizar un análisis multivariable sobre las variables continúas, a través de la construcción de un conjunto de gráficos en Python, tales como: Matriz de correlación, Scatter y Media Condicional (o derivas).


Tópicos:

- Importación librerías: pandas, seaborn, plotly, probscale, matplotlib.
- Matriz de correlación a través del método corr (Pandas - DataFrame).
- HeatMap de la Matriz correlación (seaborn).
- Scatter entre variables continuas agrupadas por la unidad geológica.
- Media Condicional (o Derivas) en la coordenada East.
- Visualización espacial.
- Gráficos de distribución acumulada por categoría (Probplot).

Duración : 08:27 min.

Tiempo aprox a emplear : 45 min.

Complejidad : Alta

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
jupyter notebook Mod6.ipynb
```

o a través del siguiente Script python modularizado:

```
python Mod6.py --filename \path\to\your\file --coord [coordx coordy coordz] --cont [var_1] --cat [var_1]
```

Ejemplo:

```
python Mod6.py --filename .\output_mod4.csv --coord 'East' 'North' 'Elevation' --cont 'bo' 'py' --cat 'ug'
```

o a través del siguiente ejecutable [link download](https://drive.google.com/file/d/1sH6V7eNUfJmsNUTmQX2WbcUvBUKvS95d/view?usp=sharing):

```
./Mod6.exe --filename .\output_mod4.csv --coord 'East' 'North' 'Elevation' --cont 'bo' 'py' --cat 'ug'
```

## Distribución

Este módulo utiliza pandas y dos liberías externas (mpl-probscale, plotly) incluidas. Se recomienda utilizar [Mod6.spec](https://pyinstaller.readthedocs.io/en/stable/spec-files.html) para incluir todas las dependecias al generar su propio Ejecutable.

```
pyinstaller --onefile Mod6.spec
```

```
# Mod6.spec
# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000)
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

a = Analysis(['Mod6.py'],
             pathex=['TU_RUTA_COMPLETA\\intro-a-data-analytics-en-geociencias-con-python\\Mod6'],
             binaries=[],
             datas=[('TU_RUTA_COMPLETA\\anaconda3\\Lib\\site-packages\\plotly', '.\\plotly\\')],
			 hiddenimports=['pandas._libs.tslibs.timedeltas', 'pandas._libs.tslibs.np_datetime', 'pandas._libs.tslibs.nattype', 'pandas._libs.skiplist', 'scipy._lib.messagestream', 'scipy.special.cython_special'] + collect_submodules('pkg_resources._vendor') + ['pkg_resources.py2_warn'],
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
          name='Mod6',
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