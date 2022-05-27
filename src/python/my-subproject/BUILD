poetry_requirements(name="poetry")

resource(name="pyproject", source="pyproject.toml")
resources(name="my_subproject_sources", sources=["my_subproject/**/*.py"])

python_distribution(
    name="my_subproject_distribution",
    dependencies=[
        ":pyproject",
        ":my_subproject_sources",
        ":poetry#pydantic",
        ":poetry#pyzmq",
    ],
    provides=python_artifact(
        name="my_subproject_distribution",
    ),
    entry_points={
        "console_scripts": {
            "some_helpful_script": "my_script:main"
        }
    },
    sdist=False, # needed because of https://github.com/pantsbuild/pants/issues/14983#issuecomment-1086656910
)


pex_binary(
    name="my_script",
    # don't know how to add a script, I would like the following to work
    # script="some_helpful_script",
    # entry points work:
    # entry_point="my_subproject.my_script:main",
    # entry_point="my_subproject.my_script",
    entry_point="my_subproject/my_script.py",
    dependencies=[":my_subproject_distribution"]
)