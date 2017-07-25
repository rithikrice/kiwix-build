class TargetInfo:
    def __init__(self, build, static, toolchains, hosts=None):
        self.build = build
        self.static = static
        self.toolchains = toolchains
        self.compatible_hosts = hosts

    def __str__(self):
        return "{}_{}".format(self.build, 'static' if self.static else 'dyn')

    def get_cross_config(self, host):
        if self.build == 'native':
            return {}
        elif self.build == 'win32':
            root_paths = {
                'fedora': '/usr/i686-w64-mingw32/sys-root/mingw',
                'debian': '/usr/i686-w64-mingw32'
            }
            return {
                'root_path': root_paths[host],
                'extra_libs': ['-lwinmm', '-lws2_32', '-lshlwapi', '-lrpcrt4', '-lmsvcr90'],
                'extra_cflags': ['-DWIN32'],
                'host_machine': {
                    'system': 'Windows',
                    'lsystem': 'windows',
                    'cpu_family': 'x86',
                    'cpu': 'i686',
                    'endian': 'little',
                    'abi': ''
                }
            }
        elif self.build == 'armhf':
            return {
                'extra_libs': [],
                'extra_cflags': [],
                'host_machine': {
                    'system': 'linux',
                    'lsystem': 'linux',
                    'cpu_family': 'arm',
                    'cpu': 'armhf',
                    'endian': 'little',
                    'abi': ''
                }
            }
