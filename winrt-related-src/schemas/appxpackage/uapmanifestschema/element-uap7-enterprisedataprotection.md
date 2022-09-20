---
title: uap7:EnterpriseDataProtection
description: When declared in an app, this ensures that all files it creates and clipboard/dragged items are encrypted.
ms.date: 10/03/2018
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap7:EnterpriseDataProtection

Declares that the app is safe for auto-encryption and allows it to be managed without device enrollment via Windows Information Protection policy.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap7:Extension\>](element-uap7-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap7:EnterpriseDataProtection\>**

## Syntax

```xml
<uap7:EnterpriseDataProtection
  ProtectionMode = 'A string that can have one of the following values: "auto" or "default".' />
```

## Attrbutes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ProtectionMode** | The mode of data protection. | A string that can have one of the following values: *auto* or *default*. | Yes |  |

### Child elements

None

### Parent elements

| Parent element | Description |
|-|-|
| [uap7:Extension](element-uap7-extension.md) | Declares an extensibility point for the package. |

## Remarks

Use this extension only if the app is exclusively for work, and/or you provide a mechanism to restore any non-work personal data the app modifies. All files that the app creates or modifies will be encrypted on behalf of the managing organization, and become inaccessible after a selective wipe occurs, when the protection policy is removed from the device. (To safely handle both work and personal data when managed with Windows Information Protection use the enterpriseDataPolicy capability instead.)

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
