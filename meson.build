project('pymt_heatc', 'c', 'cython', version: '0.4')

py = import('python').find_installation(pure: false)

python_inc = py.get_path('data') / 'include'
numpy_inc = run_command(
    py,
    [
        '-c',
        'import numpy; print(numpy.get_include())'
    ],
    check: true
).stdout().strip()
incs = include_directories(
    [
        meson.project_name() / 'lib',
        python_inc,
        numpy_inc,
    ]
)

deps = [
    dependency('bmiheatc')
]

srcs = [
    meson.project_name() / 'lib/heatmodelc.pyx',
]

# Files get copied to <python directory>/site-packages/<subdir>
install_pkg_srcs = [
    meson.project_name() / '__init__.py',
    meson.project_name() / 'bmi.py',
]
py.install_sources(
    install_pkg_srcs,
    subdir: meson.project_name(),
)
install_lib_srcs = [
    meson.project_name() / 'lib/__init__.py',
    meson.project_name() / 'lib/heatmodelc.pyx',
]
py.install_sources(
    install_lib_srcs,
    subdir: meson.project_name() / 'lib',
)

install_subdir(
    'meta/HeatModelC',
    install_dir: py.get_install_dir() / meson.project_name() / 'data',
)

py.extension_module(
    'heatmodelc',
    srcs,
    dependencies: deps,
    include_directories: incs,
    install: true,
    subdir: meson.project_name() / 'lib',
)

# This is a temporary fix for editable installs.
run_command('cp', '-r', meson.project_name() / 'data', 'build')
