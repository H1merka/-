from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()


setup(
    name='recfacelib',
    version='0.0.1',
    author='Progress-code team',
    author_email='',
    description='Этот репозиторий предназначен для обнаружения, выравнивания, распознавания лиц, а также для создания векторов признаков для заданных лиц и их сравнения.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/H1merka/Face_recognition',
    packages=find_packages(),
    install_requires=['click>=8.1.7',
        'colorama>=0.4.6',
        'dlib @ https://github.com/z-mahmud22/Dlib_Windows_Python3.x/raw/main/dlib-19.24.1-cp311-cp311-win_amd64.whl',
        'face-recognition>=1.3.0',
        'face-recognition-models>=0.3.0',
        'numpy>=1.26.4',
        'opencv-python>=4.9.0.80',
        'pillow>=10.3.0'
    ],
    classifiers=[
      'Programming Language :: Python :: 3.11.7',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent'
    ],
    keywords='',
    project_urls={
      'Dlib_package_GitHub': 'https://github.com/z-mahmud22/Dlib_Windows_Python3.x'
    },
    python_requires='==3.11.7'
)
