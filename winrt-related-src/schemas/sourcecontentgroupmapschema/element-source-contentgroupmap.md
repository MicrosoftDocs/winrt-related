---
author: laurenhughes
ms.assetid: 60660150-a566-438c-ac07-4470f570c2c1 
title: ContentGroupMap
description: Specifies the layout of the source content group map, SourceAppxContentGroupMap.xml.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, streaming install, content group, map, final content group, automatic content group
---

# ContentGroupMap

## -description
Specifies the layout of the source content group map, SourceAppxContentGroupMap.xml.

## -element-hierarchy
<b>&lt;ContentGroupMap&gt;</b>

## -syntax
```syntax
<ContentGroupMap IgnorableNamespaces? = String type. >
  <!-- Child elements -->
 ( Required, 
   Automatic )
</ContentGroupMap>
```

## -key
`?`    optional (zero or one)

## -attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| IgnorableNamespaces | Declares namespaces used in the manifest that should be ignored. Ignored namespace elements are not validated and should be considered untrusted. Multiple namespaces are specified with a space between each namespace. | String type. | No |

## -child-elements

| Child Element | Description |
|---------------|-------------|
| [Required](element-source-required.md) | The required content group. |
| [Automatic](element-source-automatic.md) | The automatic content group(s). |

## -remarks
The source content group map (SourceAppxContentGroupMap.xml) is a content group map authored by the developer. After SourceAppxContentGroupMap.xml is complete, it is converted into the final content group map (AppxContentGroupMap.xml) which will be packaged with the app to enable the app to be streaming installed. For more information on converting your content group map, see TODO. 

It's possible to simply author AppxContentGroupMap.xml and skip converting the SourceAppxContentGroupMap.xml. By skipping this step, you won't be able to use wildcards for files and you'll miss additional validations.

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
<td><p>http://schemas.microsoft.com/appx/2016/sourcecontentgroupmap</p></td>
</tr>
</tbody>
</table>