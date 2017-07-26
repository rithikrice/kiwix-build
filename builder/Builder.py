from collections import OrderedDict
from .Environment import Environment
from utils.exception import StopBuild


class Builder:
    def __init__(self, options):
        self.options = options
        self.targets = OrderedDict()
        self.buildEnv = Environment(options, self.targets)

        _targets = {}
        targetDef = options.targets
        # self.add_targets(targetDef, _targets)
        # dependencies = self.order_dependencies(_targets, targetDef)
        # dependencies = list(remove_duplicates(dependencies))
        #
        # for dep in dependencies:
        #     if self.options.build_deps_only and dep == targetDef:
        #         continue
        #     self.targets[dep] = _targets[dep]

    # def add_targets(self, target_name, targets):
    #     if target_name in targets:
    #         return
    #     targetClass = Dependency.all_deps[target_name]
    #     target = targetClass(self.buildEnv)
    #     targets[target_name] = target
    #     for dep in target.dependencies:
    #         self.add_targets(dep, targets)
    #
    # def order_dependencies(self, _targets, targetName):
    #     target = _targets[targetName]
    #     for depName in target.dependencies:
    #         yield from self.order_dependencies(_targets, depName)
    #     yield targetName
    #
    # def prepare_sources(self):
    #     if self.options.skip_source_prepare:
    #         print("SKIP")
    #         return
    #
    #     toolchain_sources = (tlc.source for tlc in self.buildEnv.toolchains if tlc.source)
    #     for toolchain_source in toolchain_sources:
    #         print("prepare sources for toolchain {} :".format(toolchain_source.name))
    #         toolchain_source.prepare()
    #
    #     sources = (dep.source for dep in self.targets.values() if not dep.skip)
    #     sources = remove_duplicates(sources, lambda s: s.__class__)
    #     for source in sources:
    #         print("prepare sources {} :".format(source.name))
    #         source.prepare()
    #
    # def build(self):
    #     toolchain_builders = (tlc.builder for tlc in self.buildEnv.toolchains if tlc.builder)
    #     for toolchain_builder in toolchain_builders:
    #         print("build toolchain {} :".format(toolchain_builder.name))
    #         toolchain_builder.build()
    #
    #     builders = (dep.builder for dep in self.targets.values() if (dep.builder and not dep.skip))
    #     for builder in builders:
    #         print("build {} :".format(builder.name))
    #         builder.build()

    def run(self):
        try:
            print("[INSTALL PACKAGES]")
            self.buildEnv.install_packages()
            # self.buildEnv.finalize_setup()
            # print("[PREPARE]")
            # self.prepare_sources()
            # print("[BUILD]")
            # self.build()
            # # No error, clean intermediate file at end of build if needed.
            # print("[CLEAN]")
            # if self.buildEnv.options.clean_at_end:
            #     self.buildEnv.clean_intermediate_directories()
            # else:
            #     print("SKIP")
        except StopBuild:
            sys.exit("Stopping build due to errors")
