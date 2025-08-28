OK_FORMAT = True

test = {   'name': 'complete-log-likelihood-coding',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> assert np.isclose(compute_log_likelihood(1, 1, 0.5, 0.7, 0.4), -1.0498, atol=10 ** (-3)), f'Expected -1.0498, got {compute_log_likelihood(1, 1, "
                                               "0.5, 0.7, 0.4)}'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
