---

title: desktop7:MailProvider
description: Registers a dll as a mail provider.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:MailProvider

## Description
Registers a dll as a mail provider.

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
<dd><b>&lt;desktop7:MailProvider&gt;</b></dd>
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
<desktop7:MailProvider   Name          =  A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
                    Description          =  A string between 1 and 256 characters in length.
                    SimpleMapiLibrary          =  A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".  
                    ExtendedMapiLibrary          =  A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".>
</desktop7:MailProvider>
```



## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | A descriptive name of the Mail Provider extension. This value is not actually used directly by the system but makes it easier to read the entry in the registry. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| Description | A description of the mail provider. | A string between 1 and 256 characters in length. | Yes |
| SimpleMapiLibrary | The path to the Dll file that implements a Simple MAPI provider. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", \|, ?, or *, ending with the case-insensitive file extension ".dll". | Yes |
| EntendedMapiLibrary | The path to the Dll file that implements a Simple MAPI provider. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", \|, ?, or *, ending with the case-insensitive file extension ".dll". | Yes |

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [Extension](element-desktop7-extension.md) | Defines an extensibility point for the application. |  


## Remarks

For more information on registering mail providers, see [File format of MapiSvc.inf](/office/client-developer/outlook/mapi/file-format-of-mapisvc-inf).



## Requirements

|               |       Value                                                      |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |