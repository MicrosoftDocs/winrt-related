---
title: uap4:Kind
description: Specifies the Kind value.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap4:Extension, uap4:FileTypeAssociation, uap4:KindMap, uap4:Kind]
keywords: windows 10, uwp, schema, manifest, desktop, extension
---

# uap4:Kind

Specifies the Kind value.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap4:Extension>`](element-uap4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap4:FileTypeAssociation>`](element-uap-filetypeassociation.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap4:KindMap>`](element-uap4-kindmap.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap4:Kind>`**

## Syntax

```xml
<uap4:Kind
  Value = 'A required string that can have one of the following values: "calendar", "communication", "contact", "document", "email", "feed", "folder", "game", "instantmessage", "journal", "link", "movie", "music", "note", "picture", "program", "recordedtv", "searchfolder", "task", "unknown", "video", or "webhistory".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Value** | The Kind value. | A string that can have one of the following values: *calendar*, *communication*, *contact*, *document*, *email*, *feed*, *folder*, *game*, *instantmessage*, *journal*, *link*, *movie*, *music*, *note*, *picture*, *program*, *recordedtv*, *searchfolder*, *task*, *unknown*, *video*, or *webhistory*. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap4:KindMap](element-uap4-kindmap.md) | Specifies what Kind is and how it's used. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
