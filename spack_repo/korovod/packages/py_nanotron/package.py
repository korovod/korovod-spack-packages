from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *

class PyNanotron(PythonPackage):
    """Minimalistic large language model 3D-parallelism training.
    """

    homepage = "https://github.com/korovod/kenotron"
    git = "https://github.com/korovod/kenotron.git"

    maintainers("thomas-bouvier")

    license("Apache-2.0")

    version("main", branch="main")

    variant("nanosets", default=True, description="Dataset processing tools")
    variant("datastates", default=False, description="Efficient asynchronous checkpointing using CUDA copy engines")

    depends_on("python@3.9:3.11")

    depends_on("py-setuptools", type="build")
    depends_on("py-torch@2:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-numpy@:2", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-safetensors", type=("build", "run"))
    depends_on("py-dacite", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-wandb", type=("build", "run"))
    depends_on("py-datasets", type=("build", "run"), when="@0.5:")
    depends_on("py-transformers", type=("build", "run"))
    depends_on("py-flash-attn@2.7:", type=("build", "run"))

    # Nanosets
    depends_on("py-transformers", type=("build", "run"), when="+nanosets")
    depends_on("py-numba", type=("build", "run"), when="+nanosets")
    depends_on("py-datatrove", type=("build", "run"), when="+nanosets")

    # DataStates
    depends_on("py-datastates", type=("build", "run"), when="+datastates")
