---
title:  printSupport2:SupportedFormat
description: Specifies a Page Description Language (PDL) format supported by the virtual printer.
keywords: windows 10, uwp, schema, manifest, extension
ms.date: 01/09/2023
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, printSupport2:Extension, printSupport2:PrintSupportVirtualPrinter, printSupport2:SupportedFormats, printSupport2:SupportedFormats]
---

# printSupport2:SupportedFormat

Specifies a Page Description Language (PDL) format supported by the virtual printer.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<printSupport2:Extension>`](element-printsupport2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<printSupport2:PrintSupportVirtualPrinter>`](element-printsupport2-printsupportvirtualprinter.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<printSupport2:SupportedFormats>`](element-printsupport2-supportedformats.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<printSupport2:SupportedFormats>`**  

## Syntax

```xml
<printSupport2:SupportedFormat
  Type = 'A MIME type string specifying the PDL format.'
  MaxVersion = 'The maximum version of the PDL format that the virtual printer can handle.'/>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Type** | A MIME type string specifying the PDL format. | A MIME type string. | Yes |  |
| **MaxVersion** | The maximum version of the PDL format that the virtual printer can handle. | A string in the format *"MajorVersion.MinorVersion" where *MajorVersion* and *MinorVersion* include only digits. If letter characters are included in the version strings, the value is invalid and will be ignored. | No |  |


### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [printsupport2:SupportedFormats](element-printsupport2-supportedformats.md) | Specifies the Page Description Language (PDL) formats supported by the virtual printer. |

### Remarks

For information about developing Print Support Apps, see the [Print support app design guide](/windows-hardware/drivers/devapps/print-support-app-design-guide).

### Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/printsupport/windows10/2` |