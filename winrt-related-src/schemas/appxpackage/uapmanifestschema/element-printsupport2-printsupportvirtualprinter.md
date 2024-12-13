---
title:  printSupport2:PrintSupportVirtualPrinter
description: Specifies a virtual endpoint print queue to be installed with the app..
keywords: windows 10, uwp, schema, manifest, extension
ms.date: 01/09/2023
ms.topic: reference
---

# printSupport2:PrintSupportVirtualPrinter

Specifies a virtual endpoint print queue to be installed with the app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<printSupport2:Extension\>](element-printsupport2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<printSupport2:PrintSupportVirtualPrinter\>**

## Syntax

```xml
<printSupport2:PrintSupportVirtualPrinter 
  DisplayName = 'TBD".'
  PdcFile = 'TBD".'
  PdrFile = 'TBD".'
  PreferredInputFormat = 'TBD".'
  PrinterUri = 'TBD".'
  OutputFileTypes = 'TBD".'
>

  <!-- Child elements -->
  SupportedFormats
</printSupport2:PrintSupportVirtualPrinter>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** | The display name of the birtual printer. | 'A string with a value between 1 and 256 characters in length. This string is localizable.' | Yes |  |
| **PdcFile** | The Print Device Capabilities (PDC) file for the virtual printer that defines printer capabilities and any custom features, options, or parameters. The path must point to a resource file within the application package. The file must use the PDC XML format. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |
| **PdrFile** | The Print Device Resources (PDR) file for the virtual printer. If provided, the path must point to a resource file within the application package. An app should specify a PDR file if it wants to localize custom print preferences. If a PDR file is not specified, resource localization for print preferences will be performed by the print system. |  A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **PreferredInputFormat** | The preferred input PDL format for the virtual printer. Windows Print System will generate this format before giving PDL data to the virtual printer for all printing paths. | A string that can have one of the following values: *application/oxps*, *application/postscript*. | No |  |
| **PrinterUri** | A unique URI that can be used by a Print Support Application (PSA) to identify the printer. If an app installs multiple virtual printers, this value can be used to differentiate the printers. This is the value returned by calls to [IppPrintDevice.PrinterUri Property](/uwp/api/windows.devices.printers.ippprintdevice.printeruri). If a URI is not specified, Windows will assign an arbitrary unique URI to the printer.  | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **OutputFileTypes** | Specifies the output file types supported by the virtual printer. When an app specifies a value for this field, the Windows Print System will create a printer queue that is marked as a file printer, the **Save As** dialog will be shown to the user when the app starts printing, and in that dialog, the allowed extensions will be limited to the specified values. If a virtual printer does not want file print behavior, then this attribute should not be included in the manifest. | A string containing a comma-delimited list of file extensions. For example, *"pdf,pwgr,ps"*.  | No |  |


### Child elements

| Child element | Description |
|-|-|
| [SupportedFormats](element-printsupport2-supportedformats.md) | Specifies the Page Description Language (PDL) formats supported by the virtual printer. |

### Parent elements

| Parent element | Description |
|-|-|
| [printsupport2:Extension](element-printsupport2-extension.md) | Declares an extensibility point for a Print Support App, adding support for virtual printers. |

### Remarks

For information about developing Print Support Apps, see the [Print support app design guide](/windows-hardware/drivers/devapps/print-support-app-design-guide).

### Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/printsupport/windows10/2` |