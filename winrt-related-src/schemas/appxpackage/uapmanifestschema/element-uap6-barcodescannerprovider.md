---
title: uap6:BarcodeScannerProvider
description: Used for enabling the support of a barcode scanner.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, uap6:Extension, uap6:BarcodeScannerProvider]
---

# uap6:BarcodeScannerProvider

Used for enabling the support of a barcode scanner.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap6:Extension>`](element-uap6-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap6:BarcodeScannerProvider>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap6:Extension>`](element-uap6-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap6:BarcodeScannerProvider>`**  

## Syntax

```xml
<uap6:BarcodeScannerProvider
  DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.'
  SupportsVideoPreview = 'An optional boolean value.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** | The barcode scanner provider display name. | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |
| **SupportsVideoPreview** | Specify true or false to indicate whether video preview is supported. | An optional boolean value. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap6:Extension](element-uap6-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/6` |
| **Minimum OS Version** | Windows 10 version 1803 (Build 17134) |

## Remarks

If the *SupportsVideoPreview* attribute is true, indicating that the provider supports video preview, a *windows.barcodeScannerPreviewProvider* extension must also be specified in the manifest.

## Examples

<!-- Author content goes here -->
