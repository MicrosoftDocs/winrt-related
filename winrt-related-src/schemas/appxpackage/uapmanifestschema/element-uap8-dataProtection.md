---
title: uap8:DataProtection
description: Settings to configure data encryption.
ms.date: 03/14/2022

ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap8:DataProtection

Settings to configure data encryption.

## Element Hierarchy (Application Extensions)
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap8-extension.md">&lt;uap8:Extension&gt;</a></dt>
<dd><b>&lt;uap8:dataProtection&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap8:DataProtection UserDataAvailability = One of the following string values: "always", "afterFirstUnlock", "whileUnlocked", "applicationManaged">

</uap8:DataProtection>
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| UserDataAvailability | Specifies how the application should make user data available. | A string value that can be one of the following: "always", "afterFirstUnlock", "whileUnlocked", or "applicationManaged" | Yes |



## Requirements
|   | Value |
|--|--|
| **uap8** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/8` |