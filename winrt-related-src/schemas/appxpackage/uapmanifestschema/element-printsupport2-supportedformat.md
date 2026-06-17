---
title: printSupport2:SupportedFormat
description: Specifies a Page Description Language (PDL) format supported by the virtual printer.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Applications, Application, Extensions, printSupport2:Extension, printSupport2:PrintSupportVirtualPrinter, printSupport2:SupportedFormats, printSupport2:SupportedFormat]
---

# printSupport2:SupportedFormat

Specifies a Page Description Language (PDL) format supported by the virtual printer.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<printSupport2:Extension>`](element-printsupport2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<printSupport2:PrintSupportVirtualPrinter>`](element-printsupport2-printsupportvirtualprinter.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<printSupport2:SupportedFormats>`](element-printsupport2-supportedformats.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<printSupport2:SupportedFormat>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<printSupport2:Extension>`](element-printsupport2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<printSupport2:PrintSupportVirtualPrinter>`](element-printsupport2-printsupportvirtualprinter.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<printSupport2:SupportedFormats>`](element-printsupport2-supportedformats.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<printSupport2:SupportedFormat>`**  

## Syntax

```xml
<printSupport2:SupportedFormat
  Type = 'A required value. <!-- TODO: Add description for printSupport2:ST_MimeType -->'
  MaxVersion = 'An optional value. <!-- TODO: Add description for printSupport2:ST_MaxVersion -->' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Type** | A MIME type string specifying the PDL format. | A value. <!-- TODO: Add data type for printSupport2:ST_MimeType --> | Yes |  |
| **MaxVersion** | The maximum version of the PDL format that the virtual printer can handle. | An optional value. <!-- TODO: Add data type for printSupport2:ST_MaxVersion --> | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [printSupport2:SupportedFormats](element-printsupport2-supportedformats.md) | Specifies the Page Description Language (PDL) formats supported by the virtual printer. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/printsupport/windows10/2` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
