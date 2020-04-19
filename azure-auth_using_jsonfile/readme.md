# Azure Authentication using a JSON file

* Azure Authentication with Python: https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-authenticate#mgmt-auth-file
* Azure Packages for Python: https://azure.github.io/azure-sdk/releases/latest/all/python.html

## Requirements

Install Python Azure Compute package
```
python -m pip install azure.mgmt.compute
python -m pip install azure.common
python -m pip install azure-cli-core
```

You can create a `credentials.json` file using Az cli (see doc to create manually)
```
az login
az ad sp create-for-rbac --sdk-auth > credentials.json
```

The `credentials.json` file content looks like this:

```json
{
  "clientId": "<client_id>",
  "clientSecret": "<client_secret>",
  "subscriptionId": "<sub_id>",
  "tenantId": "<tenantid>",
  "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
  "resourceManagerEndpointUrl": "https://management.azure.com/",
  "activeDirectoryGraphResourceId": "https://graph.windows.net/",
  "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
  "galleryEndpointUrl": "https://gallery.azure.com/",
  "managementEndpointUrl": "https://management.core.windows.net/"
}

```