---
author: laurenhughes
title: desktop3:InvokeAction
description: Contains content and device information for invoking an AutoPlay action.
ms.author: lahugh
ms.date: 10/10/2017
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop3:InvokeAction

## Description
Contains content and device information for invoking an AutoPlay action.

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
<dd>
<dl>
<dt><a href="element-desktop3-extension.md">&lt;desktop3:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop3-AutoPlayHandler.md">&lt;desktop3:AutoPlayHandler&gt;</a></dt>
<dd><b>&lt;desktop3:InvokeAction&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<desktop3:InvokeAction ActionDisplayName   = A string between 1 and 256 characters in length.
                       ProviderDisplayName = A string between 1 and 256 characters in length.
                       DefaultIcon?        = A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, %, ", |, ?, or *. >

  <!-- Child elements -->
  ( desktop3:Content{0,1000},
    desktop3:Device{0,1000} )

</desktop3:InvokeAction>
```

### Key
`{}`   specific range of occurrences

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| ActionDisplayName | A string that represents the action that users can take with a device that they connect to a PC (For example: "Import files", or "Play video"). | A string between 1 and 256 characters in length. | Yes |
| ProviderDisplayName | A string that represents your app or service (For example: "Contoso video player"). | A string between 1 and 256 characters in length. | Yes |
| DefaultIcon | A path to either an .ico file or a resource in a binary file for the default icon.  | A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, %, ", |, ?, or *. | No |



## Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop3:Content](element-desktop3-content.md) | Defines the content information of an AutoPlayHandler. |  
| [desktop3:Device](element-desktop3-device.md) | Defines the device information of an AutoPlayHandler. | 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/desktop/windows10/3</p></td>
</tr>
</tbody>
</table>