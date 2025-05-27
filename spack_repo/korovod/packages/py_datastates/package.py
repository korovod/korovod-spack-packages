from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *

class PyDatastates(PythonPackage, CudaPackage):
    """Efficient asynchronous checkpointing using CUDA copy engines
    """

    homepage = "https://github.com/korovod/datastates"
    git = "https://github.com/korovod/datastates.git"

    maintainers("thomas-bouvier")

    license("MIT")

    version("main", branch="main")

    with default_args(type=("build")):
        depends_on("py-setuptools")
        depends_on("py-packaging")
        depends_on("py-pip")

    with default_args(type=("build", "link", "run")):
        depends_on("python@3:")
        depends_on("py-torch@2: +cuda")

    depends_on("py-pybind11", type=("build", "link", "run"))
    depends_on("cuda@12:")

    def setup_build_environment(self, env):
        env.set("CUDA_HOME", self.spec["cuda"].prefix)
