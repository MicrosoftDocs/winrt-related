---
title: desktop7:ControlPanelItem
description: Registers an extension as a control panel item.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:ControlPanelItem

Registers an extension as a control panel item.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop7:Extension\>](element-desktop7-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop7:ControlPanelItem\>**

## Syntax

```xml
<desktop7:ControlPanelItem
    Name = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
    SystemApplicationName = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
    SystemControlPanelCategory = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
    SystemSoftwareTasksFileUrl = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
    Clsid = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' >

    desktop7:DefaultIcon
    desktop7:LocalizedString
    desktop7:InfoTip

</desktop7:ControlPanelItem>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | A descriptive name of the Shell extension. This value is not actually used directly by the system but makes it easier to read the entry in the registry. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **SystemApplicationName** | The canonical name of the item. The command of form `control.exe /name [System.ApplicationName]` opens the item. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **SystemControlPanelCategory** | A value that declares the control panel categories where the item appears. Multiple categories are separated by commas. For more information see [Assigning Control Panel Categories](/previous-versions/windows/desktop/legacy/cc144183(v=vs.85))| A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **SystemSoftwareTasksFileUrl** | The path of the XML file that defines task links.  This provides a sub-list of items underneath this Control Panel Item, when Control Panel is viewed in the “Category” mode. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **Clsid**  | The Clsid of the COM class that implements the Shell Extension.  | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.  | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [desktop7:DefaultIcon](element-desktop7-defaulticon.md) | Specifies the icon to show for the item in the Control Panel. |  
| [desktop7:LocalizedString](element-desktop7-localizedstring.md) | Specifies the localized string to show for the item in the Control Panel. |  
| [desktop7:InfoTip](element-desktop7-infotip.md) | Specifies the Infotip string to show when the mouse hovers over the item’s icon. |  

### Parent elements

| Parent element | Description |
|-|-|
| [Extension](element-desktop7-extension.md) | Defines an extensibility point for the application. |  

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
