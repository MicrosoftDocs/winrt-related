---
Description: The package family name of the app that will be invoked to handle the WISPr authentication.
Search.Product: eADQiWindows 10XVcnh
title: ExtensionId
ms.assetid: 2b5d31a8-4896-4890-82f7-6caa3ac92318

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# ExtensionId


The package family name of the app that will be invoked to handle the WISPr authentication.

## Element hierarchy

<dl>
<dt><a href="element-hotspotprofile.md">&lt;HotspotProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extauth.md">&lt;ExtAuth&gt;</a></dt>
<dd><b>&lt;ExtensionId&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<ExtensionId>

  token

</ExtensionId>
```

## Attributes and Elements


### Attributes

None.

### Child Elements

None.

### Parent Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parent Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-extauth.md">ExtAuth</a> </td>
<td><p>Contains the parameters for handling WISPr authentication through an app (rather than specifying a static user name and password via <a href="element-basicauth.md"><strong>BasicAuth</strong></a> ).</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The app must register for the corresponding system event using [**Windows.ApplicationModel.Background.NetworkOperatorHotspotAuthenticationTrigger**](https://msdn.microsoft.com/library/windows/apps/hh779764). One or more profiles referencing an app must be provisioned (see [**Windows.Networking.NetworkOperators.ProvisioningAgent**](https://msdn.microsoft.com/library/windows/apps/br207397)) before the app can register for this event.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/WLAN/HotspotProfile/v1` |

 

 



