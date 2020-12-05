import os
import PyInstaller.__main__ as executable_generator

def _generate_executable():
    current_dir = os.getcwd()
    client_file =os.path.join(current_dir, 'src/client.py')
    distdir = os.path.join(current_dir, 'dist')
    builddir = os.path.join(current_dir, 'build')

    if not os.path.exists('dist'):
        os.makedirs('dist')
    if not os.path.exists('build'):
        os.makedirs('build')
    executable_generator.run([
        client_file,
        '--onefile',
        '--distpath',
        distdir,
        '--workpath',
        builddir,
    ])