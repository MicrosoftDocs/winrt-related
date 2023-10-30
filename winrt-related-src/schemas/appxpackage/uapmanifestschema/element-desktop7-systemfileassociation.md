---
title: desktop7:SystemFileAssociation
description: Registers system file associations for an app. 
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:SystemFileAssociation

Registers system file associations for an app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop7:Extension\>](element-desktop7-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop7:SystemFileAssociation\>**

## Syntax

```xml
<desktop7:SystemFileAssociation
  FileType = 'A string with a value between 1 and 64 characters in length that begins with a period (".") and cannot contain these characters: <, >, :, ", |, ?, or *.'
  FullDetails = 'An optional string with a value between 1 and 256 characters in length.'
  PreviewDetails = 'An optional string with a value between 1 and 256 characters in length.'
  PreviewTitle = 'An optional string with a value between 1 and 256 characters in length.'
  TileInfo = 'An optional string with a value between 1 and 256 characters in length.'
  ExtendedTileInfo = 'An optional string with a value between 1 and 256 characters in length.'
  InfoTip = 'An optional string with a value between 1 and 256 characters in length.'
  QuickTip = 'An optional string with a value between 1 and 256 characters in length.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **FileType** | The file type for which the associations are made. | A string with a value between 1 and 64 characters in length that begins with a period (`.`) and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |
| **FullDetails** | Properties are displayed on the Details tab of the Properties dialog box. This is the complete list of properties that the file type supports. | An optional string with a value between 1 and 256 characters in length. | No |  |
| **PreviewDetails** | Properties are displayed in the Preview Pane. | An optional string with a value between 1 and 256 characters in length. | No |  |
| **PreviewTitle** | Properties are displayed in the title area of the Preview Pane next to the thumbnail for the item. The maximum number of entries is 3. If the property list contains more than the maximum allowable number, the rest of the entries are ignored. | An optional string with a value between 1 and 256 characters in length. | No |  |
| **TileInfo** | Properties are displayed when the list view is in Tiles view mode. The maximum number of entries is 3. If the property list contains more than the maximum allowable number, the rest of the entries are ignored. | An optional string with a value between 1 and 256 characters in length. | No |  |
| **ExtendedTileInfo** | Properties are displayed for an item when the list view is in Extended Tile view mode. | An optional string with a value between 1 and 256 characters in length. | No |  |
| **InfoTip** | Properties are displayed in an InfoTip when a user hovers over an item. | An optional string with a value between 1 and 256 characters in length. | No |  |
| **QuickTip** | Properties are displayed when it is difficult to retrieve properties directly from an item, such as when the item must be accessed over a slow network connection. It is recommended that the properties named here, such as Type or Size, do not require opening the file stream to determine their value. | An optional string with a value between 1 and 256 characters in length. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop7:Extension](element-desktop7-extension.md) | Defines an extensibility point for the application. |  

## Remarks

For information on registering applications, see [Application Registration](/windows/win32/shell/app-registration).

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| **Minimum OS Version** | Windows 10 (Build 19645) |
