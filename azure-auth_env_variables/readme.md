# Azure Authentication using environment variables

example initially from https://github.com/Azure-Samples/resource-manager-python-resources-and-groups/blob/master/example.py


## Requirements

Install Python Azure Compute package
```
python -m pip install azure.mgmt.compute
python -m pip install azure.common
python -m pip install azure-cli-core
```

Create secrets.json with you SPN secrets data
```
{
    "appId": "<clientid>",
    "password": "<client_secret>",
    "tenant": "<tenant_id>",
    "subscription_id": "<subscriptionid>"
}
```

You can generate a new SPN using the az cli
```
az login
az ad sp create-for-rbac --sdk-auth > secrets.json
```

## Usage

```
python3 example.py
```

## Resources

* Azure Authentication with Python: https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-authenticate#mgmt-auth-file
* Azure Packages for Python: https://azure.github.io/azure-sdk/releases/latest/all/python.html