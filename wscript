# -*- mode: python -*-

def common(ctx):
    ctx.load("compiler_cxx")
    ctx.load("core externals", "ext/waf-sfiera")
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
        cxxflags="-Wall -Werror",
        includes=". ./include",
        export_includes="./include",
        use="googletest/gtest",
    )

    bld.platform(
        target="googlemock/gmock",
        platform="darwin",
        arch="x86_64 i386 ppc",
    )

    bld.stlib(
        target="googlemock/gmock_main",
        source="src/gmock_main.cc",
        cxxflags="-Wall -Werror",
        use="googlemock/gmock",
    )

    bld.platform(
        target="googlemock/gmock_main",
        platform="darwin",
        arch="x86_64 i386 ppc",
    )
