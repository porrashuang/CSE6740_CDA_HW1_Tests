OK_FORMAT = True

test = {   'name': 'distance_euclidean',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> assert np.isclose(distance_euclidean(np.array([1]), np.array([0])), 1.0)\n',
                                       'failure_message': '1st distance_euclidean public test failed',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5},
                                   {   'code': '>>> assert np.isclose(distance_euclidean(np.array([0, 0]), np.array([3, 4])), 5.0)\n',
                                       'failure_message': '2nd distance_euclidean public test failed',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
