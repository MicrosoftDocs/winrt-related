---
title: cloudFiles:Verb
description: Defines the verbs associated with a file context menu (cloudFiles:Verb).
ms.date: 01/27/2023
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, cloudFiles:Extension, cloudFiles:CloudFiles, cloudFiles:Verb]
---

# cloudFiles:Verb

Specifies the names of items in the File Explorer context menu for cloud based placeholder files.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<cloudFiles:Extension>`](element-cloudfiles-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<cloudFiles:CloudFiles>`](element-cloudfiles-cloudfiles.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<cloudFiles:Verb>`**  

## Syntax

```xml
<cloudFiles:Verb
  Id = 'An alphanumeric string with a value between 3 and 64 characters in length.'
  ClsId = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'>
```


## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The name of the verb. | An alphanumeric string with a value between 3 and 64 characters in length. | Yes |  |
| **Clsid** | The class ID of the app that implements the associated verb. | An alphanumeric string with a value between 3 and 64 characters in length. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [cloudFiles:CloudFilesContextMenus](element-cloudfiles-cloudfilescontextmenus.md) | Registration of a context menu for a cloud based placeholder file. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/cloudfiles/windows10` |
| **Minimum OS Version** | Windows 10 (Build 19645) |
