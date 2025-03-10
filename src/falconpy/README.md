![CrowdStrike Falcon](../../docs/asset/cs-logo.png)
# FalconPy - The CrowdStrike Falcon SDK for Python 3
This folder contains the FalconPy project, a Python 3 interface handler for the CrowdStrike Falcon OAuth2 API.

## Service Classes
### Currently implemented:
+ `cloud_connect_aws.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws
+ `cspm-registration.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration
+ `custom_ioa.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa
+ `d4c_registration.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration
+ `detects.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/detects
+ `device_control_policies.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/device-control-policies
+ `event_streams.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/event-streams
+ `falcon_complete_dashboard.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falcon-complete-dashboard
+ `falconx_sandbox.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox
+ `firewall_management.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management
+ `firewall_policies.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies
+ `host_group.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group
+ `hosts.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts
+ `identity_protection.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/identity-protection
+ `incidents.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents
+ `installation_tokens.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens
+ `intel.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel
+ `ioa_exclusions.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions
+ `ioc.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc
+ `iocs.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs
+ `kubernetes_protection.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection
+ `malquery.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/malquery
+ `ml_exclusions.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions
+ `mssp.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp
+ `oauth2.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/oauth2
+ `overwatch_dashboard.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/overwatch-dashboard
+ `prevention_policy.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies
+ `quick_scan.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/quick-scan
+ `real_time_response_admin.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin
+ `real_time_response.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response
+ `recon.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon
+ `response_policies.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/response-policies
+ `sample_uploads.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sample-uploads
+ `sensor_download.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download
+ `sensor_update_policy.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies
+ `sensor_visibility_exclusions.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-visibility-exclusions
+ `spotlight_vulnerabilities.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/spotlight-vulnerabilities
+ `user_management.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management
+ `zero_trust_assessment.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/zero-trust-assessment

## The Uber Class
### A single class to interface with the entire API
+ `api_complete.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html
