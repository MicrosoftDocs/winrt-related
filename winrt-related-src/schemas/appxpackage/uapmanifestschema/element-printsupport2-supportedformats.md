---
title:  printSupport2:SupportedFormats
description: Specifies the Page Description Language (PDL) formats supported by the virtual printer.
keywords: windows 10, uwp, schema, manifest, extension
ms.date: 01/09/2023
ms.topic: reference
---

# printSupport2:SupportedFormats

Specifies the Page Description Language (PDL) formats supported by the virtual printer.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[<\printSupport2:Extension\>](element-printsupport2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[<\printSupport2:PrintSupportVirtualPrinter\>](element-printsupport2-printsupportvirtualprinter.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**<printSupport2:SupportedFormats>**

## Syntax

```xml
<printSupport2:SupportedFormats>
  <!-- Child elements -->
  SupportedFormat {0,1000}
</printSupport2:SupportedFormats>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None


### Child elements

| Child element | Description |
|-|-|
| [SupportedFormat](element-printsupport2-supportedformat.md) | Specifies a Page Description Language (PDL) format supported by the virtual printer. |

### Parent elements

| Parent element | Description |
|-|-|
| [printsupport2:PrintSupportVirtualPrinter](element-printsupport2-printsupportvirtualprinter.md) | Specifies a virtual endpoint print queue to be installed with the app. |

### Remarks

For information about developing Print Support Apps, see the [Print support app design guide](/windows-hardware/drivers/devapps/print-support-app-design-guide).

### Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/printsupport/windows10/2` |