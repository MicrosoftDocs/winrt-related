---
author: laurenhughes
ms.assetid: 5babaec2-35fc-4eac-8f82-317a7d3ce5c9
title: ContentGroupMap
description: Specifies the layout of the final content group map, AppxContentGroupMap.xml.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, streaming install, content group, map, final content group, automatic content group
---

# ContentGroupMap

## -description
Specifies the layout of the final content group map, AppxContentGroupMap.xml.

## -element-hierarchy
<b>&lt;ContentGroupMap&gt;</b>

## -syntax
```syntax
<ContentGroupMap IgnorableNamespaces? = String type. >
  <!-- Child elements -->
   Automatic
</ContentGroupMap>
```

## -key

## -attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| IgnorableNamespaces | Declares namespaces used in the manifest that should be ignored. Ignored namespace elements are not validated and should be considered untrusted. Multiple namespaces are specified with a space between each namespace. | String type. | No |

## -child-elements

| Child Element | Description |
|---------------|-------------|
| [Automatic](element-final-automatic.md) | The automatic content group. |

## -remarks
It's recommended to start with authoring the source content group map (SourceAppxContentGroupMap.xml) and converting that into the final content group map (AppxContentGroupMap.xml) via Visual Studio or MakeAppx.exe. For more information, see TODO.

## -examples

## -requirements
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2016/contentgroupmap</p></td>
</tr>
</tbody>
</table>