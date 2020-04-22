from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.compute import ComputeManagementClient




# Retrieve tenant_id, client_id, and client_secret from Azure KeyVault
config_dict = {
    "subscriptionId": "bfc42d3a-65ca-11e7-95cf-ecb1d756380e",
    "tenantId": tenant_id,
    "clientId": client_id,
    "clientSecret": client_secret,
    "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
    "resourceManagerEndpointUrl": "https://management.azure.com/",
    "activeDirectoryGraphResourceId": "https://graph.windows.net/",
    "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
    "galleryEndpointUrl": "https://gallery.azure.com/",
    "managementEndpointUrl": "https://management.core.windows.net/"
}
client = get_client_from_json_dict(ComputeManagementClient, config_dict)


# Show properties of the object
def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %r" % (attr, getattr(obj, attr)))

#
dump(client)