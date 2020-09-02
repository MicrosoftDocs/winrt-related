---

ms.assetid: 5babaec2-35fc-4eac-8f82-317a7d3ce5c9
title: ContentGroupMap
description: Specifies the layout of the final content group map, AppxContentGroupMap.xml.

ms.date: 03/29/2017
ms.topic: article


keywords: windows 10, uwp, streaming install, content group, map, final content group, automatic content group
---

# ContentGroupMap

## Description
Specifies the layout of the final content group map, AppxContentGroupMap.xml.

## Element Hierarchy
<b>&lt;ContentGroupMap&gt;</b>

## Syntax
```syntax
<ContentGroupMap IgnorableNamespaces? = String type. >
  <!-- Child elements -->
   Automatic
</ContentGroupMap>
```

## Key

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| IgnorableNamespaces | Declares namespaces used in the manifest that should be ignored. Ignored namespace elements are not validated and should be considered untrusted. Multiple namespaces are specified with a space between each namespace. | String type. | No |

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [Automatic](element-final-automatic.md) | The automatic content group. |

## Remarks
It's recommended to start with authoring the source content group map (SourceAppxContentGroupMap.xml) and converting that into the final content group map (AppxContentGroupMap.xml) via Visual Studio or MakeAppx.exe. For more information, see [Create and convert a source content group map](/windows/uwp/packaging/create-cgm).

## Examples

## Requirements
|          |         |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2016/contentgroupmap` |