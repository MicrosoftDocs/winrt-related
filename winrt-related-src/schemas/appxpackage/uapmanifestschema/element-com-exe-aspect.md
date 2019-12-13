---

ms.assetid: 92d6f9b0-dc05-47d6-bd5f-8d0667325e6f
title: com:Aspect (in ExeServer/Class)
description: Specifies the desired data or view aspect of the object when drawing or getting data.

ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---

# com:Aspect (in ExeServer/Class)

## Description
Specifies the desired data or view aspect of the object when drawing or getting data.

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
<dt><a href="element-com-extension.md">&lt;com:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-comserver.md">&lt;com:ComServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-exeserver.md">&lt;com:ExeServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-exeserver-class.md">&lt;com:Class&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-exe-miscstatus.md">&lt;com:MiscStatus&gt;</a></dt>
<dd><b>&lt;com:Aspect&gt;</b></dd>
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
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com:Aspect  
    Type = A string as one of the enumeration values: Content, Thumbnail, Icon, or DocPrint.
    OleMiscFlag = An integer value in the range of 0-4194303. >
</com:Aspect>
```

## Key

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Type      | The string value for the view aspect of the object. | A string as one of the enumeration values: Content, Thumbnail, Icon, or DocPrint. | Yes |
| OleMiscFlag | The integer value for the view aspect of the object. | An integer value in the range of 0-4194303. | Yes |

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