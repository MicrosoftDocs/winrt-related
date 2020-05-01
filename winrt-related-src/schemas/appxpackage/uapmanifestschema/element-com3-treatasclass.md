---
title: com3:TreatAsClass
description: A registration that corresponds to a CLSID registration with the TreatAs subkey.
ms.date: 04/04/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com3:TreatAsClass

## Description

A registration that corresponds to a CLSID registration with the TreatAs subkey.

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
<dd><b>&lt;com3:TreatAsClass&gt;</b></dd>
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
<com3:TreatAsClass 
    Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    DisplayName? = A string between 1 and 256 characters in length. This string is localizable.    
    TreatAs = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. >
</com3:TreatAsClass>
```

## Key
`?`   optional (zero or more)

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Id | Corresponds to the CLSID of the COM class object. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |
| DisplayName | An optional string representing the default value of the CLSID key. | A string between 1 and 256 characters in length. This string is localizable. | No |
| TreatAs | Specifies the CLSID of a class that can emulate the current class. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |

## Requirements
|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/3` |