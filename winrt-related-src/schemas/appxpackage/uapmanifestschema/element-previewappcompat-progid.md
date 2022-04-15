---
title: previewappcompat:ProgId
description: A programmatic identifier (ProgID) that can be associated with a CLSID. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique.
ms.date: 03/14/2022

ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# previewappcompat:ProgId

A programmatic identifier (ProgID) that can be associated with a CLSID. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique.

## Element Hierarchy

[ <  Package  > ](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Applications > ](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Application > ](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < UAP10:Extension > ](element-uap10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < UAP10:Extension > ](element-uap10-protocol.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**< previewappcompat:ProgId >**

## Syntax
```syntax
<previewAppCompat:ProgId>
  An alphanumeric string that contains between 1 and 255 characters.

</previewAppCompat:ProgId>
```

### Key
`?` optional (zero or one)

## Attributes

None.

## Child Elements

None.

## Parent Elements
| Parent Element | Description |
|---------------|-------------|
| [UAP10:Protocol](element-uap10-protocol.md) | Sets parameters to define the protocol of the extensions. |

## Requirements
|   | Value |
|--|--|
| **previewappcompat** | `http://schemas.microsoft.com/appx/manifest/preview/windows10/msixappcompatsupport/3` |