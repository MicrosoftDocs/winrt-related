---
title: desktop2:DesktopPreviewHandler
description: Enables declaration of a preview handler for a file type association.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop2:Extension, desktop2:FileTypeAssociation, desktop2:DesktopPreviewHandler]
---

# desktop2:DesktopPreviewHandler

Enables declaration of a preview handler for a file type association.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:Extension>`](element-desktop2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:FileTypeAssociation>`](element-uap-filetypeassociation.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop2:DesktopPreviewHandler>`**

## Syntax

```xml
<desktop2:DesktopPreviewHandler
  Clsid = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  desktop10:DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.'
  ManualSafeSave = 'An optional boolean value.'
  EnableShareDenyNone = 'An optional boolean value.'
  EnableShareDenyWrite = 'An optional boolean value.'
  NoOplock = 'An optional boolean value.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Clsid** |  The ID of the class in the app's package.  | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **desktop10:DisplayName** |  The display name for the preview handler.  | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |
| **ManualSafeSave** |  Sets STGM_TRANSACTED (true = off).  | An optional boolean value. | No |  |
| **EnableShareDenyNone** |  Sets STGM_SHARE_DENY_NONE.  | An optional boolean value. | No |  |
| **EnableShareDenyWrite** |  Sets STGM_SHARE_DENY_WRITE.  | An optional boolean value. | No |  |
| **NoOplock** |  Disables oplock logic. This is used to close the file if another process attempts to access the file.  | An optional boolean value. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap:FileTypeAssociation](element-uap-filetypeassociation.md) | Declares an app extensibility point of type **windows.fileTypeAssociation**. A file type association indicates that the app is registered to handle files of the specified types. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |

## Remarks

Note that the Clsid attribute from PreviewHandler **must** match the ID attribute under the Class element in the [SurrogateServer](element-com-surrogateserver.md) element from the COM registration in the app manifest.

## Examples

<!-- Author content goes here -->
