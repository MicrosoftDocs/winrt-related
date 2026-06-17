---
title: desktop2:AppPrinter
description: Enables the ability to install software file printers in Windows Desktop Bridge apps.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop2:Extension, desktop2:AppPrinter]
---

# desktop2:AppPrinter

Enables the ability to install software file printers in Windows Desktop Bridge apps.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:Extension>`](element-desktop2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop2:AppPrinter>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:Extension>`](element-desktop2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop2:AppPrinter>`**

## Syntax

```xml
<desktop2:AppPrinter
  DisplayName = 'A required string between 1 and 256 characters in length. This string is localizable.'
  Parameters = 'A required string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  uap11:DataFormat = 'An optional string that can have one of the following values: "xps", or "pdf".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** |  The name for the printer queue.  | A string between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **Parameters** |  The file to print. The "%1" token can be used for the full path to the print file being passed into the app.  | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **uap11:DataFormat** | <!-- TODO: Add description --> | An optional string that can have one of the following values: *xps*, *pdf*. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop2:Extension](element-desktop2-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
| **uap11** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/11` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |

## Remarks

<!-- Author content goes here -->

## Examples

Here is a simple example of the syntax you might use to print to OneNote.

```xml
<Extension Category="windows.appPrinter"> 
    <!-- e.g. “Print to OneNote 2016” -->
    <AppPrinter DisplayName=”ms-resource:ONENOTE_PRINTER_NAME” Parameters=”/insertdoc %1”>  
    </AppPrinter> 
</Extension>
```
