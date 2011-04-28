# -*- mode: python -*-

DEFAULTS = {
    "cxxflags": "-Wall -Werror",
    "arch": "x86_64 i386 ppc",
}

def common(ctx):
    ctx.load("compiler_cxx")
    ctx.load("externals", "ext/waf-sfiera")
    ctx.load("platforms", "ext/waf-sfiera")
    ctx.external("googletest")

def options(opt):
    common(opt)

def configure(cnf):
    common(cnf)

def build(bld):
    common(bld)

    bld.stlib(
        target="googlemock/gmock",
        source=[
            "src/gmock-cardinalities.cc",
            "src/gmock-internal-utils.cc",
            "src/gmock-matchers.cc",
            "src/gmock-spec-builders.cc",
            "src/gmock.cc",
        ],
        includes=". ./include",
        export_includes="./include",
        use=[
            "googletest/common",
            "googletest/gtest",
        ],
        **DEFAULTS
    )

    bld.stlib(
        target="googlemock/gmock_main",
        source="src/gmock_main.cc",
        use=[
            "googletest/common",
            "googlemock/gmock",
        ],
        **DEFAULTS
    )
