---
ms.assetid: 0aab475f-cb99-4742-9be5-e0b760c7bf05
title: desktop2:AppPrinter
description: Enables the ability to install software file printers in Windows Desktop Bridge apps.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:AppPrinter

Enables the ability to install software file printers in Windows Desktop Bridge apps.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[desktop2:Extension](element-desktop2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop2:AppPrinter\>**

## Syntax

```xml
<desktop2:AppPrinter 
    DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.'
    Parameters  = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** | The name for the printer queue. | A string between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **Parameters** | The file to print. The "%1" token can be used for the full path to the print file being passed into the app. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop2:Extension](element-desktop2-extension.md) | Declares an extensibility point for the app. |

## Examples

Here is a simple example of the syntax you might use to print to OneNote.

```xml
<Extension Category="windows.appPrinter"> 
    <!-- e.g. “Print to OneNote 2016” -->
    <AppPrinter DisplayName=”ms-resource:ONENOTE_PRINTER_NAME” Parameters=”/insertdoc %1”>  
    </AppPrinter> 
</Extension>
```

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
| Minimum OS Version | Windows 10 version 1703 (Build 15063) |
