# Pants example

This repo tries to make a pants library that includes tests

## Things that don't work but I think they should

### Testing

```
pants_example$ ./pants dependencies --transitive src/python/my-subproject/tests/test_my_subproject.py
src/python/my-subproject/my_subproject/__init__.py
src/python/my-subproject/my_subproject/__init__.py:../my_subproject_sources
src/python/my-subproject/my_subproject/core/__init__.py:../../my_subproject_sources
src/python/my-subproject/my_subproject/core/config.py:../../my_subproject_sources
src/python/my-subproject/my_subproject/main.py:../my_subproject_sources
src/python/my-subproject/my_subproject/my_script.py:../my_subproject_sources
src/python/my-subproject/pyproject.toml:poetry
src/python/my-subproject:my_subproject_distribution
src/python/my-subproject:poetry#pydantic
src/python/my-subproject:poetry#pyzmq
src/python/my-subproject:pyproject


pants_example$ ./pants --no-local-cache --no-pantsd test ::
17:11:30.78 [INFO] Canceled: Building pytest.pex from pytest_default_lockfile.txt
17:11:45.28 [INFO] Completed: Building requirements.pex with 2 requirements: pydantic<2.0.0,>=1.8.2, pyzmq<23.0.0,>=22.3.0
17:11:55.07 [INFO] Completed: Building pytest.pex from pytest_default_lockfile.txt
17:11:58.90 [INFO] Completed: Building build_backend.pex with 1 requirement: poetry-core>=1.0.0
17:11:59.42 [INFO] Completed: List contents of artifacts produced by src/python/my-subproject:my_subproject_distribution
17:12:00.56 [INFO] Completed: Building local_dists.pex with 1 requirement: my_subproject-0.1.0-py3-none-any.whl
17:12:01.33 [INFO] Completed: Building pytest_runner.pex
17:12:01.33 [ERROR] 1 Exception encountered:

  ProcessExecutionFailure: Process 'Building pytest_runner.pex' failed with exit code 1.
stdout:

stderr:
Traceback (most recent call last):
  File "/Users/maartenderickx/.cache/pants/named_caches/pex_root/unzipped_pexes/3c037481d92e64c70b4c4d598b63e24e6c2bb819/.bootstrap/pex/pex.py", line 503, 
    ...
    ...
    ...
  File "/Users/maartenderickx/.cache/pants/named_caches/pex_root/installed_wheels/9fb4bc59f7085c6133bed415fd8806a166d6f472798f2350158f7f0a710ec0f6/pex-2.1.71-py2.py3-none-any.whl/pex/environment.py", line 582, in resolve_dists
    raise ResolveError(
pex.environment.ResolveError: Failed to resolve requirements from PEX environment @ /Users/maartenderickx/.cache/pants/named_caches/pex_root/unzipped_pexes/1c7638f34d87170c74c32859f4549bb9a127ea34.
Needed cp310-cp310-macosx_12_0_x86_64 compatible dependencies for:
 1: pydantic<2.0.0,>=1.8.2
    Required by:
      FingerprintedDistribution(distribution=my-subproject 0.1.0 (/Users/maartenderickx/.cache/pants/named_caches/pex_root/installed_wheels/e223b653e265d6f66fdd0f020b1a0452749752d34d3482ddbfa7db8029d4404d/my_subproject-0.1.0-py3-none-any.whl), fingerprint='a3b4305beab465271df6b0b6bc4e9662713f2c6768ef17b828097c7346675aed')
    But this pex had no 'pydantic' distributions.
 2: pyzmq<23.0.0,>=22.3.0
    Required by:
      FingerprintedDistribution(distribution=my-subproject 0.1.0 (/Users/maartenderickx/.cache/pants/named_caches/pex_root/installed_wheels/e223b653e265d6f66fdd0f020b1a0452749752d34d3482ddbfa7db8029d4404d/my_subproject-0.1.0-py3-none-any.whl), fingerprint='a3b4305beab465271df6b0b6bc4e9662713f2c6768ef17b828097c7346675aed')
    But this pex had no 'pyzmq' distributions.
```
As you can see the pyzmq and pydantic dependencies are correctly listed, for `test_my_subproject.py` still pants fails by complaining that some pex file does not contain these dependencies.

### Packaging

This is as described in https://github.com/pantsbuild/pants/issues/14983#issuecomment-1086928602

```
pants_example maartenderickx$ ./pants --no-local-cache --no-pantsd package src/python/my-subproject:my_script
17:19:48.04 [INFO] Completed: Building build_backend.pex with 1 requirement: poetry-core>=1.0.0
17:19:48.66 [INFO] Completed: List contents of artifacts produced by src/python/my-subproject:my_subproject_distribution
17:19:50.17 [INFO] Completed: Building local_dists.pex with 1 requirement: my_subproject-0.1.0-py3-none-any.whl
17:19:51.20 [INFO] Completed: Building src.python.my-subproject/my_script.pex
17:19:51.20 [ERROR] 1 Exception encountered:

  ProcessExecutionFailure: Process 'Building src.python.my-subproject/my_script.pex' failed with exit code 1.
stdout:

stderr:
Traceback (most recent call last):
  File "/Users/maartenderickx/.cache/pants/named_caches/pex_root/unzipped_pexes/3c037481d92e64c70b4c4d598b63e24e6c2bb819/.bootstrap/pex/pex.py", line 503, in execute
    exit_value = self._wrap_coverage(self._wrap_profiling, self._execute)
    ...
    ...
    ...
  File "/Users/maartenderickx/.cache/pants/named_caches/pex_root/installed_wheels/9fb4bc59f7085c6133bed415fd8806a166d6f472798f2350158f7f0a710ec0f6/pex-2.1.71-py2.py3-none-any.whl/pex/pex_builder.py", line 305, in add
    raise self.InvalidDistribution(
pex.pex_builder.PEXBuilder.InvalidDistribution: Distribution my_subproject-0.1.0-py3-none-any.whl at /Users/maartenderickx/.pex/installed_wheels/a3b4305beab465271df6b0b6bc4e9662713f2c6768ef17b828097c7346675aed/my_subproject-0.1.0-py3-none-any.whl had hash b0859baf32c3541cba467a0a119bd9df2eedd1e6, expected a3b4305beab465271df6b0b6bc4e9662713f2c6768ef17b828097c7346675aed
```
