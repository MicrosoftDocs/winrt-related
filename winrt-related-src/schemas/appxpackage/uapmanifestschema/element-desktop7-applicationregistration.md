---

title: desktop7:ApplicationRegistration
description: Registers an application, replacing the need to register the application in the system PATH variable.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:ApplicationRegistration

## Description
Registers an application in the registry, replacing the need to register the application in the system PATH variable.

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
<dd><b>&lt;desktop7:ApplicationRegistration&gt;</b></dd>
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
<desktop7:ApplicationRegistration   Name          =  A string between 1 and 256 characters in length. This string is localizable.
                    Path          =  A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.  
                    ApplicationName          =  A string between 1 and 256 characters in length. 
                    ApplicationDescription          =  A string between 1 and 256 characters in length.>
</desktop7:ApplicationRegistration>
```



## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | A display name for the application. |  A string between 1 and 256 characters in length. This string is localizable. | Yes |
| Path | The path to the application. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", \|, ?, or *. | Yes |
| ApplicationName | The name of the application. | Yes |
| ApplicationDescription | The description of the application. | A string between 1 and 256 characters in length. | Yes |

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