---
title: desktop10:IconHandler
description: Enables an IconHandler for a file type association.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop10:IconHandler

## Description
Enables an IconHandler for a file type association.


## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop10-extension.md">&lt;desktop10:Extension&gt;</a></dt>
<dd><strong>&lt;desktop10:IconHandler&gt;</strong></dd>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<desktop10:IconHandler Clsid = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. >
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Clsid | The ID for activating the COM class. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |

## Remarks
A `<desktop10:IconHandler>` element can only exist under a `<FileTypeAssociation>` element that is defined with an `<Application>` element that has: EntryPoint="windows.FullTrustApplication".


## Requirements

|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |