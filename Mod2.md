# Mod 2: Despliegue de datos y estadísticas básicas.

En este módulo aprenderás a visualizar espacialmente variables continuas y/o categóricas en Plotly a través de un DataFrame en Pandas. Aprenderás a generar estadísticas básicas sobre tus datos de entrada, así como también filtrar tus datos. Finalmente se exportarán los resultados.

Tópicos:

- Importación librerías: pandas, numpy y plotly
- Descripción del contenido DataFrame al cargar muestras
- Visualización espacial de variables continuas y categóricas (Plotly)
- Estadísticas básicas
- Generación de operaciones lógicas para filtros
- Exportación resultados

Duración : 7:38 min.

Tiempo aprox a emplear : 30 min.

Complejidad : Media

## Instalación

Para visualizar los datos espacialmente se necesita instalar la librería externa [plotly](https://plotly.com/python)
```
conda install -c plotly plotly
```

## Ejecución

Puedes replicar el contenido del curso a través de [Jupyter Notebook](https://jupyter.org/):

```
jupyter notebook Mod2.ipynb
```

o a través del siguiente Script python modularizado:

```
python Mod2.py --filename \path\to\your\file --coord [coordx coordy coordz] --cont [var_1 .. var_n] --cat [var_1 .. var_n]
```

Ejemplo:

```
python Mod2.py --filename .\db_mineralogia.csv --coord 'East' 'North' 'Elevation' --cont 'bo' 'py' --cat 'dom' 'mine'
```

o a través del siguiente ejecutable [link download](https://drive.google.com/file/d/11pYruUtIQkn35iUsUG3lQH74HTcPnZOD/view?usp=sharing):

```
./Mod2.exe --filename .\db_mineralogia.csv --coord 'East' 'North' 'Elevation' --cont 'bo' 'py' --cat 'dom' 'mine'
```

## Distribución

Este módulo utiliza pandas y una libería externa plotly. Se recomienda utilizar [Mod2.spec](https://pyinstaller.readthedocs.io/en/stable/spec-files.html) para incluir todas las dependecias al generar su propio Ejecutable.

```
pyinstaller --onefile Mod2.spec
```

```
# Mod2.spec
# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000)
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

a = Analysis(['Mod2.py'],
             pathex=['TU_RUTA_COMPLETA\\intro-a-data-analytics-en-geociencias-con-python\\Mod2'],
             binaries=[],
             datas=[('TU_RUTA_COMPLETA\\anaconda3\\Lib\\site-packages\\plotly', '.\\plotly\\')],
			hiddenimports=['pandas._libs.tslibs.timedeltas', 'pandas._libs.tslibs.np_datetime', 'pandas._libs.tslibs.nattype', 'pandas._libs.skiplist', 'scipy._lib.messagestream'],
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
          name='Mod2',
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