---
title: Schema for Mobile Broadband
description: The Mobile Broadband Schema are used by the Windows.Networking.NetworkOperators namespace provided in the Windows Runtime environment to enable a UWP app to provision a mobile broadband enabled device on a mobile broadband network, query subscriber data usage information, or query the results of the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
ms.assetid: b9f29690-466f-4b5f-bd4e-d4bf07260ca1
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Schema for Mobile Broadband


## Purpose


The Mobile Broadband Schema are used by the [**Windows.Networking.NetworkOperators**](https://msdn.microsoft.com/library/windows/apps/br241148) namespace provided in the Windows Runtime environment to enable a UWP app to provision a mobile broadband enabled device on a mobile broadband network, query subscriber data usage information, or query the results of the last provisioning attempt.

The Mobile Broadband Schema define subscriber and network configuration parameters. They contain the subscriber preferences for a connection as well as subscriber data usage information.

The Mobile Broadband Schema strictly enforces the order of the nodes. Nodes used by the [**Windows.Networking.NetworkOperators**](https://msdn.microsoft.com/library/windows/apps/br241148) namespace must adhere to the Mobile Broadband Schema and appear in the order prescribed in the schema definition.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="base/schema-root.md">Base schema</a> </p></td>
<td><p>The <a href="base/schema-root.md">Base</a>  schema defines elements that are used to describe basic data types used throughout the Mobile Broadband schema. It defines only simple and complex types.</p></td>
</tr>
<tr class="even">
<td><p><a href="carriercontrolschema/schema-root.md">CarrierControlSchema schema</a> </p></td>
<td><p>The <a href="carriercontrolschema/schema-root.md">CarrierControlSchema</a>  schema defines elements that are used to create the provisioning file in a call to <a href="https://msdn.microsoft.com/library/windows/apps/br207400"><strong>ProvisionFromXmlDocumentAsync</strong></a> and describe all of the settings required to authenticate and provision a subscriber's account on a Mobile Network Operator's (MNO) network. All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControl/v1. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="odd">
<td><p><a href="carriercontrolschema-v2/schema-root.md">CarrierControlSchema_v2 schema</a> </p></td>
<td><p>The <a href="carriercontrolschema-v2/schema-root.md">CarrierControlSchema_v2</a>  schema defines additional elements that are used to create the provisioning file in a call to <a href="https://msdn.microsoft.com/library/windows/apps/br207400"><strong>ProvisionFromXmlDocumentAsync</strong></a> and describe additional settings required to authenticate and provision a subscriber's account on a Mobile Network Operator's (MNO) network. All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControl/v2. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="even">
<td><p><a href="carriercontrolsignatureschema/schema-root.md">CarrierControlSignatureSchema schema</a> </p></td>
<td><p>The <a href="carriercontrolsignatureschema/schema-root.md">CarrierControlSignatureSchema</a>  schema defines elements that are used to describe the signature appended to the provisioning file. It is based on the <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> specification with only minor deviations that are explicitly described below. All of the elements are in the namespace http://www.w3.org/2000/09/xmldsig#. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="odd">
<td><p><a href="dusm/schema-root.md">DUSM schema</a> </p></td>
<td><p>The <a href="dusm/schema-root.md">Data Usage Subscription Management (DUSM)</a>  schema defines elements that are used to describe cost information for a subscriber's connection to a metered network. All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControl/DUSM/v1. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="even">
<td><p><a href="hotspotprofile/schema-root.md">HotspotProfile schema</a> </p></td>
<td><p>The <a href="hotspotprofile/schema-root.md">HotspotProfile</a>  schema defines elements that are used to describe login credentials for Wi-Fi hotspots that use the Wireless Internet Service Provider roaming (WISPr) protocol. All of the elements are in the namespace http://www.microsoft.com/networking/WLAN/HotspotProfile/v1. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="odd">
<td><p><a href="mbae/schema-root.md">MBAE schema</a> </p></td>
<td><p>The <a href="mbae/schema-root.md">Mobile Broadband Account Experience (MBAE)</a>  schema defines elements that are used by mobile network operators and retail partners to deliver valued added services to customers. All of the elements are in the namespace http://schemas.microsoft.com/windows/2010/12/DeviceMetadata/MobileBroadbandInfo. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="even">
<td><p><a href="plans/schema-root.md">Plans schema</a> </p></td>
<td><p>The <a href="plans/schema-root.md">Plans</a>  schema defines elements that are used to describe a subscriber's data plan on a Mobile Network Operator (MNO). All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControl/Plans/v1. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="odd">
<td><p><a href="resultsschema/schema-root.md">ResultsSchema schema</a> </p></td>
<td><p>The <a href="resultsschema/schema-root.md">ResultsSchema</a>  schema defines elements that are returned from a call to <a href="https://msdn.microsoft.com/library/windows/apps/br212048"><strong>ProvisionResultsXml</strong></a> and describe the results of the last provisioning attempt. All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControlResults/v1. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="even">
<td><p><a href="resultsschema-v2/schema-root.md">ResultsSchema_v2 schema</a> </p></td>
<td><p>The <a href="resultsschema-v2/schema-root.md">ResultsSchema_v2</a>  schema defines additional elements that are returned from a call to <a href="https://msdn.microsoft.com/library/windows/apps/br212048"><strong>ProvisionResultsXml</strong></a> and describe the results of the last provisioning attempt. All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControlResults/v2. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="odd">
<td><p><a href="wlan/schema-root.md">WLAN schema</a> </p></td>
<td><p>The <a href="wlan/schema-root.md">WLAN</a>  schema defines elements that are used to describe a subscriber's connection to a Wireless Local Area Network (WLAN).</p></td>
</tr>
<tr class="even">
<td><p><a href="wlan-v2/schema-root.md">WLAN_v2 schema</a> </p></td>
<td><p>The <a href="wlan-v2/schema-root.md">WLAN_v2</a>  schema defines additional elements that are used to describe a subscriber's connection to a Wireless Local Area Network (WLAN).</p></td>
</tr>
<tr class="odd">
<td><p><a href="wwan/schema-root.md">WWAN Schema</a> </p></td>
<td><p>The <a href="wwan/schema-root.md">WWAN</a>  schema defines elements that are used to describe a subscriber's connection to a Wireless Wide Area Network (WWAN). All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControl/WWAN/v1. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
</tbody>
</table>

 

## Developer audience


The Mobile Broadband Schema are designed for use by Javascript/C++/C#/Visual Basic developers interested in enabling the use of Mobile Broadband for network communications in their UWP app.

## Related topics


[**Windows.Networking.NetworkOperators**](https://msdn.microsoft.com/library/windows/apps/br241148)

 

 




