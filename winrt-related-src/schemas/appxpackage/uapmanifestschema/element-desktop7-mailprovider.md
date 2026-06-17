---
title: desktop7:MailProvider
description: Registers a dll as a mail provider.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop7:Extension, desktop7:MailProvider]
---

# desktop7:MailProvider

Registers a dll as a mail provider.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:MailProvider>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:MailProvider>`**  

## Syntax

```xml
<desktop7:MailProvider
  Name = 'A required string between 1 and 256 characters in length. This string is localizable.'
  Description = 'A required string between 1 and 2048 characters in length.'
  SimpleMapiLibrary = 'A required string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".'
  ExtendedMapiLibrary = 'A required string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | A descriptive name of the Mail Provider extension. This value is not actually used directly by the system but makes it easier to read the entry in the registry. | A string between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **Description** | A description of the mail provider. | A string between 1 and 2048 characters in length. | Yes |  |
| **SimpleMapiLibrary** | The path to the Dll file that implements a Simple MAPI provider. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *, ending with the case-insensitive file extension ".dll". | Yes |  |
| **ExtendedMapiLibrary** | The path to the Dll file that implements an Extended MAPI provider. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *, ending with the case-insensitive file extension ".dll". | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop7:Extension](element-desktop7-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| **Minimum OS Version** | Windows 10 (Build 19645) |

## Remarks

For more information on registering mail providers, see [File format of MapiSvc.inf](/office/client-developer/outlook/mapi/file-format-of-mapisvc-inf).

## Examples

<!-- Author content goes here -->
