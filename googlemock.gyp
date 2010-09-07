{
    'target_defaults': {
        'include_dirs': [
            'include',
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
                'src/gmock-spec-builders.cc',
                'src/gmock.cc',
            ],
            'dependencies': [
                '<(DEPTH)/ext/googletest/googletest.gyp:gtest',
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                    'include',
                ],
            },
            'export_dependent_settings': [
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
            'export_dependent_settings': [
                ':gmock',
            ],
        },
    ],
}
