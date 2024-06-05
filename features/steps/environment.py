"""Behave environment setup commands."""

from commons import get_project_root
import os

def call(cmd, env):
    res = run(cmd, env=env)
    if res.returncode:
        print(res.stdout)
        print(res.stderr)
        assert False

def before_all(context):
    """Environment preparation before other cli tests are run.
    Installs modak by running pip in the top level directory.
    """
    context = _setup_minimal_env(context)
    context = _install_project_requirements(context)

def _setup_minimal_env(context):
        kmodak_install_venv_dir = _create_new_venv()
        context.modak_install_venv_dir = modak_install_venv_dir
        context = _setup_context_with_venv(context, modak_install_venv_dir)

        call(
            [
                context.python,
                "-m",
                "pip",
                "install",
                "-U",
                "pip>=21.2",
            ],
            env=context.env,
        )
        call([context.python, "-m", "pip", "install", "-e", "."], env=context.env)
        return context

def _setup_context_with_venv(context, venv_dir):
    context.venv_dir = venv_dir
    # note the locations of some useful stuff
    # this is because exe resolution in subprocess doesn't respect a passed env
    if os.name == "posix":
        bin_dir = context.venv_dir / "bin"
    else:
        bin_dir = context.venv_dir / "scripts"
    context.bin_dir = bin_dir
    context.pip = str(bin_dir / "pip")
    context.python = str(bin_dir / "python")
    context.modak = str(bin_dir / "modak")

    # clone the environment, remove any condas and venvs and insert our venv
    context.env = os.environ.copy()
    path = context.env["PATH"].split(os.pathsep)
    path = [p for p in path if not (Path(p).parent / "pyvenv.cfg").is_file()]
    path = [p for p in path if not (Path(p).parent / "conda-meta").is_dir()]
    path = [str(bin_dir)] + path
    context.env["PATH"] = os.pathsep.join(path)

    # Create an empty pip.conf file and point pip to it
    pip_conf_path = context.venv_dir / "pip.conf"
    pip_conf_path.touch()
    context.env["PIP_CONFIG_FILE"] = str(pip_conf_path)

    return context
