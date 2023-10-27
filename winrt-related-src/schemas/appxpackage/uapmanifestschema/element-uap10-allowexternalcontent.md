---
description: Enables your package manifest to reference content outside the package, in a specific location on disk, for packages with external location.
title: uap10:AllowExternalContent
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/22/2020
---

# uap10:AllowExternalContent

Enables your package manifest to reference content outside the package, in a specific location on disk. See [Grant package identity by packaging with external location](/windows/apps/desktop/modernize/grant-identity-to-nonpackaged-apps).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap10:AllowExternalContent\>**

## Syntax

```xml
<uap10:AllowExternalContent>
  A boolean value.
</uap10:AllowExternalContents>
```

### Key

`?`   optional (zero or one)

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package behaves. |

## Remarks

The **uap10:AllowExternalContent** element contains a boolean value. For more information about the use of the element, see [Grant package identity by packaging with external location](/windows/apps/desktop/modernize/grant-identity-to-nonpackaged-apps).

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| Minimum OS Version | Windows 10 version 2004 (Build 19041) |
