---

title: desktop7:ControlPanelItem
description: Registers an extension as a control panel item.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:ControlPanelItem

## Description
Registers an extension as a control panel item.

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
<dd><b>&lt;desktop7:ControlPanelItem&gt;</b></dd>
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
<desktop7:ControlPanelItem   Name          =  A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
                    SystemApplicationName          =  A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
                    SystemControlPanelCategory          =  A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
                    SystemSoftwareTasksFileUrl          =  A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
                    Clsid   =  A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. >
    desktop7:DefaultIcon
    desktop7:LocalizedString
    desktop7:InfoTip
</desktop7:ControlPanelItem>
```



## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | A descriptive name of the Shell extension. This value is not actually used directly by the system but makes it easier to read the entry in the registry. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| SystemApplicationName | The canonical name of the item. The command of form `control.exe /name [System.ApplicationName]` opens the item. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| SystemControlPanelCategory | A value that declares the control panel categories where the item appears. Multiple categories are separated by commas. For more information see [Assigning Control Panel Categories](/previous-versions/windows/desktop/legacy/cc144183(v=vs.85))| A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| SystemSoftwareTasksFileUrl | The path of the XML file that defines task links.  This provides a sub-list of items underneath this Control Panel Item, when Control Panel is viewed in the “Category” mode. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| Clsid  | The Clsid of the COM class that implements the Shell Extension.  | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.  | Yes |

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop7:DefaultIcon](element-desktop7-defaulticon.md) | Specifies the icon to show for the item in the Control Panel. |  
| [desktop7:LocalizedString](element-desktop7-localizedstring.md) | Specifies the localized string to show for the item in the Control Panel. |  
| [desktop7:InfoTip](element-desktop7-infotip.md) | Specifies the Infotip string to show when the mouse hovers over the item’s icon. |  

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [Extension](element-desktop7-extension.md) | Defines an extensibility point for the application. |  


## Remarks




## Requirements

|               |       Value                                                      |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |