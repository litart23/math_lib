from setuptools import setup, find_packages

setup(
    name='math_lib',  # Имя вашей библиотеки
    version='0.1',    # Версия
    packages=find_packages(),  # Автоматически находит пакеты
    install_requires=[],  # Зависимости (если есть)
    author='litart23',  # Ваше имя
    author_email='ваш@email.com',  # Ваш email
    description='Простая библиотека для математических операций',  # Описание
    long_description=open('README.md').read(),  # Длинное описание из README
    long_description_content_type='text/markdown',  # Тип контента
    url='https://github.com/litart23/math-lib',  # Ссылка на репозиторий
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)