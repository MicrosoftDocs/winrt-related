---
title: com3:ProgId
description: A programmatic identifier (ProgID) that can be associated with a CLSID.
ms.date: 04/04/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com3:ProgId

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
<dt><a href="element-com2-extension.md">&lt;com2:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com2-comserver.md">&lt;com2:ComServer&gt;</a></dt>
<dd><b>&lt;com3:ProgId&gt;</b></dd>
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
<com3:ProgId 
    Id = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1
    Clsid? = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    CurrentVersion? = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1 >
</com3:ProgId>
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

## Requirements
|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/3` |