from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
  name='hek',
  version='0.2.1',
  description='A python library mostly used for pentesting and automate some tasks.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/greedalbadi/hek',
  author='greed albadi',
  author_email='greedalbadi@gmail.com',
  license='MIT',
  keywords=["python", "pentesting", "automation", "stream", "http"],
  packages=find_packages(),
  install_requires=['pillow', "psutil", "requests", "requests[socks]",
                    "numpy", "pyautogui", "datetime", "opencv-python"
                    ]
)