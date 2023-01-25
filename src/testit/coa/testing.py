# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import testit.coa


class TestitCoaLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=testit.coa)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'testit.coa:default')


TESTIT_COA_FIXTURE = TestitCoaLayer()


TESTIT_COA_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TESTIT_COA_FIXTURE,),
    name='TestitCoaLayer:IntegrationTesting',
)


TESTIT_COA_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TESTIT_COA_FIXTURE,),
    name='TestitCoaLayer:FunctionalTesting',
)


TESTIT_COA_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TESTIT_COA_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='TestitCoaLayer:AcceptanceTesting',
)
