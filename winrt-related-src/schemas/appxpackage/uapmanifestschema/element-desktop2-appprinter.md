---

ms.assetid: 0aab475f-cb99-4742-9be5-e0b760c7bf05
title: desktop2:AppPrinter
description: Enables the ability to install software file printers in Windows Desktop Bridge apps.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:AppPrinter

## Description
Enables the ability to install software file printers in Windows Desktop Bridge apps.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop2-extension.md">&lt;desktop2:Extension&gt;</a></dt>
<dd><b>&lt;desktop2:AppPrinter&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<desktop2:AppPrinter DisplayName = A string between 1 and 256 characters in length. This string is localizable.
                     Parameters  = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| DisplayName | The name for the printer queue. | A string between 1 and 256 characters in length. This string is localizable. | Yes |
| Parameters | The file to print. The "%1" token can be used for the full path to the print file being passed into the app. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |

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

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |