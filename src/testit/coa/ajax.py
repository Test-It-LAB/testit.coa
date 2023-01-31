from bika.lims import api
from bika.coa.ajax import AjaxPublishView as AP


class AjaxPublishView(AP):
    def ajax_templates(self):
        """Returns the available templates
        """
        templates = api.get_registry_record("senaite.impress.templates")
        return sorted([item for item in templates if 'tesit' in item])
