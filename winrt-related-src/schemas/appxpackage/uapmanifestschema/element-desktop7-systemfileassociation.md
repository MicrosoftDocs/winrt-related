---

title: desktop7:SystemFileAssociation
description: Registers an application.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:SystemFileAssociation

## Description
Registers system file associations for an app. 

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
<dt><a href="element-desktop7-extension.md">&lt;desktop7:Extension&gt;</a></dt>
<dd><b>&lt;desktop7:SystemFileAssociation&gt;</b></dd>
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
```xml
<desktop7:SystemFileAssociation   FileType          =  A string between 1 and 64 characters in length that begins with . and cannot contain these characters: <, >, :, ", |, ?, or *.
                    FullDetails?          =  A string between 1 and 256 characters in length. 
                    PreviewDetails?          =  A string between 1 and 256 characters in length. 
                    PreviewTitle?          =  A string between 1 and 256 characters in length.
                    TileInfo?          =  A string between 1 and 256 characters in length.
                    ExtendedTileInfo?          =  A string between 1 and 256 characters in length.
                    InfoTip?          =  A string between 1 and 256 characters in length.
                    QuickTip?          =  A string between 1 and 256 characters in length.>
</desktop7:SystemFileAssociation>
```



## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| FileType | The file type for which the associations are made. |  A string between 1 and 64 characters in length that begins with . and cannot contain these characters: <, >, :, ", \|, ?, or *. | Yes |
| FullDetails | Properties are displayed on the Details tab of the Properties dialog box. This is the complete list of properties that the file type supports. | A string between 1 and 256 characters in length. | No |
| PreviewDetails | Properties are displayed in the Preview Pane. | A string between 1 and 256 characters in length. | No |
| PreviewTitle | Properties are displayed in the title area of the Preview Pane next to the thumbnail for the item. The maximum number of entries is 3. If the property list contains more than the maximum allowable number, the rest of the entries are ignored. | A string between 1 and 256 characters in length. | No |
| TileInfo | Properties are displayed when the list view is in Tiles view mode. The maximum number of entries is 3. If the property list contains more than the maximum allowable number, the rest of the entries are ignored. | A string between 1 and 256 characters in length. | No |
| ExtendedTileInfo | Properties are displayed for an item when the list view is in Extended Tile view mode. | A string between 1 and 256 characters in length. | No |
| InfoTip | Properties are displayed in an InfoTip when a user hovers over an item. | A string between 1 and 256 characters in length. | No |
| QuickTip | Properties are displayed when it is difficult to retrieve properties directly from an item, such as when the item must be accessed over a slow network connection. It is recommended that the properties named here, such as Type or Size, do not require opening the file stream to determine their value. | A string between 1 and 256 characters in length. | No |

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [Extension](element-desktop7-extension.md) | Defines an extensibility point for the application. |  


## Remarks

For information on registering applications, see [Application Registration](/windows/win32/shell/app-registration).


## Requirements

|               |       Value                                                      |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |