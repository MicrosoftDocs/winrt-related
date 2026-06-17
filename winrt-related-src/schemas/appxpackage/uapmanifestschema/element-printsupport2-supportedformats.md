---
title: printSupport2:SupportedFormats
description: Specifies the Page Description Language (PDL) formats supported by the virtual printer.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Applications, Application, Extensions, printSupport2:Extension, printSupport2:PrintSupportVirtualPrinter, printSupport2:SupportedFormats]
---

# printSupport2:SupportedFormats

Specifies the Page Description Language (PDL) formats supported by the virtual printer.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<printSupport2:Extension>`](element-printsupport2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<printSupport2:PrintSupportVirtualPrinter>`](element-printsupport2-printsupportvirtualprinter.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<printSupport2:SupportedFormats>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<printSupport2:Extension>`](element-printsupport2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<printSupport2:PrintSupportVirtualPrinter>`](element-printsupport2-printsupportvirtualprinter.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<printSupport2:SupportedFormats>`**  

## Syntax

```xml
<printSupport2:SupportedFormats>

  <!-- Child elements -->
  printSupport2:SupportedFormat{1,1000}

</printSupport2:SupportedFormats>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|  | Specifies a Page Description Language (PDL) format supported by the virtual printer. |  |  |  |
|  | Description |  |  |  |
|  | - |  |  |  |
|  | Specifies a virtual endpoint print queue to be installed with the app. |  |  |  |
|  | Value |  |  |  |
|  | -- |  |  |  |
|  | `http://schemas.microsoft.com/appx/manifest/printsupport/windows10/2` |  |  |  |
|  | <!-- TODO: Add minimum OS version --> |  |  |  |

## Child elements

| Child element | Description |
|-|-|
| [printSupport2:SupportedFormat](element-printsupport2-supportedformat.md) | Specifies a Page Description Language (PDL) format supported by the virtual printer. |

## Parent elements

| Parent element | Description |
|-|-|
| [printSupport2:PrintSupportVirtualPrinter](element-printsupport2-printsupportvirtualprinter.md) | Specifies a virtual endpoint print queue to be installed with the app. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/printsupport/windows10/2` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
