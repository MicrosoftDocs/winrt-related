---
title: printSupport2:PrintSupportVirtualPrinter
description: Specifies a virtual endpoint print queue to be installed with the app.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Applications, Application, Extensions, printSupport2:Extension, printSupport2:PrintSupportVirtualPrinter]
---

# printSupport2:PrintSupportVirtualPrinter

Specifies a virtual endpoint print queue to be installed with the app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<printSupport2:Extension>`](element-printsupport2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<printSupport2:PrintSupportVirtualPrinter>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<printSupport2:Extension>`](element-printsupport2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<printSupport2:PrintSupportVirtualPrinter>`**  

## Syntax

```xml
<printSupport2:PrintSupportVirtualPrinter
  DisplayName = 'A required string between 1 and 256 characters in length. This string is localizable.'
  PdcFile = 'A required string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  PdrFile = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  PreferredInputFormat = 'An optional string that can have one of the following values: "application/oxps", or "application/postscript".'
  PrinterUri = 'An optional string between 1 and 2084 characters in length in the form of a valid URI.'
  OutputFileTypes = 'An optional value. <!-- TODO: Add description for printSupport2:ST_OutputFileTypes -->' >

  <!-- Child elements -->
  printSupport2:SupportedFormats?

</printSupport2:PrintSupportVirtualPrinter>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** | The display name of the virtual printer. | A string between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **PdcFile** | The Print Device Capabilities (PDC) file for the virtual printer that defines printer capabilities and any custom features, options, or parameters. The path must point to a resource file within the application package. The file must use the PDC XML format. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |
| **PdrFile** | The Print Device Resources (PDR) file for the virtual printer. If provided, the path must point to a resource file within the application package. An app should specify a PDR file if it wants to localize custom print preferences. If a PDR file is not specified, resource localization for print preferences will be performed by the print system. | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |
| **PreferredInputFormat** | The preferred input PDL format for the virtual printer. Windows Print System will generate this format before giving PDL data to the virtual printer for all printing paths. | An optional string that can have one of the following values: *application/oxps*, *application/postscript*. | No |  |
| **PrinterUri** | A unique URI that can be used by a Print Support Application (PSA) to identify the printer. If an app installs multiple virtual printers, this value can be used to differentiate the printers. This is the value returned by calls to [IppPrintDevice.PrinterUri Property](/uwp/api/windows.devices.printers.ippprintdevice.printeruri). If a URI is not specified, Windows will assign an arbitrary unique URI to the printer. | An optional string between 1 and 2084 characters in length in the form of a valid URI. | No |  |
| **OutputFileTypes** | Specifies the output file types supported by the virtual printer. When an app specifies a value for this field, the Windows Print System will create a printer queue that is marked as a file printer, the **Save As** dialog will be shown to the user when the app starts printing, and in that dialog, the allowed extensions will be limited to the specified values. If a virtual printer does not want file print behavior, then this attribute should not be included in the manifest. | An optional value. <!-- TODO: Add data type for printSupport2:ST_OutputFileTypes --> | No |  |

## Child elements

| Child element | Description |
|-|-|
| [printSupport2:SupportedFormats](element-printsupport2-supportedformats.md) | Specifies the Page Description Language (PDL) formats supported by the virtual printer. |

## Parent elements

| Parent element | Description |
|-|-|
| [printSupport2:Extension](element-printsupport2-extension.md) | Declares an extensibility point for a Print Support App, adding support for virtual printers. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/printsupport/windows10/2` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
