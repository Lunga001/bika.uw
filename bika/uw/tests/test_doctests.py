from bika.lims.testing import BIKA_FUNCTIONAL_TESTING
from doctest import DocFileSuite
from doctest import DocTestSuite
from plone.testing import layered
import doctest
import unittest

OPTIONFLAGS = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)

DOCTESTS = [
    'bika.uw.browser.batch',
    'bika.uw.browser.analysisrequest',
]


def test_suite():
    suite = unittest.TestSuite()
    for module in DOCTESTS:
        suite.addTests([
            layered(DocTestSuite(module=module, optionflags=OPTIONFLAGS),
                    layer=BIKA_FUNCTIONAL_TESTING),
        ])
    return suite
