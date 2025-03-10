# Version 0.5.0
## Added features and functionality
+ Added: IOC API Service Class (`ioc.py`)
    * indicator_combined_v1
    * indicator_get_v1
    * indicator_create_v1
    * indicator_delete_v1
    * indicator_update_v1
    * indicator_search_v1
+ Added: Kubernetes Protection API Service Class (`kubernetes_protection.py`)
    * GetAWSAccountsMixin0
    * CreateAWSAccount
    * DeleteAWSAccountsMixin0
    * UpdateAWSAccount
    * GetLocations
    * GetHelmValuesYaml
    * RegenerateAPIKey
    * GetClusters
    * TriggerScan
+ Added: Recon API Service Class (`recon.py`)
    * AggregateNotificationsV1
    * PreviewRuleV1
    * GetActionsV1
    * CreateActionsV1
    * DeleteActionV1
    * UpdateActionV1
    * GetNotificationsDetailedTranslatedV1
    * GetNotificationsDetailedV1
    * GetNotificationsTranslatedV1
    * GetNotificationsV1
    * DeleteNotificationsV1
    * UpdateNotificationsV1
    * GetRulesV1
    * CreateRulesV1
    * DeleteRulesV1
    * UpdateRulesV1
    * QueryActionsV1
    * QueryActionsV1
    * QueryNotificationsV1
    * QueryRulesV1
+ Added: Response Policies API Service Class (`response_policies.py`)
    * queryCombinedRTResponsePolicyMembers
    * queryCombinedRTResponsePolicies
    * performRTResponsePoliciesAction
    * setRTResponsePoliciesPrecedence
    * getRTResponsePolicies
    * createRTResponsePolicies
    * deleteRTResponsePolicies
    * updateRTResponsePolicies
    * queryRTResponsePolicyMembers
    * queryRTResponsePolicies
+ Updated: CSPM Registration API Service Class (`cspm_registration.py`)
    * Refactored to utilized updated pattern for Service Classes
    * Added: PatchCSPMAwsAccount function
    * Added: UpdateCSPMAzureTenantDefaultSubscriptionID function
    * Added: GetIOAEvents function
    * Added: GetIOAUsers function
    * Updated: Unit tests
