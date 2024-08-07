# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opamp.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from opamp import anyvalue_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bopamp.proto\x12\x0bopamp.proto\x1a\x0e\x61nyvalue.proto\"\xbc\x06\n\rAgentToServer\x12!\n\x0cinstance_uid\x18\x01 \x01(\x0cR\x0binstanceUid\x12!\n\x0csequence_num\x18\x02 \x01(\x04R\x0bsequenceNum\x12J\n\x11\x61gent_description\x18\x03 \x01(\x0b\x32\x1d.opamp.proto.AgentDescriptionR\x10\x61gentDescription\x12\"\n\x0c\x63\x61pabilities\x18\x04 \x01(\x04R\x0c\x63\x61pabilities\x12\x34\n\x06health\x18\x05 \x01(\x0b\x32\x1c.opamp.proto.ComponentHealthR\x06health\x12G\n\x10\x65\x66\x66\x65\x63tive_config\x18\x06 \x01(\x0b\x32\x1c.opamp.proto.EffectiveConfigR\x0f\x65\x66\x66\x65\x63tiveConfig\x12Q\n\x14remote_config_status\x18\x07 \x01(\x0b\x32\x1f.opamp.proto.RemoteConfigStatusR\x12remoteConfigStatus\x12G\n\x10package_statuses\x18\x08 \x01(\x0b\x32\x1c.opamp.proto.PackageStatusesR\x0fpackageStatuses\x12G\n\x10\x61gent_disconnect\x18\t \x01(\x0b\x32\x1c.opamp.proto.AgentDisconnectR\x0f\x61gentDisconnect\x12\x14\n\x05\x66lags\x18\n \x01(\x04R\x05\x66lags\x12\x66\n\x1b\x63onnection_settings_request\x18\x0b \x01(\x0b\x32&.opamp.proto.ConnectionSettingsRequestR\x19\x63onnectionSettingsRequest\x12P\n\x13\x63ustom_capabilities\x18\x0c \x01(\x0b\x32\x1f.opamp.proto.CustomCapabilitiesR\x12\x63ustomCapabilities\x12\x41\n\x0e\x63ustom_message\x18\r \x01(\x0b\x32\x1a.opamp.proto.CustomMessageR\rcustomMessage\"\x11\n\x0f\x41gentDisconnect\"^\n\x19\x43onnectionSettingsRequest\x12\x41\n\x05opamp\x18\x01 \x01(\x0b\x32+.opamp.proto.OpAMPConnectionSettingsRequestR\x05opamp\"r\n\x1eOpAMPConnectionSettingsRequest\x12P\n\x13\x63\x65rtificate_request\x18\x01 \x01(\x0b\x32\x1f.opamp.proto.CertificateRequestR\x12\x63\x65rtificateRequest\"&\n\x12\x43\x65rtificateRequest\x12\x10\n\x03\x63sr\x18\x01 \x01(\x0cR\x03\x63sr\"\xc8\x05\n\rServerToAgent\x12!\n\x0cinstance_uid\x18\x01 \x01(\x0cR\x0binstanceUid\x12G\n\x0e\x65rror_response\x18\x02 \x01(\x0b\x32 .opamp.proto.ServerErrorResponseR\rerrorResponse\x12\x43\n\rremote_config\x18\x03 \x01(\x0b\x32\x1e.opamp.proto.AgentRemoteConfigR\x0cremoteConfig\x12V\n\x13\x63onnection_settings\x18\x04 \x01(\x0b\x32%.opamp.proto.ConnectionSettingsOffersR\x12\x63onnectionSettings\x12M\n\x12packages_available\x18\x05 \x01(\x0b\x32\x1e.opamp.proto.PackagesAvailableR\x11packagesAvailable\x12\x14\n\x05\x66lags\x18\x06 \x01(\x04R\x05\x66lags\x12\"\n\x0c\x63\x61pabilities\x18\x07 \x01(\x04R\x0c\x63\x61pabilities\x12S\n\x14\x61gent_identification\x18\x08 \x01(\x0b\x32 .opamp.proto.AgentIdentificationR\x13\x61gentIdentification\x12;\n\x07\x63ommand\x18\t \x01(\x0b\x32!.opamp.proto.ServerToAgentCommandR\x07\x63ommand\x12P\n\x13\x63ustom_capabilities\x18\n \x01(\x0b\x32\x1f.opamp.proto.CustomCapabilitiesR\x12\x63ustomCapabilities\x12\x41\n\x0e\x63ustom_message\x18\x0b \x01(\x0b\x32\x1a.opamp.proto.CustomMessageR\rcustomMessage\"\xbb\x01\n\x17OpAMPConnectionSettings\x12\x31\n\x14\x64\x65stination_endpoint\x18\x01 \x01(\tR\x13\x64\x65stinationEndpoint\x12.\n\x07headers\x18\x02 \x01(\x0b\x32\x14.opamp.proto.HeadersR\x07headers\x12=\n\x0b\x63\x65rtificate\x18\x03 \x01(\x0b\x32\x1b.opamp.proto.TLSCertificateR\x0b\x63\x65rtificate\"\xbf\x01\n\x1bTelemetryConnectionSettings\x12\x31\n\x14\x64\x65stination_endpoint\x18\x01 \x01(\tR\x13\x64\x65stinationEndpoint\x12.\n\x07headers\x18\x02 \x01(\x0b\x32\x14.opamp.proto.HeadersR\x07headers\x12=\n\x0b\x63\x65rtificate\x18\x03 \x01(\x0b\x32\x1b.opamp.proto.TLSCertificateR\x0b\x63\x65rtificate\"\xdd\x02\n\x17OtherConnectionSettings\x12\x31\n\x14\x64\x65stination_endpoint\x18\x01 \x01(\tR\x13\x64\x65stinationEndpoint\x12.\n\x07headers\x18\x02 \x01(\x0b\x32\x14.opamp.proto.HeadersR\x07headers\x12=\n\x0b\x63\x65rtificate\x18\x03 \x01(\x0b\x32\x1b.opamp.proto.TLSCertificateR\x0b\x63\x65rtificate\x12^\n\x0eother_settings\x18\x04 \x03(\x0b\x32\x37.opamp.proto.OtherConnectionSettings.OtherSettingsEntryR\rotherSettings\x1a@\n\x12OtherSettingsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"8\n\x07Headers\x12-\n\x07headers\x18\x01 \x03(\x0b\x32\x13.opamp.proto.HeaderR\x07headers\"0\n\x06Header\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"t\n\x0eTLSCertificate\x12\x1d\n\npublic_key\x18\x01 \x01(\x0cR\tpublicKey\x12\x1f\n\x0bprivate_key\x18\x02 \x01(\x0cR\nprivateKey\x12\"\n\rca_public_key\x18\x03 \x01(\x0cR\x0b\x63\x61PublicKey\"\x98\x04\n\x18\x43onnectionSettingsOffers\x12\x12\n\x04hash\x18\x01 \x01(\x0cR\x04hash\x12:\n\x05opamp\x18\x02 \x01(\x0b\x32$.opamp.proto.OpAMPConnectionSettingsR\x05opamp\x12I\n\x0bown_metrics\x18\x03 \x01(\x0b\x32(.opamp.proto.TelemetryConnectionSettingsR\nownMetrics\x12G\n\nown_traces\x18\x04 \x01(\x0b\x32(.opamp.proto.TelemetryConnectionSettingsR\townTraces\x12\x43\n\x08own_logs\x18\x05 \x01(\x0b\x32(.opamp.proto.TelemetryConnectionSettingsR\x07ownLogs\x12h\n\x11other_connections\x18\x06 \x03(\x0b\x32;.opamp.proto.ConnectionSettingsOffers.OtherConnectionsEntryR\x10otherConnections\x1ai\n\x15OtherConnectionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12:\n\x05value\x18\x02 \x01(\x0b\x32$.opamp.proto.OtherConnectionSettingsR\x05value:\x02\x38\x01\"\xe5\x01\n\x11PackagesAvailable\x12H\n\x08packages\x18\x01 \x03(\x0b\x32,.opamp.proto.PackagesAvailable.PackagesEntryR\x08packages\x12*\n\x11\x61ll_packages_hash\x18\x02 \x01(\x0cR\x0f\x61llPackagesHash\x1aZ\n\rPackagesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32\x1d.opamp.proto.PackageAvailableR\x05value:\x02\x38\x01\"\xa1\x01\n\x10PackageAvailable\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x18.opamp.proto.PackageTypeR\x04type\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x12\x31\n\x04\x66ile\x18\x03 \x01(\x0b\x32\x1d.opamp.proto.DownloadableFileR\x04\x66ile\x12\x12\n\x04hash\x18\x04 \x01(\x0cR\x04hash\"v\n\x10\x44ownloadableFile\x12!\n\x0c\x64ownload_url\x18\x01 \x01(\tR\x0b\x64ownloadUrl\x12!\n\x0c\x63ontent_hash\x18\x02 \x01(\x0cR\x0b\x63ontentHash\x12\x1c\n\tsignature\x18\x03 \x01(\x0cR\tsignature\"\xb8\x01\n\x13ServerErrorResponse\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32$.opamp.proto.ServerErrorResponseTypeR\x04type\x12#\n\rerror_message\x18\x02 \x01(\tR\x0c\x65rrorMessage\x12\x37\n\nretry_info\x18\x03 \x01(\x0b\x32\x16.opamp.proto.RetryInfoH\x00R\tretryInfoB\t\n\x07\x44\x65tails\"C\n\tRetryInfo\x12\x36\n\x17retry_after_nanoseconds\x18\x01 \x01(\x04R\x15retryAfterNanoseconds\"D\n\x14ServerToAgentCommand\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x18.opamp.proto.CommandTypeR\x04type\"\xb5\x01\n\x10\x41gentDescription\x12L\n\x16identifying_attributes\x18\x01 \x03(\x0b\x32\x15.opamp.proto.KeyValueR\x15identifyingAttributes\x12S\n\x1anon_identifying_attributes\x18\x02 \x03(\x0b\x32\x15.opamp.proto.KeyValueR\x18nonIdentifyingAttributes\"\x93\x03\n\x0f\x43omponentHealth\x12\x18\n\x07healthy\x18\x01 \x01(\x08R\x07healthy\x12/\n\x14start_time_unix_nano\x18\x02 \x01(\x06R\x11startTimeUnixNano\x12\x1d\n\nlast_error\x18\x03 \x01(\tR\tlastError\x12\x16\n\x06status\x18\x04 \x01(\tR\x06status\x12\x31\n\x15status_time_unix_nano\x18\x05 \x01(\x06R\x12statusTimeUnixNano\x12\x66\n\x14\x63omponent_health_map\x18\x06 \x03(\x0b\x32\x34.opamp.proto.ComponentHealth.ComponentHealthMapEntryR\x12\x63omponentHealthMap\x1a\x63\n\x17\x43omponentHealthMapEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32\x1c.opamp.proto.ComponentHealthR\x05value:\x02\x38\x01\"M\n\x0f\x45\x66\x66\x65\x63tiveConfig\x12:\n\nconfig_map\x18\x01 \x01(\x0b\x32\x1b.opamp.proto.AgentConfigMapR\tconfigMap\"\xab\x01\n\x12RemoteConfigStatus\x12\x35\n\x17last_remote_config_hash\x18\x01 \x01(\x0cR\x14lastRemoteConfigHash\x12\x39\n\x06status\x18\x02 \x01(\x0e\x32!.opamp.proto.RemoteConfigStatusesR\x06status\x12#\n\rerror_message\x18\x03 \x01(\tR\x0c\x65rrorMessage\"\xa1\x02\n\x0fPackageStatuses\x12\x46\n\x08packages\x18\x01 \x03(\x0b\x32*.opamp.proto.PackageStatuses.PackagesEntryR\x08packages\x12H\n!server_provided_all_packages_hash\x18\x02 \x01(\x0cR\x1dserverProvidedAllPackagesHash\x12#\n\rerror_message\x18\x03 \x01(\tR\x0c\x65rrorMessage\x1aW\n\rPackagesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32\x1a.opamp.proto.PackageStatusR\x05value:\x02\x38\x01\"\xb8\x02\n\rPackageStatus\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12*\n\x11\x61gent_has_version\x18\x02 \x01(\tR\x0f\x61gentHasVersion\x12$\n\x0e\x61gent_has_hash\x18\x03 \x01(\x0cR\x0c\x61gentHasHash\x12\x34\n\x16server_offered_version\x18\x04 \x01(\tR\x14serverOfferedVersion\x12.\n\x13server_offered_hash\x18\x05 \x01(\x0cR\x11serverOfferedHash\x12\x36\n\x06status\x18\x06 \x01(\x0e\x32\x1e.opamp.proto.PackageStatusEnumR\x06status\x12#\n\rerror_message\x18\x07 \x01(\tR\x0c\x65rrorMessage\"?\n\x13\x41gentIdentification\x12(\n\x10new_instance_uid\x18\x01 \x01(\x0cR\x0enewInstanceUid\"i\n\x11\x41gentRemoteConfig\x12\x33\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x1b.opamp.proto.AgentConfigMapR\x06\x63onfig\x12\x1f\n\x0b\x63onfig_hash\x18\x02 \x01(\x0cR\nconfigHash\"\xb7\x01\n\x0e\x41gentConfigMap\x12I\n\nconfig_map\x18\x01 \x03(\x0b\x32*.opamp.proto.AgentConfigMap.ConfigMapEntryR\tconfigMap\x1aZ\n\x0e\x43onfigMapEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32\x1c.opamp.proto.AgentConfigFileR\x05value:\x02\x38\x01\"H\n\x0f\x41gentConfigFile\x12\x12\n\x04\x62ody\x18\x01 \x01(\x0cR\x04\x62ody\x12!\n\x0c\x63ontent_type\x18\x02 \x01(\tR\x0b\x63ontentType\"8\n\x12\x43ustomCapabilities\x12\"\n\x0c\x63\x61pabilities\x18\x01 \x03(\tR\x0c\x63\x61pabilities\"W\n\rCustomMessage\x12\x1e\n\ncapability\x18\x01 \x01(\tR\ncapability\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12\x12\n\x04\x64\x61ta\x18\x03 \x01(\x0cR\x04\x64\x61ta*c\n\x12\x41gentToServerFlags\x12\"\n\x1e\x41gentToServerFlags_Unspecified\x10\x00\x12)\n%AgentToServerFlags_RequestInstanceUid\x10\x01*`\n\x12ServerToAgentFlags\x12\"\n\x1eServerToAgentFlags_Unspecified\x10\x00\x12&\n\"ServerToAgentFlags_ReportFullState\x10\x01*\xf7\x02\n\x12ServerCapabilities\x12\"\n\x1eServerCapabilities_Unspecified\x10\x00\x12$\n ServerCapabilities_AcceptsStatus\x10\x01\x12)\n%ServerCapabilities_OffersRemoteConfig\x10\x02\x12-\n)ServerCapabilities_AcceptsEffectiveConfig\x10\x04\x12%\n!ServerCapabilities_OffersPackages\x10\x08\x12,\n(ServerCapabilities_AcceptsPackagesStatus\x10\x10\x12/\n+ServerCapabilities_OffersConnectionSettings\x10 \x12\x37\n3ServerCapabilities_AcceptsConnectionSettingsRequest\x10@*>\n\x0bPackageType\x12\x18\n\x14PackageType_TopLevel\x10\x00\x12\x15\n\x11PackageType_Addon\x10\x01*\x8f\x01\n\x17ServerErrorResponseType\x12#\n\x1fServerErrorResponseType_Unknown\x10\x00\x12&\n\"ServerErrorResponseType_BadRequest\x10\x01\x12\'\n#ServerErrorResponseType_Unavailable\x10\x02*&\n\x0b\x43ommandType\x12\x17\n\x13\x43ommandType_Restart\x10\x00*\xef\x04\n\x11\x41gentCapabilities\x12!\n\x1d\x41gentCapabilities_Unspecified\x10\x00\x12#\n\x1f\x41gentCapabilities_ReportsStatus\x10\x01\x12)\n%AgentCapabilities_AcceptsRemoteConfig\x10\x02\x12,\n(AgentCapabilities_ReportsEffectiveConfig\x10\x04\x12%\n!AgentCapabilities_AcceptsPackages\x10\x08\x12,\n(AgentCapabilities_ReportsPackageStatuses\x10\x10\x12&\n\"AgentCapabilities_ReportsOwnTraces\x10 \x12\'\n#AgentCapabilities_ReportsOwnMetrics\x10@\x12%\n AgentCapabilities_ReportsOwnLogs\x10\x80\x01\x12\x35\n0AgentCapabilities_AcceptsOpAMPConnectionSettings\x10\x80\x02\x12\x35\n0AgentCapabilities_AcceptsOtherConnectionSettings\x10\x80\x04\x12,\n\'AgentCapabilities_AcceptsRestartCommand\x10\x80\x08\x12$\n\x1f\x41gentCapabilities_ReportsHealth\x10\x80\x10\x12*\n%AgentCapabilities_ReportsRemoteConfig\x10\x80 *\x9c\x01\n\x14RemoteConfigStatuses\x12\x1e\n\x1aRemoteConfigStatuses_UNSET\x10\x00\x12 \n\x1cRemoteConfigStatuses_APPLIED\x10\x01\x12!\n\x1dRemoteConfigStatuses_APPLYING\x10\x02\x12\x1f\n\x1bRemoteConfigStatuses_FAILED\x10\x03*\xa1\x01\n\x11PackageStatusEnum\x12\x1f\n\x1bPackageStatusEnum_Installed\x10\x00\x12$\n PackageStatusEnum_InstallPending\x10\x01\x12 \n\x1cPackageStatusEnum_Installing\x10\x02\x12#\n\x1fPackageStatusEnum_InstallFailed\x10\x03\x42\x9d\x01\n\x0f\x63om.opamp.protoB\nOpampProtoP\x01Z1github.com/odigos-io/odigos/opampserver/protobufs\xa2\x02\x03OPX\xaa\x02\x0bOpamp.Proto\xca\x02\x0bOpamp\\Proto\xe2\x02\x17Opamp\\Proto\\GPBMetadata\xea\x02\x0cOpamp::Protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'opamp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.opamp.protoB\nOpampProtoP\001Z1github.com/odigos-io/odigos/opampserver/protobufs\242\002\003OPX\252\002\013Opamp.Proto\312\002\013Opamp\\Proto\342\002\027Opamp\\Proto\\GPBMetadata\352\002\014Opamp::Proto'
  _globals['_OTHERCONNECTIONSETTINGS_OTHERSETTINGSENTRY']._options = None
  _globals['_OTHERCONNECTIONSETTINGS_OTHERSETTINGSENTRY']._serialized_options = b'8\001'
  _globals['_CONNECTIONSETTINGSOFFERS_OTHERCONNECTIONSENTRY']._options = None
  _globals['_CONNECTIONSETTINGSOFFERS_OTHERCONNECTIONSENTRY']._serialized_options = b'8\001'
  _globals['_PACKAGESAVAILABLE_PACKAGESENTRY']._options = None
  _globals['_PACKAGESAVAILABLE_PACKAGESENTRY']._serialized_options = b'8\001'
  _globals['_COMPONENTHEALTH_COMPONENTHEALTHMAPENTRY']._options = None
  _globals['_COMPONENTHEALTH_COMPONENTHEALTHMAPENTRY']._serialized_options = b'8\001'
  _globals['_PACKAGESTATUSES_PACKAGESENTRY']._options = None
  _globals['_PACKAGESTATUSES_PACKAGESENTRY']._serialized_options = b'8\001'
  _globals['_AGENTCONFIGMAP_CONFIGMAPENTRY']._options = None
  _globals['_AGENTCONFIGMAP_CONFIGMAPENTRY']._serialized_options = b'8\001'
  _globals['_AGENTTOSERVERFLAGS']._serialized_start=6233
  _globals['_AGENTTOSERVERFLAGS']._serialized_end=6332
  _globals['_SERVERTOAGENTFLAGS']._serialized_start=6334
  _globals['_SERVERTOAGENTFLAGS']._serialized_end=6430
  _globals['_SERVERCAPABILITIES']._serialized_start=6433
  _globals['_SERVERCAPABILITIES']._serialized_end=6808
  _globals['_PACKAGETYPE']._serialized_start=6810
  _globals['_PACKAGETYPE']._serialized_end=6872
  _globals['_SERVERERRORRESPONSETYPE']._serialized_start=6875
  _globals['_SERVERERRORRESPONSETYPE']._serialized_end=7018
  _globals['_COMMANDTYPE']._serialized_start=7020
  _globals['_COMMANDTYPE']._serialized_end=7058
  _globals['_AGENTCAPABILITIES']._serialized_start=7061
  _globals['_AGENTCAPABILITIES']._serialized_end=7684
  _globals['_REMOTECONFIGSTATUSES']._serialized_start=7687
  _globals['_REMOTECONFIGSTATUSES']._serialized_end=7843
  _globals['_PACKAGESTATUSENUM']._serialized_start=7846
  _globals['_PACKAGESTATUSENUM']._serialized_end=8007
  _globals['_AGENTTOSERVER']._serialized_start=45
  _globals['_AGENTTOSERVER']._serialized_end=873
  _globals['_AGENTDISCONNECT']._serialized_start=875
  _globals['_AGENTDISCONNECT']._serialized_end=892
  _globals['_CONNECTIONSETTINGSREQUEST']._serialized_start=894
  _globals['_CONNECTIONSETTINGSREQUEST']._serialized_end=988
  _globals['_OPAMPCONNECTIONSETTINGSREQUEST']._serialized_start=990
  _globals['_OPAMPCONNECTIONSETTINGSREQUEST']._serialized_end=1104
  _globals['_CERTIFICATEREQUEST']._serialized_start=1106
  _globals['_CERTIFICATEREQUEST']._serialized_end=1144
  _globals['_SERVERTOAGENT']._serialized_start=1147
  _globals['_SERVERTOAGENT']._serialized_end=1859
  _globals['_OPAMPCONNECTIONSETTINGS']._serialized_start=1862
  _globals['_OPAMPCONNECTIONSETTINGS']._serialized_end=2049
  _globals['_TELEMETRYCONNECTIONSETTINGS']._serialized_start=2052
  _globals['_TELEMETRYCONNECTIONSETTINGS']._serialized_end=2243
  _globals['_OTHERCONNECTIONSETTINGS']._serialized_start=2246
  _globals['_OTHERCONNECTIONSETTINGS']._serialized_end=2595
  _globals['_OTHERCONNECTIONSETTINGS_OTHERSETTINGSENTRY']._serialized_start=2531
  _globals['_OTHERCONNECTIONSETTINGS_OTHERSETTINGSENTRY']._serialized_end=2595
  _globals['_HEADERS']._serialized_start=2597
  _globals['_HEADERS']._serialized_end=2653
  _globals['_HEADER']._serialized_start=2655
  _globals['_HEADER']._serialized_end=2703
  _globals['_TLSCERTIFICATE']._serialized_start=2705
  _globals['_TLSCERTIFICATE']._serialized_end=2821
  _globals['_CONNECTIONSETTINGSOFFERS']._serialized_start=2824
  _globals['_CONNECTIONSETTINGSOFFERS']._serialized_end=3360
  _globals['_CONNECTIONSETTINGSOFFERS_OTHERCONNECTIONSENTRY']._serialized_start=3255
  _globals['_CONNECTIONSETTINGSOFFERS_OTHERCONNECTIONSENTRY']._serialized_end=3360
  _globals['_PACKAGESAVAILABLE']._serialized_start=3363
  _globals['_PACKAGESAVAILABLE']._serialized_end=3592
  _globals['_PACKAGESAVAILABLE_PACKAGESENTRY']._serialized_start=3502
  _globals['_PACKAGESAVAILABLE_PACKAGESENTRY']._serialized_end=3592
  _globals['_PACKAGEAVAILABLE']._serialized_start=3595
  _globals['_PACKAGEAVAILABLE']._serialized_end=3756
  _globals['_DOWNLOADABLEFILE']._serialized_start=3758
  _globals['_DOWNLOADABLEFILE']._serialized_end=3876
  _globals['_SERVERERRORRESPONSE']._serialized_start=3879
  _globals['_SERVERERRORRESPONSE']._serialized_end=4063
  _globals['_RETRYINFO']._serialized_start=4065
  _globals['_RETRYINFO']._serialized_end=4132
  _globals['_SERVERTOAGENTCOMMAND']._serialized_start=4134
  _globals['_SERVERTOAGENTCOMMAND']._serialized_end=4202
  _globals['_AGENTDESCRIPTION']._serialized_start=4205
  _globals['_AGENTDESCRIPTION']._serialized_end=4386
  _globals['_COMPONENTHEALTH']._serialized_start=4389
  _globals['_COMPONENTHEALTH']._serialized_end=4792
  _globals['_COMPONENTHEALTH_COMPONENTHEALTHMAPENTRY']._serialized_start=4693
  _globals['_COMPONENTHEALTH_COMPONENTHEALTHMAPENTRY']._serialized_end=4792
  _globals['_EFFECTIVECONFIG']._serialized_start=4794
  _globals['_EFFECTIVECONFIG']._serialized_end=4871
  _globals['_REMOTECONFIGSTATUS']._serialized_start=4874
  _globals['_REMOTECONFIGSTATUS']._serialized_end=5045
  _globals['_PACKAGESTATUSES']._serialized_start=5048
  _globals['_PACKAGESTATUSES']._serialized_end=5337
  _globals['_PACKAGESTATUSES_PACKAGESENTRY']._serialized_start=5250
  _globals['_PACKAGESTATUSES_PACKAGESENTRY']._serialized_end=5337
  _globals['_PACKAGESTATUS']._serialized_start=5340
  _globals['_PACKAGESTATUS']._serialized_end=5652
  _globals['_AGENTIDENTIFICATION']._serialized_start=5654
  _globals['_AGENTIDENTIFICATION']._serialized_end=5717
  _globals['_AGENTREMOTECONFIG']._serialized_start=5719
  _globals['_AGENTREMOTECONFIG']._serialized_end=5824
  _globals['_AGENTCONFIGMAP']._serialized_start=5827
  _globals['_AGENTCONFIGMAP']._serialized_end=6010
  _globals['_AGENTCONFIGMAP_CONFIGMAPENTRY']._serialized_start=5920
  _globals['_AGENTCONFIGMAP_CONFIGMAPENTRY']._serialized_end=6010
  _globals['_AGENTCONFIGFILE']._serialized_start=6012
  _globals['_AGENTCONFIGFILE']._serialized_end=6084
  _globals['_CUSTOMCAPABILITIES']._serialized_start=6086
  _globals['_CUSTOMCAPABILITIES']._serialized_end=6142
  _globals['_CUSTOMMESSAGE']._serialized_start=6144
  _globals['_CUSTOMMESSAGE']._serialized_end=6231
# @@protoc_insertion_point(module_scope)
