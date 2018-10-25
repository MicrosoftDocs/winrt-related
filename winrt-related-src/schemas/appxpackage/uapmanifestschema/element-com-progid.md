---
author: laurenhughes
ms.assetid: be322b98-2ab7-4a7e-9135-3051b3b00a75
title: com:ProgId
description: A programmatic identifier (ProgID) that can be associated with a CLSID.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---


# com:ProgId

## Description
A programmatic identifier (ProgID) that can be associated with a CLSID. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique.

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
<dd><b>&lt;com:ProgId&gt;</b></dd>
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
<com:ProgId 
    Id = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1
    Clsid? = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    CurrentVersion? = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1 >
</com:ProgId>
```

## Key
`?`   optional (zero or more)

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Id | The ID of the ProgID. | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1 | Yes |
| Clsid | Associates a ProgID with a CLSID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |
| CurrentVersion | The version of the ProgID. | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1 | No |

## Remarks
The **Clsid** attribute must reference the **Id** attribute of an ExeServer class, SurrogateServer class, or TreatAsClass registration within the same [ComServer](element-com-comserver.md) extension.

For more information on the ProgID, see [&lt;ProgID&gt; Key](https://msdn.microsoft.com/library/windows/desktop/dd542719.aspx).

> [!NOTE]
> Clsid and CurrentVersion are mutually exclusive, but at least one must be provided.

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