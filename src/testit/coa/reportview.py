from bika.coa import logger
from bika.coa.reportview import MultiReportView as MRV
from bika.coa.reportview import SingleReportView as SRV


class SingleReportView(SRV):
    """View for Bika COA Single Reports
    """


class MultiReportView(MRV):
    """View for Bika COA Multi Reports
    """

    def __init__(self, collection, request):
        logger.info("MultiReportView::__init__:collection={}".format(collection))
        super(MultiReportView, self).__init__(collection, request)
        self.collection = collection
        self.request = request
