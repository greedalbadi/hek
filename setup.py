from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
  name='hek',
  version='0.2.9',
  description='A python library mostly used for pentesting and automate some tasks.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/greedalbadi/hek',
  author='greed albadi',
  author_email='greedalbadi@gmail.com',
  project_urls={
      'Source': 'https://github.com/greedalbadi/hek',
      'Report Bugs': 'https://github.com/greedalbadi/hek/issues',
      'Download': 'https://pypi.org/project/PyScaffold/#files',
      'Documentation': 'https://github.com/greedalbadi/hek/blob/master/README.md'
  },
  license='MIT',
  keywords=["python", "pentesting", "automation", "stream", "http", "education"],
  packages=find_packages(),
  install_requires=['pillow', "psutil", "requests", "requests[socks]",
                    "numpy", "pyautogui", "datetime", "opencv-python"
                    ]
)