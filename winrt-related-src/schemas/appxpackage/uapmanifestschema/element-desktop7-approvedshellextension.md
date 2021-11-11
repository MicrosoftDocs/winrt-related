---

title: desktop7:ApprovedShellExtension
description: Specifies that a shell extension should be added to the approved shell extensions list when installed. 
ms.date: 10/14/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:ApprovedShellExtension

## Description

Specifies that a shell extension should be added to the approved shell extensions list when installed. 

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
<dd><b>&lt;desktop7:ApprovedShellExtension&gt;</b></dd>
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
<desktop7:ApprovedShellExtension   Name          =  A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
                    Clsid   =  A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.>
</desktop7:ApprovedShellExtension>
```


## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | A descriptive name of the Shell extension. This value is not actually used directly by the system but makes it easier to read the entry in the registry. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| Clsid  | The Clsid of the COM class that implements the Shell Extension.  | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.  | Yes |

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [Extension](element-desktop6-extension.md) | Defines an extensibility point for the application. |  


## Remarks

The process installing the shell extension must have permissions to add entries to the approved shell extensions list. For more information on registering shell extensions, see [Registering Shell Extension Handlers](/windows/win32/shell/reg-shell-exts)


## Requirements

|               |       Value                                                      |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |