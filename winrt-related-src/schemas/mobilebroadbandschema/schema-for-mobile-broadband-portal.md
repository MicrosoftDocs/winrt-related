---
title: Schema for Mobile Broadband
description: The Mobile Broadband Schema are used by the Windows.Networking.NetworkOperators namespace provided in the Windows Runtime environment to enable a UWP app to provision a mobile broadband enabled device on a mobile broadband network, query subscriber data usage information, or query the results of the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
ms.assetid: b9f29690-466f-4b5f-bd4e-d4bf07260ca1

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Schema for Mobile Broadband


## Purpose


The Mobile Broadband Schema are used by the [**Windows.Networking.NetworkOperators**](/uwp/api/Windows.Networking.NetworkOperators) namespace provided in the Windows Runtime environment to enable a UWP app to provision a mobile broadband enabled device on a mobile broadband network, query subscriber data usage information, or query the results of the last provisioning attempt.

The Mobile Broadband Schema define subscriber and network configuration parameters. They contain the subscriber preferences for a connection as well as subscriber data usage information.

The Mobile Broadband Schema strictly enforces the order of the nodes. Nodes used by the [**Windows.Networking.NetworkOperators**](/uwp/api/Windows.Networking.NetworkOperators) namespace must adhere to the Mobile Broadband Schema and appear in the order prescribed in the schema definition.

## In this section

|  Topic  |  Description  |
|---------|---------------|
| [Base schema](base/schema-root.md) | Defines elements that are used to describe basic data types used throughout the Mobile Broadband schema. It defines only simple and complex types. |
| [CarrierControlSchema schema](carriercontrolschema/schema-root.md) | Defines elements that are used to create the provisioning file in a call to [ProvisionFromXmlDocumentAsync](/uwp/api/Windows.Networking.NetworkOperators.ProvisioningAgent) and describe all of the settings required to authenticate and provision a subscriber's account on a Mobile Network Operator's (MNO) network. All of the elements are in the namespace `http://www.microsoft.com/networking/CarrierControl/v1`. Not all elements are in every profile, as some elements are optional. |
| [CarrierControlSchema_v2 schema](carriercontrolschema-v2/schema-root.md) | Defines additional elements that are used to create the provisioning file in a call to [ProvisionFromXmlDocumentAsync](/uwp/api/Windows.Networking.NetworkOperators.ProvisioningAgent) and describe additional settings required to authenticate and provision a subscriber's account on a Mobile Network Operator's (MNO) network. All of the elements are in the namespace `http://www.microsoft.com/networking/CarrierControl/v2`. Not all elements are in every profile, as some elements are optional. |
| [CarrierControlSignatureSchema schema](carriercontrolsignatureschema/schema-root.md) | Defines elements that are used to describe the signature appended to the provisioning file. It is based on the [XML DSIG](https://www.w3.org/TR/xmldsig-core/) specification with only minor deviations that are explicitly described below. All of the elements are in the namespace `http://www.w3.org/2000/09/xmldsig#`. Not all elements are in every profile, as some elements are optional. |
| [DUSM schema](dusm/schema-root.md) | Defines elements that are used to describe cost information for a subscriber's connection to a metered network. All of the elements are in the namespace `http://www.microsoft.com/networking/CarrierControl/DUSM/v1`. Not all elements are in every profile, as some elements are optional.  |
| [HotspotProfile schema](hotspotprofile/schema-root.md) | Defines elements that are used to describe login credentials for Wi-Fi hotspots that use the Wireless Internet Service Provider roaming (WISPr) protocol. All of the elements are in the namespace `http://www.microsoft.com/networking/WLAN/HotspotProfile/v1`. Not all elements are in every profile, as some elements are optional. |
| [MBAE schema](mbae/schema-root.md) | Defines elements that are used by mobile network operators and retail partners to deliver valued added services to customers. All of the elements are in the namespace `http://schemas.microsoft.com/windows/2010/12/DeviceMetadata/MobileBroadbandInfo`. Not all elements are in every profile, as some elements are optional. |
| [Plans schema](plans/schema-root.md) | Defines elements that are used to describe a subscriber's data plan on a Mobile Network Operator (MNO). All of the elements are in the namespace `http://www.microsoft.com/networking/CarrierControl/Plans/v1`. Not all elements are in every profile, as some elements are optional. |
| [ResultsSchema schema](resultsschema/schema-root.md) | Defines elements that are returned from a call to [ProvisionResultsXml](/uwp/api/Windows.Networking.NetworkOperators.ProvisionFromXmlDocumentResults) and describe the results of the last provisioning attempt. All of the elements are in the namespace `http://www.microsoft.com/networking/CarrierControlResults/v1`. Not all elements are in every profile, as some elements are optional. |
| [ResultsSchema_v2 schema](resultsschema-v2/schema-root.md) | Defines additional elements that are returned from a call to [ProvisionResultsXml](/uwp/api/Windows.Networking.NetworkOperators.ProvisionFromXmlDocumentResults) and describe the results of the last provisioning attempt. All of the elements are in the namespace `http://www.microsoft.com/networking/CarrierControlResults/v2`. Not all elements are in every profile, as some elements are optional. |
| [WLAN schema](wlan/schema-root.md) | Defines elements that are used to describe a subscriber's connection to a Wireless Local Area Network (WLAN). |
| [WLAN_v2 schema](wlan-v2/schema-root.md) | Defines additional elements that are used to describe a subscriber's connection to a Wireless Local Area Network (WLAN). |
| [WWAN schema](wwan/schema-root.md) | Defines elements that are used to describe a subscriber's connection to a Wireless Wide Area Network (WWAN). All of the elements are in the namespace `http://www.microsoft.com/networking/CarrierControl/WWAN/v1`.` Not all elements are in every profile, as some elements are optional. |

## Developer audience

The Mobile Broadband Schema are designed for use by Javascript/C++/C#/Visual Basic developers interested in enabling the use of Mobile Broadband for network communications in their UWP app.

## Related topics


[**Windows.Networking.NetworkOperators**](/uwp/api/Windows.Networking.NetworkOperators)

 

 