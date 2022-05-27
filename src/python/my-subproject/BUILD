poetry_requirements(name="poetry")

resource(name="pyproject", source="pyproject.toml")
resources(name="my_subproject_sources", sources=["my_subproject/**/*.py"])

python_distribution(
    name="my_subproject_distribution",
    dependencies=[
        ":pyproject",
        ":my_subproject_sources",
    ],
    provides=python_artifact(
        name="my_subproject_distribution",
    ),
    sdist=False, # needed because of https://github.com/pantsbuild/pants/issues/14983#issuecomment-1086656910
)


pex_binary(
    name="my_script",
    script="my_script.py",
    dependencies=[":my_subproject_distribution"]
)