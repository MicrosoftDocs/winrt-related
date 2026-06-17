---
title: uap7:EnterpriseDataProtection
description: When declared in an app, this ensures that all files it creates and clipboard/dragged items are encrypted.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, uap7:Extension, uap7:EnterpriseDataProtection]
---

# uap7:EnterpriseDataProtection

Declares that the app is safe for auto-encryption and allows it to be managed without device enrollment via Windows Information Protection policy.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap7:Extension>`](element-uap7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap7:EnterpriseDataProtection>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap7:Extension>`](element-uap7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap7:EnterpriseDataProtection>`**  

## Syntax

```xml
<uap7:EnterpriseDataProtection
  ProtectionMode = 'A required string that can have one of the following values: "auto", or "default".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ProtectionMode** | The mode of data protection. | A string that can have one of the following values: *auto*, *default*. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap7:Extension](element-uap7-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
| **Minimum OS Version** | Windows 10 version 1809 (Build 17763) |

## Remarks

Use this extension only if the app is exclusively for work, and/or you provide a mechanism to restore any non-work personal data the app modifies. All files that the app creates or modifies will be encrypted on behalf of the managing organization, and become inaccessible after a selective wipe occurs, when the protection policy is removed from the device. (To safely handle both work and personal data when managed with Windows Information Protection use the enterpriseDataPolicy capability instead.)

## Examples

<!-- Author content goes here -->