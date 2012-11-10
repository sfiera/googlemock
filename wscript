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
        features="universal",
        source=[
            "src/gmock-cardinalities.cc",
            "src/gmock-internal-utils.cc",
            "src/gmock-matchers.cc",
            "src/gmock-spec-builders.cc",
            "src/gmock.cc",
        ],
        cxxflags="-Wall -Werror",
        defines="GTEST_USE_OWN_TR1_TUPLE",
        includes=". ./include",
        export_includes="./include",
        use="googletest/gtest",
    )

    bld.stlib(
        target="googlemock/gmock_main",
        features="universal",
        source="src/gmock_main.cc",
        cxxflags="-Wall -Werror",
        defines="GTEST_USE_OWN_TR1_TUPLE",
        use="googlemock/gmock",
    )
