---
author: laurenhughes
ms.assetid: ae4a725d-10f9-4e03-a579-c3db2d859a9f
title: com:Extension (Windows 10)
description: Provides functionality to expose COM registrations to clients outside of the app package.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, schema, manifest, com
---


# com:Extension (Windows 10)

## Description
Provides functionality to expose COM registrations to clients outside of the app package.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd><b>&lt;com:Extension&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<com:Extension Category = "windows.comServer" | "windows.comInterface" >

  <!-- Child elements -->
  ( com:ComServer
  | com:ComInterface )
</com:Extension>
```

## Key

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| **Category** | The type of app extensibility point. | This attribute can have one of the following values: <ul><li>windows.comServer</li><li>windows.comExtension</li></ul>| Yes |


## Child Elements

| Child Element         | Description |
|-----------------------|-------------|
| [com:ComServer](element-com-cominterface.md) | Declares a package extension point of type **windows.comServer**. |
| [com:ComInterface](element-com-comserver.md) | Declares a package extension point of type **windows.comInterface**. |

## Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [Extensions (type: CT_ApplicationExtensions)](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Remarks

## Examples

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/com/windows10</p></td>
</tr>
</tbody>
</table>