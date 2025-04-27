from setuptools import setup, find_packages

setup(
    name="todo_manager",                     # 项目名称
    version="0.1.0",                       # 版本号
    author="jackmin-sw",                    # 作者
    author_email="jackmin.sw@gmail.com", # 作者邮箱
    description="Python todo list",     # 项目简介
    long_description=open("README.md").read(),  # 详细描述，通常从 README 读取
    long_description_content_type="text/markdown",  # 描述格式
    url="https://github.com/jackmin-sw/todo_manager",  # 项目主页
    packages=find_packages(where="src"),
    package_dir={"": "src"},              # 自动查找所有 Python 包
    install_requires=[                     # 依赖列表
        "requests>=2.25.1",
        "numpy",
    ],
    classifiers=[                          # 项目分类信息
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",               # Python 版本要求
)