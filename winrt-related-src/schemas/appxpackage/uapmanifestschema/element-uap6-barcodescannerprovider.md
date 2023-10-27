---
title: uap6:BarcodeScannerProvider
description: Used for enabling the support of a barcode scanner.
ms.date: 04/10/2018
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap6:BarcodeScannerProvider

Used for enabling the support of a barcode scanner.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap6:Extension\>](element-uap6-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap6:BarcodeScannerProvider\>**

## Syntax

```xml
<uap6:BarcodeScannerProvider
  DisplayName = 'A string with a value between 1 and 256 characters in length.'
  SupportsVideoPreview = 'A boolean value.' >
```

## Attrbutes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** | The barcode scanner provider display name. | A string with a value between 1 and 256 characters in length. | No |  |
| **SupportsVideoPreview** | Specify true or false to indicate whether video preview is supported. | A boolean value. | No |  |

### Child elements

None

### Parent elements

| Parent element | Description |
|-|-|
| [uap6:Extension](element-uap6-extension.md) | Declares an extensibility point for the app. |

## Remarks

If the *SupportsVideoPreview* attribute is true, indicating that the provider supports video preview, a *windows.barcodeScannerPreviewProvider* extension must also be specified in the manifest.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/6` |
| Minimum OS Version | Windows 10 version 1803 (Build 17134) |
