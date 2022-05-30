python_requirements(resolve="my-subproject2")

python_distribution(
    name="my_subproject2_distribution",
    dependencies=[
        "./my_subproject2:my_subproject2",
    ],
    provides=python_artifact(
        name="my_subproject2_distribution",
        version="0.2.0",
    ),
    entry_points={
        "console_scripts": {
            "some_helpful_script": "my_script:main"
        }
    },
    sdist=False, # needed because of https://github.com/pantsbuild/pants/issues/14983#issuecomment-1086656910
    generate_setup = True,
)


pex_binary(
    name="my_script",
    # don't know how to add a script, I would like the following to work
    # script="some_helpful_script",
    # entry points work:
    # entry_point="my_subproject2.my_script:main",
    # entry_point="my_subproject2.my_script",
    entry_point="my_subproject2/my_script.py",
    dependencies=[":my_subproject2_distribution"]
)