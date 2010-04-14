{
    'target_defaults': {
        'include_dirs': [
            'include',
            '<(DEPTH)/ext/googletest/include',
        ],
        'xcode_settings': {
            'GCC_TREAT_WARNINGS_AS_ERRORS': 'YES',
            'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES',
            'SDKROOT': 'macosx10.4',
            'GCC_VERSION': '4.0',
            'ARCHS': 'ppc x86_64 i386',
            'WARNING_CFLAGS': [
                '-Wall',
                '-Wendif-labels',
            ],
        },
    },
    'targets': [
        {
            'target_name': 'check-deps',
            'type': 'none',
            'actions': [
                {
                    'action_name': 'check-deps',
                    'inputs': [ ],
                    'outputs': [ ],
                    'action': [
                        './scripts/check-deps.sh',
                        '<(DEPTH)',
                    ],
                },
            ],
        },
        {
            'target_name': 'gmock',
            'type': '<(library)',
            'sources': [
                'src/gmock-cardinalities.cc',
                'src/gmock-internal-utils.cc',
                'src/gmock-matchers.cc',
                'src/gmock-printers.cc',
                'src/gmock-spec-builders.cc',
                'src/gmock.cc',
            ],
            'dependencies': [
                ':check-deps',
                '<(DEPTH)/ext/googletest/googletest.gyp:gtest',
            ],
        },
        {
            'target_name': 'gmock_main',
            'type': '<(library)',
            'sources': [
                'src/gmock_main.cc',
            ],
            'dependencies': [
                ':gmock',
            ],
        },
    ],
}
