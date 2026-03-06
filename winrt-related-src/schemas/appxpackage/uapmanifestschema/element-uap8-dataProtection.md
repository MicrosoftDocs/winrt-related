---
title: uap8:DataProtection
description: Settings to configure data encryption.
ms.date: 03/14/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
no-loc: [Package, Extensions, uap8:Extension, uap8:DataProtection]
---

# uap8:DataProtection

Settings to configure data encryption.

## Element hierarchy

**[`<Package>`](element-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap8:Extension>`](element-uap8-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap8:DataProtection>`**  

## Syntax

```xml
<uap8:DataProtection
  UserDataAvailability = 'A string that can have one of the following values: "always", "afterFirstUnlock", "whileUnlocked", or "applicationManaged".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **UserDataAvailability** | Specifies how the application should make user data available. | A string that can have one of the following values: *always*, *afterFirstUnlock*, *whileUnlocked*, or *applicationManaged*. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap8:Extension](element-uap8-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **uap8** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/8` |
| **Minimum OS Version** | Windows 10 version 1903 (Build 18362) |
