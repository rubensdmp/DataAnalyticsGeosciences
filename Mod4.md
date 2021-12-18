# Mod 4: Definición de unidad de estimación.

En este módulo aprenderás a crear una unidad de estimación, a través de la definición de una nueva variable (columna) en nuestro DataFrame (pandas). Posteriormente, mediante operaciones lógicas, podrás crear nuevos códigos geológicos sujeto a las variables: alteración, zona mineral y dominio.

Tópicos:

- Importación librerías: pandas, plotly, probscale, matplotlib.
- Creación de nuevas columnas en DataFrame.
- Iteración sobre DataFrame mediante iterrows().
- Modificación de valores en el DataFrame mediante loc[].
- Visualización espacial.

Duración : 08:56 min.

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
jupyter notebook Mod4.ipynb
```

o a través del siguiente Script python modularizado:

```
python Mod4.py
```

o a través del siguiente ejecutable [link download](https://drive.google.com/file/d/1I54VUuCVL1dgFfwFweqWKjapBj2PGlgk/view?usp=sharing):

```
./Mod4.exe
```

## Distribución

Este módulo utiliza pandas y dos liberías externas (mpl-probscale, plotly) incluidas. Se recomienda utilizar [Mod4.spec](https://pyinstaller.readthedocs.io/en/stable/spec-files.html) para incluir todas las dependecias al generar su propio Ejecutable.

```
pyinstaller --onefile Mod4.spec
```

```
# Mod4.spec
# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000)
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

a = Analysis(['Mod4.py'],
             pathex=['TU_RUTA_COMPLETA\\intro-a-data-analytics-en-geociencias-con-python\\Mod4'],
             binaries=[],
             datas=[('TU_RUTA_COMPLETA\\anaconda3\\Lib\\site-packages\\plotly', '.\\plotly\\')],
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
          name='Mod4',
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