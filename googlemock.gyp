{
    'target_defaults': {
        'include_dirs': [
            'include',
            '<(DEPTH)/ext/googletest/include',
        ],
    },
    'targets': [
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
                ':check-deps',
                ':gmock',
            ],
        },
    ],
}
