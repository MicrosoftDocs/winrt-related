---
title: Schema for Mobile Broadband
description: The Mobile Broadband Schema are used by the Windows.Networking.NetworkOperators namespace provided in the Windows Runtime environment to enable a UWP app to provision a mobile broadband enabled device on a mobile broadband network, query subscriber data usage information, or query the results of the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
ms.assetid: b9f29690-466f-4b5f-bd4e-d4bf07260ca1
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
ms.prod: windows
ms.technology: winrt-reference
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
<td><p>[Base schema](base/schema-root.md)</p></td>
<td><p>The [Base](base/schema-root.md) schema defines elements that are used to describe basic data types used throughout the Mobile Broadband schema. It defines only simple and complex types.</p></td>
</tr>
<tr class="even">
<td><p>[CarrierControlSchema schema](carriercontrolschema/schema-root.md)</p></td>
<td><p>The [CarrierControlSchema](carriercontrolschema/schema-root.md) schema defines elements that are used to create the provisioning file in a call to [<strong>ProvisionFromXmlDocumentAsync</strong>](https://msdn.microsoft.com/library/windows/apps/br207400) and describe all of the settings required to authenticate and provision a subscriber's account on a Mobile Network Operator's (MNO) network. All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControl/v1. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="odd">
<td><p>[CarrierControlSchema_v2 schema](carriercontrolschema-v2/schema-root.md)</p></td>
<td><p>The [CarrierControlSchema_v2](carriercontrolschema-v2/schema-root.md) schema defines additional elements that are used to create the provisioning file in a call to [<strong>ProvisionFromXmlDocumentAsync</strong>](https://msdn.microsoft.com/library/windows/apps/br207400) and describe additional settings required to authenticate and provision a subscriber's account on a Mobile Network Operator's (MNO) network. All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControl/v2. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="even">
<td><p>[CarrierControlSignatureSchema schema](carriercontrolsignatureschema/schema-root.md)</p></td>
<td><p>The [CarrierControlSignatureSchema](carriercontrolsignatureschema/schema-root.md) schema defines elements that are used to describe the signature appended to the provisioning file. It is based on the [XML DSIG](http://www.w3.org/TR/xmldsig-core/) specification with only minor deviations that are explicitly described below. All of the elements are in the namespace http://www.w3.org/2000/09/xmldsig#. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="odd">
<td><p>[DUSM schema](dusm/schema-root.md)</p></td>
<td><p>The [Data Usage Subscription Management (DUSM)](dusm/schema-root.md) schema defines elements that are used to describe cost information for a subscriber's connection to a metered network. All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControl/DUSM/v1. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="even">
<td><p>[HotspotProfile schema](hotspotprofile/schema-root.md)</p></td>
<td><p>The [HotspotProfile](hotspotprofile/schema-root.md) schema defines elements that are used to describe login credentials for Wi-Fi hotspots that use the Wireless Internet Service Provider roaming (WISPr) protocol. All of the elements are in the namespace http://www.microsoft.com/networking/WLAN/HotspotProfile/v1. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="odd">
<td><p>[MBAE schema](mbae/schema-root.md)</p></td>
<td><p>The [Mobile Broadband Account Experience (MBAE)](mbae/schema-root.md) schema defines elements that are used by mobile network operators and retail partners to deliver valued added services to customers. All of the elements are in the namespace http://schemas.microsoft.com/windows/2010/12/DeviceMetadata/MobileBroadbandInfo. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="even">
<td><p>[Plans schema](plans/schema-root.md)</p></td>
<td><p>The [Plans](plans/schema-root.md) schema defines elements that are used to describe a subscriber's data plan on a Mobile Network Operator (MNO). All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControl/Plans/v1. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="odd">
<td><p>[ResultsSchema schema](resultsschema/schema-root.md)</p></td>
<td><p>The [ResultsSchema](resultsschema/schema-root.md) schema defines elements that are returned from a call to [<strong>ProvisionResultsXml</strong>](https://msdn.microsoft.com/library/windows/apps/br212048) and describe the results of the last provisioning attempt. All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControlResults/v1. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="even">
<td><p>[ResultsSchema_v2 schema](resultsschema-v2/schema-root.md)</p></td>
<td><p>The [ResultsSchema_v2](resultsschema-v2/schema-root.md) schema defines additional elements that are returned from a call to [<strong>ProvisionResultsXml</strong>](https://msdn.microsoft.com/library/windows/apps/br212048) and describe the results of the last provisioning attempt. All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControlResults/v2. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
<tr class="odd">
<td><p>[WLAN schema](wlan/schema-root.md)</p></td>
<td><p>The [WLAN](wlan/schema-root.md) schema defines elements that are used to describe a subscriber's connection to a Wireless Local Area Network (WLAN).</p></td>
</tr>
<tr class="even">
<td><p>[WLAN_v2 schema](wlan-v2/schema-root.md)</p></td>
<td><p>The [WLAN_v2](wlan-v2/schema-root.md) schema defines additional elements that are used to describe a subscriber's connection to a Wireless Local Area Network (WLAN).</p></td>
</tr>
<tr class="odd">
<td><p>[WWAN Schema](wwan/schema-root.md)</p></td>
<td><p>The [WWAN](wwan/schema-root.md) schema defines elements that are used to describe a subscriber's connection to a Wireless Wide Area Network (WWAN). All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControl/WWAN/v1. Not all elements are in every profile, as some elements are optional.</p></td>
</tr>
</tbody>
</table>

 

## Developer audience


The Mobile Broadband Schema are designed for use by Javascript/C++/C#/Visual Basic developers interested in enabling the use of Mobile Broadband for network communications in their UWP app.

## Related topics


[**Windows.Networking.NetworkOperators**](https://msdn.microsoft.com/library/windows/apps/br241148)

 

 




