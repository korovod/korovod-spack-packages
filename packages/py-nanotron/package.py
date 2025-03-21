from spack.package import *

class PyNanotron(PythonPackage):
    """Minimalistic large language model 3D-parallelism training."""

    homepage = "https://github.com/korovod/nanotron"
    git = "https://github.com/korovod/nanotron.git"

    maintainers("thomas-bouvier")

    license("Apache-2.0")

    version("main", branch="main")

    variant("examples", default=True, description="Build with example scripts support")

    depends_on("python@3.6:3.11")

    depends_on("py-setuptools", type="build")
    depends_on("py-torch@1.13.0:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-numpy@:2", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-safetensors", type=("build", "run"))
    depends_on("py-dacite", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-datasets", type=("build", "run"), when="@0.5:")

    depends_on("py-transformers", type=("build", "run"), when="+examples")
    depends_on("py-flash-attn", type=("build", "run"), when="+examples")
