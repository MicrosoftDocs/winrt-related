---
title: desktop7:SystemFileAssociation
description: Registers system file associations for an app. 
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
no-loc: [Package, Applications, Application, Extensions, desktop7:Extension, desktop7:SystemFileAssociation]
---

# desktop7:SystemFileAssociation

Registers system file associations for an app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:SystemFileAssociation>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:SystemFileAssociation>`**

## Syntax

```xml
<desktop7:SystemFileAssociation
  FileType = 'A required string between 1 and 64 characters in length that must begin with a period, cannot have additional periods, and cannot contain these characters: <, >, :, ", /, \, &#124;, ?, or *.'
  FullDetails = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  PreviewDetails = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  PreviewTitle = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  TileInfo = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  ExtendedTileInfo = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  InfoTip = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  QuickTip = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **FileType** | The file type for which the associations are made. | A string between 1 and 64 characters in length that must begin with a period, cannot have additional periods, and cannot contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | Yes |  |
| **FullDetails** | Properties are displayed on the Details tab of the Properties dialog box. This is the complete list of properties that the file type supports. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **PreviewDetails** | Properties are displayed in the Preview Pane. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **PreviewTitle** | Properties are displayed in the title area of the Preview Pane next to the thumbnail for the item. The maximum number of entries is 3. If the property list contains more than the maximum allowable number, the rest of the entries are ignored. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **TileInfo** | Properties are displayed when the list view is in Tiles view mode. The maximum number of entries is 3. If the property list contains more than the maximum allowable number, the rest of the entries are ignored. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **ExtendedTileInfo** | Properties are displayed for an item when the list view is in Extended Tile view mode. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **InfoTip** | Properties are displayed in an InfoTip when a user hovers over an item. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **QuickTip** | Properties are displayed when it is difficult to retrieve properties directly from an item, such as when the item must be accessed over a slow network connection. It is recommended that the properties named here, such as Type or Size, do not require opening the file stream to determine their value. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

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

For information on registering applications, see [Application Registration](/windows/win32/shell/app-registration).

## Examples

<!-- Author content goes here -->
