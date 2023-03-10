# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from testit.coa.testing import TESTIT_COA_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that testit.coa is properly installed."""

    layer = TESTIT_COA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if testit.coa is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'testit.coa'))

    def test_browserlayer(self):
        """Test that ITestitCoaLayer is registered."""
        from testit.coa.interfaces import (
            ITestitCoaLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ITestitCoaLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = TESTIT_COA_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['testit.coa'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if testit.coa is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'testit.coa'))

    def test_browserlayer_removed(self):
        """Test that ITestitCoaLayer is removed."""
        from testit.coa.interfaces import \
            ITestitCoaLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ITestitCoaLayer,
            utils.registered_layers())
