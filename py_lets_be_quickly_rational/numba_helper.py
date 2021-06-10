try:
    from numba import jit_module, jit
except ImportError:
    jit_module = None

def empty_fn(**kwargs):
    return

def maybe_jit_module():
    if jit_module:
        return jit_module
    else:
        return empty_fn

def maybe_jit(*jit_args, **jit_kwargs):
    def wrapper(fun):
        if callable(jit):
            return jit(*jit_args, **jit_kwargs)(fun)
        else:
            return fun
    return wrapper