+ Updated: Discover for Cloud Registration API Service Class (`d4c_registration.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: IOA Exclusions API Service Class (`ioa_exclusions.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: IOCs API Service Class (`iocs.py`)
    * Refactored to utilized updated pattern for Service Classes
    * Updated: Deprecated multiple endpoints as part of the release of the new IOC Service Class (`_endpoint/_iocs.py`)
+ Updated: Falcon Complete Dashboard API Service Class (`falcon_complete_dashboard.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: Falcon Flight Control API Service Class (`mssp.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: Installation Tokens API Service Class (`installation_tokens.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: Malquery API Service Class (`malquery.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: ML Exclusions API Service Class (`ml_exclusions.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: Overwatch Dashboard API Service Class (`overwatch_dashboard.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: Prevention Policies API Service Class (`prevention_policy.py`)
    * Refactored to utilized updated pattern for Service Classes
    * Updated: Added _add-rule-group_ and _remove-rule-group_ actions to __action_name__ parameter for performPreventionPoliciesAction function. (`_endpoint/_prevention_policy.py`)
+ Updated: Sensor Visibility Exclusions API Service Class (`sensor_visibility_exclusions.py`)
    * Refactored to remove unnecessary private method call / import of the sys library

## Other
+ Added: CSPM Registration API sample - CSPM registration policy export (@mccbryan3)

# Version 0.4.10
## Added features and functionality
+ Added: Timeout support - Float / tuple that is passed to the requests library when performing
requests to the API. Can specify timeouts for connect, read and global.

## Issues resolved
+ Fixed: Service Class proxy functionality support

## Other
+ Timeout functionality unit tests (`test_timeout.py`)

# Version 0.4.9
## Added features and functionality
+ Added: Proxy support - dictionary of proxies that are passed to the requests library when
performing requests to the API.
+ Related to discussion post [#154](https://github.com/CrowdStrike/falconpy/discussions/154)

# Version 0.4.8
## Issues resolved
+ Fixed: Parsing issue with __ids__ argument within MSSP.getChildren (Flight Control Service Class)
    * Resolved by migrating `mssp.py` source to the new pattern being tested for Service Classes.
    * Closes [#144](https://github.com/CrowdStrike/falconpy/issues/144)

# Version 0.4.7
## Added features and functionality

> New Service Class pattern - Query String parameters can now be passed as function arguments.

> This functionality is currently only available in the following new Service Classes while
> regression testing is underway.

+ Added: D4C Registration API Service Class (`d4c_registration.py`)
    * GetCSPMAzureAccount
    * CreateCSPMAzureAccount
    * UpdateCSPMAzureAccountClientID
    * GetCSPMAzureUserScriptsAttachment
    * GetCSPMAzureUserScripts
    * GetCSPMCGPAccount
    * GetCSPMGCPAccount (redirects to GetCSPMCGPAccount)
    * CreateCSPMGCPAccount
    * GetCSPMGCPUserScriptsAttachment
    * GetCSPMGCPUserScripts
    - Added unit tests (`test_d4c_registration.py`)
+ Added: Installation Tokens API Service Class (`installation_tokens.py`)
    * audit_events_read
    * customer_settings_read
    * tokens_read
    * tokens_create
    * tokens_delete
    * tokens_update
    * audit_events_query
    * tokens_query
    - Added unit tests (`test_installation_tokens.py`)
+ Added: IOA Exclusions API Service Class (`ioa_exclusions.py`)
    * getIOAExclusionsV1
    * createIOAExclusionsV1
    * deleteIOAExclusionsV1
    * updateIOAExclusionsV1
    * queryIOAExclusionsV1
    - Added unit tests (`test_ioa_exclusions.py`)
+ Added: Falcon Complete Dashboard API Service Class (`falcon_complete_dashboard.py`)
    * AggregateAllowList
    * AggregateBlockList
    * AggregateDetections
    * AggregateDeviceCountCollection
    * AggregateEscalations
    * AggregateFCIncidents
    * AggregateRemediations
    * QueryAllowListFilter
    * QueryBlockListFilter
    * QueryDetectionIdsByFilter
    * GetDeviceCountCollectionQueriesByFilter
    * QueryEscalationsFilter
    * QueryIncidentIdsByFilter
    * QueryRemediationsFilter
    - Added unit tests (`test_falcon_complete_dashboard.py`)
+ Added: MalQuery API Service Class (`malquery.py`)
    + GetMalQueryQuotasV1
    + PostMalQueryFuzzySearchV1
    + GetMalQueryDownloadV1
    + GetMalQueryMetadataV1
    + GetMalQueryRequestV1
    + GetMalQueryEntitiesSamplesFetchV1
    + PostMalQueryEntitiesSamplesMultidownloadV1
    + PostMalQueryExactSearchV1
    + PostMalQueryHuntV1
    * Added unit tests (`test_malquery.py`)
+ Added: ML Exclusions API Service Class (`ml_exclusions.py`)
    * getMLExclusionsV1
    * createMLExclusionsV1
    * deleteMLExclusionsV1
    * updateMLExclusionsV1
    * queryMLExclusionsV1
    - Added unit tests (`test_ml_exclusions.py`)
+ Added: Overwatch Dashboard API Service Class (`overwatch_dashboard.py`)
    * AggregatesDetectionsGlobalCounts
    * AggregatesEventsCollections
    * AggregatesEvents
    * AggregatesIncidentsGlobalCounts
    * AggregatesOWEventsGlobalCounts
    - Added unit tests (`test_overwatch_dashboard.py`)
+ Added: Sensor Visibility Exclusions API Service Class (`sensor_visibility_exclusions.py`)
    * getSensorVisibilityExclusionsV1
    * createSVExclusionsV1
    * deleteSensorVisibilityExclusionsV1
    * updateSensorVisibilityExclusionsV1
    * querySensorVisibilityExclusionsV1
    - Added unit tests (`test_sensor_visibility_exclusions.py`)
## Other
+ Added: args_to_params function (`_util.py`) - Allows developers to specify parameter dictionary elements as function arguments
    ### Example
    ```python
    import json
    from falconpy.ml_exclusions import ML_Exclusions as FalconML
    falcon = FalconML(creds={"client_id": client_ID, "client_secret": client_secret})
    print(json.dumps(falcon.queryMLExclusionsV1(limit=10, offset=20, sort="value.asc"), indent=4))
    ```
    - Unrecognized parameter values are discarded
    - Initial testing in a limited number of Service Classes
# Version 0.4.6-spotlight-remediations-patch-1
## Added features and functionality
+ Added: Missing method to Spotlight_Vulnerabilities Service Class (`spotlight_vulnerabilities.py`)
    * getRemediations
    - Added unit test to existing test series (`test_spotlight_vulnerabilities.py`)
# Version 0.4.6
## Added features and functionality
+ Added: MSSP (Falcon Flight Control) Service Class
    * getChildren
    * getCIDGroupMembersBy
    * addCIDGroupMembers
    * deleteCIDGroupMembers
    * getCIDGroupById
    * createCIDGroups
    * deleteCIDGroups
    * updateCIDGroups
    * getRolesByID
    * addRole
    * deleteRoles
    * getUserGroupMembersByID
    * addUserGroupMembers
    * deleteUserGroupMembers
    * getUserGroupsByID
    * createUserGroup
    * deleteUserGroups
    * updateUserGroups
    * queryChildren
    * queryCIDGroupMembers
    * queryCIDGroups
    * queryRoles
    * queryUserGroupMembers
    * queryUserGroups
    - Added unit tests (`test_mssp.py`)

+ Added: Zero Trust Assessment Service Class
    * getAssessmentV1
    - Added unit tests (`test_zero_trust_assessment.py`)

## Issues resolved
+ Fixed KeyError when providing invalid credentials to a Service Class using Credential
  or Object authentication, Closes [#134](https://github.com/CrowdStrike/falconpy/issues/134)

## Other
+ Moved _endpoint constant library to a private submodule (No impact to existing usage)
    - Added payload parameter information to _endpoint constants
    - Adds service collection ID to endpoint lists
    - This prepares the package for new functionality planned for future releases
+ Added: `force_default` function - decorator function that forces default values for function arguments (`_util.py`)
    - Added: Helper function `get_default`
    - Refactored Uber class to leverage this new functionality
        * Unit tests refactored to cover new code paths (`test_uber_api_complete.py`)
    - Depending upon feedback, this updated pattern will be implemented within Service Classes to reduce overall function complexity
+ Linting
    > Developers: These patterns are being tested within the Uber Class for migration over to Service Classes in future versions
    - Reduced Uber class method complexity
        * Added: Helper function `calc_url_from_args` (`_util.py`)
        * Added: Helper function `_create_header_payload` (`api_complete.py`, Requires class internal variables)
    - Migrated Uber class variables to snake_case format
    - Removed unnecessarily complex lambdas
        * New class method: `valid_cred_format`, replaces previous lambda class attribute
        * New class method: `token_expired`, replaces previous lambda class attribute
    - Reduced overall number of instance attributes
    * Unit tests updated (`test_uber_api_complete.py`)
+ Minor unit test update to `test_cspm_registration.py`
+ Added `util/coverage.config`
    - Moved unit test coverage reporting over to configuration file for parameter management
+ Documentation updates

# Version 0.4.5
## Added features and functionality
+ Added: Custom Indicators of Attack (IOA) API Service Class (`custom_ioa.py`)
    * get_patterns
    * get_platformsMixin0
    * get_rule_groupsMixin0
    * create_rule_groupMixin0
    * delete_rule_groupsMixin0
    * update_rule_groupMixin0
    * get_rule_types
    * get_rules_get
    * get_rulesMixin0
    * create_rule
    * delete_rules
    * update_rules
    * validate
    * query_patterns
    * query_platformsMixin0
    * query_rule_groups_full
    * query_rule_groupsMixin0
    * query_rule_types
    * query_rulesMixin0
    - Added unit tests (`test_custom_ioa.py`)

+ Added: Falcon X Quick Scan API Service Class (`quick_scan.py`)
    * GetScansAggregates
    * GetScans
    * ScanSamples
    * QuerySubmissionsMixin0
    - Added unit tests (`test_quick_scan.py`)

+ Added: Uber class endpoints (`_endpoints.py`)
    * Falcon Complete Dashboard API
    * Falcon Overwatch Dashboard API
    * Falcon Flight Control API
## Issues resolved
+ Fixed unidiomatic type check in `_util.py` (_parse_id_list_)
+ Fixed potentially problematic default payload lists and dictionaries (Service Classes and Uber Class)
## Other
+ Added CHANGELOG.md
+ Documentation updates to reflect new service class and upcoming API additions
+ Minor comment updates
+ Adjusted GitHub actions to test operating systems as separate workflows
+ Minor GitHub workflow adjustments
+ Unit test updates
    - Cloud Connect AWS
    - CSPM Registration
    - Sensor Download

# Version 0.4.4
## Added features and functionality
+ Added: Sensor Download API Service Class (Contributor: @CalebSchwartz)
    * GetCombinedSensorInstallersByQuery
    * DownloadSensorInstallerById
    * GetSensorInstallersEntities
    * GetSensorInstallersCCIDByQuery
    * GetSensorInstallersByQuery
    - Added unit tests
## Issues resolved
+ Fixed: action_name parameter default bug. Resolved by setting a default value and overriding this value if action_name is present in the parameters dictionary, Closes #114. 
## Other
+ Documentation updated to reflect the new Sensor Download Service Class


# Version 0.4.3
## Added features and functionality
+ Added: Sample_Uploads service class (`sample_uploads.py`)
    * UploadSampleV3
    * GetSampleV3
    * DeleteSampleV3
    - Added: Sample_Uploads unit tests (`test_sample_uploads.py`)
+ Added: FalconDebug - Interactive Python3 debugger that provides a pre-defined API token.
## Issues resolved
+ Fixed: Issue with Uber class command method using the action_name variable instead of file_name variable for actions passing the file_name parameter.
+ Fixed: Issue with `setup.py` passing GitHub emoji text to the package description.
+ Fixed: Issue with Uber class unit testing not deleting uploaded files from Sample_Uploads API. (`test_uber_api_complete.py`)


# Version 0.4.2
## Added features and functionality
+ Added missing method: `hosts.py` - Added UpdateDeviceTags method to Hosts service class. (Contributor: @rewgord)
    - Unit test added to `test_hosts.py` to test device tagging functionality.
+ API Operation summaries added to the Uber class: `_endpoint.py` - This provides for upcoming functionality that will be announced in future updates.
+ New endpoints added to the Uber class: `_endpoint.py` 

> Deprecation Warning: Legacy API operation IDs that made use of the Python reserved characters "." and "-" have been deprecated. 
> New operation IDs have been generated for each that now aligns to the method names defined in the equivalent service class.

## Issues resolved
+ Added method validation to Uber class calls to the requests library. (HTTP 418 is sent when an invalid method is specified.)
## Other
+ Cleaned up `event_streams.py` class file to match new patterns.
+ Updated return type decorators for service_request and perform_request. (`_util.py`)
+ Updated return type decorators for GetArtifacts, GetReports and GetSampleV2. (`falconx_sandbox.py`)
+ Abstracted all remaining common error output code paths to a stand-alone generic method. (`_util.py`)


# Version 0.4.1
## Added features and functionality
+ New service class: cspm_registration.py - Provides the *CSPM_Registration* service class for handling Horizon registration in Azure and AWS.
    - Unit test added
+ Added methods: falconx_sandbox.py - Support for the following operations have been added to the *FalconX_Sandbox* service class.
    * QuerySampleV1
    * DeleteSampleV2
    * GetSampleV2
    * DeleteReport
    * GetReports
    - Unit test added
## Issues resolved
+ Bug fix: Resolved malformed validator in detects.py - UpdateDetectsByIdsV2
+ Bug fix: Added action_name parameter to operations that require the parameter. Closes #53.
  This issue impacted 6 service classes in total:
    - device_control_policies.py - *Device_Control_Policies* - performDeviceControlPoliciesAction
    - firewall_policies.py - *Firewall_Policies* - performFirewallPoliciesAction
    - host_group.py - *Host_Group* - performGroupAction
    - hosts.py - *Host* - PerformActionV2
    - prevention_policy.py - *Prevention_Policy* - performPreventionPoliciesAction
    - sensor_update_policy.py - *Sensor_Update_Policy* - performSensorUpdatePoliciesAction
   
    - This issue also impacted the Uber class, resulting in updates to the command method within the APIHarness class.

    - Unit tests modified

> Breaking Change: The action_name parameter does not currently accept unspecified values. This is resolved in the 0.4.4 version of the package.

## Other
+ Minor updates to `_endpoints.py` to reflect operation ID corrections for the CSPM registration API.
+ Abstracted common error output code paths to a stand-alone method within `_util.py`.


# Version 0.4.0
## Added features and functionality
+ Added additional HTTP status codes
+ Added parameter input validation handling
    - Additional validations are planned for all service classes. Currently only enabled in `cloud_connect_aws.py`. 
+ Added body payload input validation handling
    -  Additional validations are planned for all service classes. Currently only enabled in `cloud_connect_aws.py`.  
+ Added allowed HTTP method restrictions
+ Added ID list handling to API operations that require ID lists
    - Developers may now pass in a list of IDs or a comma-delimited string. 
+ Added status code response checks to authentication events
+ Instantiate Service classes without having to manage tokens
    - Pass in credentials (Now referred to as "credential authentication")
    - Pass in the entire auth object (Now referred to as "object authentication")
    > Please note: Passing a token into Service classes is still fully supported. This is now referred to as "legacy authentication".
+ Added automatic token refresh functionality to Service Class calls
    - Developers must make use of either credential or object authentication in order to leverage this functionality.
## Issues resolved
+ Added dynamic package metadata updates (Closes #14)
    - Generalized version control
        - New constant file: `_version.py`
+ Added user-agent string to HTTP headers. (Closes #57)
+ Resolved a bug with token deauthentication (Uber and Service classes)
+ Resolved a bug in Firewall_Management.update_rule_group
## Other
+ Abstracted calls to the requests library from all classes, reducing code segment size
    - New library: _util.py
    - New class: _service_class.py
    - New class: _result.py
    - All Service Classes refactored
+ Abstracted endpoint list from the Uber class to a standalone source file
    - New constant file: _endpoint.py
+ Linting / code cleanup
    - Added function input parameter datatype specifications (where possible)
    - Added function output datatype decorators
    - In order to reduce confusion, references to the `json` requests attribute are now always referred to as "body". 
    - References to the `data` requests attribute are still referred to as "data".
+ 100% unit test coverage
+ Internal documentation updates
