from pycep.typing import ParameterAttributes

from checkov.bicep.checks.param.base_param_check import BaseParamCheck
from checkov.common.models.enums import CheckResult, CheckCategories

# https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/test-cases#secure-parameters-cant-have-hardcoded-default


class SecureStringParameterNoHardcodedValue(BaseParamCheck):
    def __init__(self) -> None:
        name = "SecureString parameter should not have hardcoded default values"
        id = "CKV_AZURE_131"
        supported_type = ("string",)
        categories = (CheckCategories.SECRETS,)
        super().__init__(name=name, id=id, categories=categories, supported_type=supported_type)

    def scan_param_conf(self, conf: ParameterAttributes) -> CheckResult:
        if not any(decorator["type"] == "secure" for decorator in conf["decorators"]):
            # if the decorator '@secure()' is not set, then it is a normal string
            return CheckResult.UNKNOWN

        if conf["default"]:  # should be missing, or an empty string
            return CheckResult.FAILED
        else:
            return CheckResult.PASSED


check = SecureStringParameterNoHardcodedValue()
